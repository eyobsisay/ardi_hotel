# Generated by Django 4.0.6 on 2024-01-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_hotelservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelservice',
            name='image',
            field=models.ImageField(default=1, upload_to='service_images/', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
