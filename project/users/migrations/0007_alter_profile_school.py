# Generated by Django 4.1.4 on 2023-02-28 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools_site', '0001_initial'),
        ('users', '0006_profile_role_profile_school_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools_site.schools'),
        ),
    ]
