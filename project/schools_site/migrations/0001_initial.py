# Generated by Django 4.1.4 on 2023-01-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm_area', models.TextField(blank=True, null=True)),
                ('district', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('public_phone', models.TextField(blank=True, null=True)),
                ('available_k', models.TextField(blank=True, null=True)),
                ('available_o', models.TextField(blank=True, null=True)),
                ('available_z', models.TextField(blank=True, null=True)),
                ('available_s', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'addresses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Predprof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'predprof',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.TextField(blank=True, null=True)),
                ('full_name', models.TextField(blank=True, null=True)),
                ('educational_services', models.TextField(blank=True, null=True)),
                ('institutions_addresses', models.TextField(blank=True, null=True)),
                ('legal_organization', models.TextField(blank=True, null=True)),
                ('chief_name', models.TextField(blank=True, null=True)),
                ('public_phone', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('web_site', models.TextField(blank=True, null=True)),
                ('predprof_id', models.TextField(blank=True, null=True)),
                ('universities_id', models.TextField(blank=True, null=True)),
                ('sections_id', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'schools',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('age_category', models.TextField(blank=True, null=True)),
                ('free', models.BooleanField(blank=True, null=True)),
                ('form', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sections',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('school_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'universities',
                'managed': True,
            },
        ),
    ]
