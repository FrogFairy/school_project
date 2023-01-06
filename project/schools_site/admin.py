from django.contrib import admin
from .models import Addresses, Predprof, Schools, Sections, Universities


@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ('id', 'adm_area', 'district', 'address', 'public_phone', 'available_k', 'available_o',
                    'available_z', 'available_s')
    list_filter = ('adm_area', 'district', 'available_k',
                   'available_o', 'available_z', 'available_s')
    search_fields = ('adm_area', 'district')
    ordering = ('id', )


@admin.register(Predprof)
class PredprofAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('title', 'description')
    search_fields = ('title',)
    ordering = ('id',)


@admin.register(Schools)
class SchoolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'full_name', 'educational_services', 'institutions_addresses',
                    'legal_organization', 'chief_name', 'public_phone', 'email', 'web_site',
                    'predprof_id', 'universities_id', 'sections_id')
    list_filter = ('educational_services', 'legal_organization', 'predprof_id')
    search_fields = ('short_name', 'full_name')
    ordering = ('id',)


@admin.register(Sections)
class SectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'age_category', 'free', 'form')
    list_filter = ('category', 'age_category', 'free', 'form')
    search_fields = ('title',)
    ordering = ('id',)


@admin.register(Universities)
class UniversitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'count', 'school_id')
    list_filter = ('school_id',)
    search_fields = ('title',)
    ordering = ('id',)