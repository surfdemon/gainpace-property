# Generated by Django 5.1.3 on 2024-11-27 15:07

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('ref', models.CharField(max_length=5)),
                ('rent', models.FloatField()),
                ('min_tenancy', models.IntegerField()),
                ('max_tenancy', models.IntegerField()),
                ('deposit', models.FloatField()),
                ('ad_link', models.CharField(max_length=200)),
                ('g_form', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('max_tenants', models.IntegerField()),
                ('bills', models.BooleanField(default=False)),
                ('broadband', models.BooleanField(default=False)),
                ('student', models.BooleanField(default=False)),
                ('families', models.BooleanField(default=False)),
                ('pets', models.BooleanField(default=False)),
                ('smoking', models.BooleanField(default=False)),
                ('garden', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('furnished', models.IntegerField(choices=[(0, 'Either'), (1, 'Furnished'), (2, 'Unfurnished')], default=0)),
                ('epc', models.CharField(max_length=1)),
                ('dss', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.CharField(max_length=200)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='property.property')),
            ],
            options={
                'verbose_name': 'Property Image',
                'verbose_name_plural': 'Property Images',
                'ordering': ['created_on'],
            },
        ),
    ]
