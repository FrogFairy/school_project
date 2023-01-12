from django.shortcuts import render, get_object_or_404
from .models import Schools, Addresses, Predprof, Sections, Universities
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    """Обработчик главной страницы"""
    # Все школы
    schools_list = Schools.schools_list.order_by('id').all()
    # Информация для фильтров
    districts = Addresses.objects.values('district').distinct().order_by("district")
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
    page = request.GET.get('page')
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
                                         'page': page})


def school_page(request, url):
    """Обработчик страницы отдельной школы"""
    school = get_object_or_404(Schools, web_site=f"{url}.mskobr.ru")
    return render(request, 'school_page.html', {'school': school})