from django import template

register = template.Library()


@register.filter
def in_category(section, category):
    """Фильтр для шаблона. Выбирает объект по категории"""
    return section.filter(category=category).all()