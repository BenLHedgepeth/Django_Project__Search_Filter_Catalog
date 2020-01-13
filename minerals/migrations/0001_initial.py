# Generated by Django 2.2.7 on 2020-01-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image_filename', models.ImageField(blank=True, max_length=255, upload_to='')),
                ('image_caption', models.CharField(blank=True, max_length=255)),
                ('category', models.CharField(blank=True, max_length=255)),
                ('formula', models.CharField(blank=True, max_length=255)),
                ('strunz_classification', models.CharField(blank=True, max_length=255)),
                ('crystal_system', models.CharField(blank=True, max_length=255)),
                ('unit_cell', models.CharField(blank=True, max_length=255)),
                ('color', models.CharField(blank=True, max_length=255)),
                ('crystal_symmetry', models.CharField(blank=True, max_length=255)),
                ('cleavage', models.CharField(blank=True, max_length=255)),
                ('mohs_scale_hardness', models.CharField(blank=True, max_length=255)),
                ('luster', models.CharField(blank=True, max_length=255)),
                ('streak', models.CharField(blank=True, max_length=255)),
                ('diaphaneity', models.CharField(blank=True, max_length=255)),
                ('optical_properties', models.CharField(blank=True, max_length=255)),
                ('refractive_index', models.CharField(blank=True, max_length=255)),
                ('crystal_habit', models.CharField(blank=True, max_length=255)),
                ('specific_gravity', models.CharField(blank=True, max_length=255)),
                ('group', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
