from django.shortcuts import render, get_object_or_404
from .models import Schools, Addresses, Predprof, Sections, Universities
from .help import remove_double


def home(request):
    """Обработчик главной страницы"""
    # Все школы
    schools = Schools.schools_list.all()
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

    return render(request, 'home.html', {'schools': schools, 'districts': districts,
                                         'predprof': predprof, 'categories': categories,
                                         'universities': universities, 'forms': forms})


def school_page(request, url):
    """Обработчик страницы отдельной школы"""
    school = get_object_or_404(Schools, web_site=f"{url}.mskobr.ru")
    return render(request, 'school_page.html', {'school': school})