# Generated by Django 4.0.6 on 2024-01-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_accommodation_description_detail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('header_image', models.ImageField(upload_to='header_images/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Header Image',
                'verbose_name_plural': 'Header Image',
            },
        ),
    ]
