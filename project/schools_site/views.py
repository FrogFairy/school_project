from django.shortcuts import render, get_object_or_404
from .models import Schools, Addresses, Predprof, Sections, Universities
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    """Обработчик главной страницы"""
    # Все школы
    schools_list = Schools.schools_list.order_by("id").all()
    # Школы по выбранным фильтрам
    response = request.POST
    if response:
        # фильтрация по району
        if "district[]" in response and response.getlist("district[]"):
            districts = response.getlist("district[]")
            for i in schools_list:
                if not i.get_addresses().filter(district__in=districts):
                    schools_list = schools_list.exclude(id=i.id)

        if "adm_area[]" in response:
            addresses = Addresses.objects.filter(district__in=response.getlist("adm_area[]")).all()
            for i in schools_list:
                if not list(filter(lambda x: x in addresses, i.get_addresses())):
                    schools_list = schools_list.exclude(id=i.id)

        if "universities[]" in response:
            universities = Universities.objects.filter(title__in=response.getlist("universities[]")).all()
            for i in schools_list:
                if not list(filter(lambda x: x in universities, i.get_universities())):
                    schools_list = schools_list.exclude(id=i.id)

        if "predprof[]" in response:
            predprof = Predprof.objects.filter(title__in=response.getlist("predprof[]")).all()
            for i in schools_list:
                if not list(filter(lambda x: x in predprof, i.get_predprof())):
                    schools_list = schools_list.exclude(id=i.id)

        if "category[]" in response:
            category = Sections.objects.filter(category__in=response.getlist("category[]")).all()
            for i in schools_list:
                if not list(filter(lambda x: x in category, i.get_sections())):
                    schools_list = schools_list.exclude(id=i.id)

        if "disabled[]" in response:
            addresses = Addresses.objects
            a = response.getlist("disabled[]")
            if "k" in a:
                addresses = addresses.filter(available_k__in=["частично", "полностью"])
            if "o" in a:
                addresses = addresses.filter(available_o__in=["частично", "полностью"])
            if "s" in a:
                addresses = addresses.filter(available_s__in=["частично", "полностью"])
            if "z" in a:
                addresses = addresses.filter(available_z__in=["частично", "полностью"])
            for i in schools_list:
                if not list(filter(lambda x: x in addresses, i.get_addresses())):
                    schools_list = schools_list.exclude(id=i.id)

        if "forms[]" in response:
            schools_list = schools_list.filter(educational_services__in=response.getlist("forms[]"))

        # номер страницы обнуляем
        page = 1
    else:
        page = request.GET.get('page')
    # Информация для фильтров
    districts = Addresses.objects.values('district').distinct().order_by("district")
    adm_area = Addresses.objects.values('adm_area').distinct().order_by("adm_area")
    predprof = Predprof.objects.values('title').distinct().order_by("title")
    categories = Sections.objects.values('category').distinct().order_by("category")
    universities = Universities.objects.values('title').distinct().order_by("title")

    f = Schools.objects.values('educational_services').distinct()
    forms = []
    for i in f:
        forms += i["educational_services"].split(', ')
    forms.remove("-")
    forms = list(set(forms))

    paginator = Paginator(schools_list, 10)  # По 10 школ на каждой странице.
    try:
        schools = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, возвращаем первую страницу.
        schools = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
        schools = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'schools': schools, 'districts': districts,
                                         'predprof': predprof, 'categories': categories,
                                         'universities': universities, 'forms': forms,
                                         'page': page, 'adm_area': adm_area})


def school_page(request, url):
    """Обработчик страницы отдельной школы"""
    school = get_object_or_404(Schools, web_site=f"{url}.mskobr.ru")
    addresses = school.get_addresses()
    predprof = school.get_predprof()
    sections = school.get_sections()
    universities = school.get_universities()
    forms = school.get_forms()
    categories = Sections.objects.values('category').distinct().order_by("category")
    return render(request, 'school_page.html', {'school': school, 'addresses': addresses,
                                                "predprof": predprof, "sections": sections,
                                                "universities": universities, "forms": forms,
                                                "categories": categories})