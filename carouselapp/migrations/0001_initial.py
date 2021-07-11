# Generated by Django 3.2.4 on 2021-07-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
                ('thumnail', models.ImageField(upload_to='carousel/images/')),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=150)),
                ('thumbnail', models.ImageField(upload_to='slider_images/')),
                ('short_decription', models.TextField()),
            ],
        ),
    ]
