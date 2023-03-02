from django.shortcuts import render, get_object_or_404
from .models import Schools, Addresses, Predprof, Sections, Universities
from users.models import Reviews, Profile
from django.http import JsonResponse
from django.core import serializers
import json
import math


def home(request):
    """Обработчик главной страницы"""
    # Все школы
    schools_list = Schools.schools_list.order_by("id").all()
    # Школы по выбранным фильтрам
    response = request.POST
    if response:
        districts_filter = response.getlist("district[]") if "district[]" in response and response.getlist("district[]") \
            else None
        adm_area_filter = response.getlist("adm_area[]") if "adm_area[]" in response and response.getlist("adm_area[]") \
            else None
        universities_filter = response.getlist("university[]") if "university[]" in response and response.getlist("university[]") \
            else None
        predprof_filter = response.getlist("predprof[]") if "predprof[]" in response and response.getlist("predprof[]") \
            else None
        category_filter = response.getlist("category[]") if "category[]" in response and response.getlist("category[]") \
            else None
        disabled_filter = response.getlist("disabled[]") if "disabled[]" in response and response.getlist("disabled[]") \
            else None
        forms_filter = response.getlist("forms[]") if "forms[]" in response and response.getlist("forms[]") \
            else None
        search_filter = response.get("search_request") if "search_request" in response else None
        rating = int(response.get("rating")) if "rating" in response and response.get("rating") else None
        if districts_filter or adm_area_filter or universities_filter or predprof_filter or \
                category_filter or disabled_filter or forms_filter or search_filter or rating:
            for i in schools_list:
                if districts_filter and not i.get_addresses().filter(district__in=districts_filter):
                    schools_list = schools_list.exclude(id=i.id)
                if adm_area_filter and not i.get_addresses().filter(adm_area__in=adm_area_filter):
                    schools_list = schools_list.exclude(id=i.id)
                if universities_filter and (not i.get_universities() or not i.get_universities().filter(title__in=universities_filter)):
                    schools_list = schools_list.exclude(id=i.id)
                if predprof_filter and (not i.get_predprof() or not i.get_predprof().filter(title__in=predprof_filter)):
                    schools_list = schools_list.exclude(id=i.id)
                if category_filter and not i.get_sections(category_filter):
                    schools_list = schools_list.exclude(id=i.id)
                if disabled_filter:
                    addresses = i.get_addresses()
                    if "k" in disabled_filter and not addresses.filter(available_k="полностью") or \
                       "o" in disabled_filter and not addresses.filter(available_o="полностью") or \
                       "s" in disabled_filter and not addresses.filter(available_s="полностью") or \
                       "z" in disabled_filter and not addresses.filter(available_z="полностью"):
                        schools_list = schools_list.exclude(id=i.id)
                if forms_filter and (not i.educational_services or
                                     not any([j in forms_filter for j in i.educational_services.split(", ")])):
                    schools_list = schools_list.exclude(id=i.id)
                if search_filter and (search_filter.lower() not in i.full_name.lower() or
                                      search_filter.lower() not in i.short_name.lower()):
                    schools_list = schools_list.exclude(id=i.id)
                if rating and round(get_mean_rating(Reviews.objects.filter(school_id=i.id))) != rating:
                    schools_list = schools_list.exclude(id=i.id)
        # если был совершен переход на другую страницу с фильтрами, то переходим на эту страницу,
        # иначе переходим на 1 страницу
        page = int(response.get("page_number")) if "page_number" in response else 1
    else:
        page = int(request.GET.get('page')) if type(request.GET.get('page')) == int else 1
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

    if page < 1:
        page = 1
    elif page > math.ceil(len(schools_list) / 10):
        page = math.ceil(len(schools_list) / 10)
    schools = schools_list[(page - 1) * 10:page * 10] if schools_list else []
    previous_page_number = page - 1 if page > 1 else 0
    next_page_number = page + 1 if page < math.ceil(len(schools_list) / 10) else 0
    num_pages = math.ceil(len(schools_list) / 10)
    if response:
        absolute_urls = [s.get_absolute_url() for s in schools]
        return JsonResponse({'schools': [i["fields"] for i in json.loads(serializers.serialize("json", schools))],
                             'previous_page_number': str(previous_page_number), 'absolute_urls': absolute_urls,
                             'next_page_number': str(next_page_number), 'number': str(page), 'num_pages': str(num_pages)})
    return render(request, 'home.html', {'schools': schools, 'districts': districts,
                                         'predprof': predprof, 'categories': categories,
                                         'universities': universities, 'forms': forms,
                                         'number': page, 'previous_page_number': previous_page_number,
                                         'next_page_number': next_page_number, 'num_pages': num_pages,
                                         'adm_area': adm_area})


def school_page(request, url):
    """Обработчик страницы отдельной школы"""
    school = get_object_or_404(Schools, web_site=f"{url}.mskobr.ru")
    addresses = school.get_addresses()
    predprof = school.get_predprof()
    sections = school.get_sections()
    universities = school.get_universities()
    forms = school.get_forms()
    categories = Sections.objects.values('category').distinct().order_by("category")

    reviews = Reviews.objects.filter(school_id=school.id)
    mean_rating = get_mean_rating(reviews)
    profiles = Profile.objects.filter(user_id__in=reviews.values("user_id"))
    return render(request, 'school_page.html', {'school': school, 'addresses': addresses,
                                                "predprof": predprof, "sections": sections,
                                                "universities": universities, "forms": forms,
                                                "categories": categories, "reviews": reviews,
                                                "mean_rating": f"{mean_rating:.2f}", "profiles": profiles})


def get_mean_rating(reviews):
    return sum(map(lambda x: int(x.rating), reviews)) // len(reviews) if len(reviews) >= 1 else 0.0