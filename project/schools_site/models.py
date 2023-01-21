from django.db import models
from django.urls import reverse


class SchoolManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class AddressManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class SectionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class PredprofManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class UniversityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Addresses(models.Model):
    adm_area = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    public_phone = models.TextField(blank=True, null=True)
    available_k = models.TextField(blank=True, null=True)
    available_o = models.TextField(blank=True, null=True)
    available_z = models.TextField(blank=True, null=True)
    available_s = models.TextField(blank=True, null=True)

    objects = models.Manager()
    addresses_list = AddressManager()

    class Meta:
        managed = True
        db_table = 'addresses'


class Predprof(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    objects = models.Manager()
    predprof_list = PredprofManager()

    class Meta:
        managed = True
        db_table = 'predprof'


class Schools(models.Model):
    short_name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    educational_services = models.TextField(blank=True, null=True)
    institutions_addresses = models.TextField(blank=True, null=True)
    legal_organization = models.TextField(blank=True, null=True)
    chief_name = models.TextField(blank=True, null=True)
    public_phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    web_site = models.TextField(blank=True, null=True)
    predprof_id = models.TextField(blank=True, null=True)
    universities_id = models.TextField(blank=True, null=True)
    sections_id = models.TextField(blank=True, null=True)

    objects = models.Manager()
    schools_list = SchoolManager()

    def get_absolute_url(self):
        return reverse('schools_site:school_page', args=[self.web_site.split(".")[0]])

    def get_sections(self):
        if self.sections_id:
            sections_id = list(map(int, self.sections_id.split(", ")))
            return Sections.objects.filter(id__in=range(sections_id[0], sections_id[1] + 1))
        return []

    def get_predprof(self):
        if self.predprof_id:
            return Predprof.objects.filter(id__in=list(map(int, self.predprof_id.split(", "))))
        return []

    def get_universities(self):
        if self.universities_id:
            universities_id = list(map(int, self.universities_id.split(", ")))
            return Universities.objects.filter(id__in=range(universities_id[0], universities_id[1] + 1))
        return []

    def get_forms(self):
        if self.educational_services and self.educational_services != "-":
            return list(map(lambda x: "".join(list(map(lambda y: y.capitalize(), x.split()))),
                            self.educational_services.split(", ")))
        return []

    def get_addresses(self):
        return Addresses.objects.filter(id__in=list(map(int, self.institutions_addresses.split(", "))))

    class Meta:
        managed = True
        db_table = 'schools'


class Sections(models.Model):
    title = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    age_category = models.TextField(blank=True, null=True)
    free = models.BooleanField(blank=True, null=True)
    form = models.TextField(blank=True, null=True)

    objects = models.Manager()
    sections_list = SectionManager()

    class Meta:
        managed = True
        db_table = 'sections'


class Universities(models.Model):
    title = models.TextField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    school_id = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    universities_list = UniversityManager()

    class Meta:
        managed = True
        db_table = 'universities'