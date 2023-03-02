from django import template
from users.models import Reviews

register = template.Library()


@register.filter
def in_category(section, category):
    """Фильтр для шаблона. Выбирает секцию по категории"""
    return section.filter(category=category).all()


@register.filter
def is_queryset(data):
    """Фильтр для шаблона. Определяет, является ли объект QuerySet"""
    if type(data) == list:
        return False
    return True


@register.filter
def check_unique(user, school):
    """Фильтр для шаблона. Определяет, оставлял ли пользователь комментарии у школы"""
    if not Reviews.objects.filter(user_id=user.id, school_id=school.id):
        return True
    return False


@register.filter
def get_info(profiles, user_id):
    """Фильтр для шаблона. Выдает информацию о пользователе по айди"""
    profile = profiles.filter(user_id=user_id)[0]
    trans = {"student": "Ученик", "parent": "Родитель", "teacher": "Преподаватель"}
    return f"{trans[profile.role]}, {profile.school.short_name}"