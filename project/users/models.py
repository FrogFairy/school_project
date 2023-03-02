from django.db import models
from django.contrib.auth.models import User
from schools_site.models import Schools
from django.core.validators import MaxValueValidator, MinValueValidator


class Reviews(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.OneToOneField(Schools, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(100),
                                                        MinValueValidator(1)])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role = models.TextField(null=True)
    school = models.OneToOneField(Schools, on_delete=models.CASCADE, null=True)