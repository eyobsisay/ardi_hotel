# Generated by Django 4.0.6 on 2024-01-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_us_images/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Amenity Name')),
            ],
            options={
                'verbose_name': 'Amenity',
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=255, verbose_name='Hotel Name')),
                ('address', models.TextField(verbose_name='Address')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('map_embed_code', models.TextField(blank=True, null=True, verbose_name='Map Embed Code')),
            ],
            options={
                'verbose_name': 'Contact Information',
                'verbose_name_plural': 'Contact Information',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Facility Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('icon', models.ImageField(upload_to='facility_icons/', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Facility',
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='gallery_images/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Gallery Image',
                'verbose_name_plural': 'Gallery Images',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Hotel Name')),
                ('address', models.TextField(verbose_name='Address')),
                ('phone_number1', models.CharField(max_length=15, verbose_name='Phone Number 1')),
                ('phone_number2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number 2')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('description', models.TextField(verbose_name='Description')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='hotel_logos/', verbose_name='Hotel Logo')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
            },
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='slider_images/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Slider Image',
                'verbose_name_plural': 'Slider Images',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Position')),
                ('content', models.TextField(verbose_name='Testimonial Content')),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonial_images/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=255, verbose_name='Room Type')),
                ('description', models.TextField(verbose_name='Description')),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price per Night')),
                ('capacity', models.IntegerField(verbose_name='Capacity')),
                ('image', models.ImageField(upload_to='accommodation_images/', verbose_name='Image')),
                ('amenities', models.ManyToManyField(blank=True, to='website.amenity', verbose_name='Amenities')),
            ],
            options={
                'verbose_name': 'Accommodation',
                'verbose_name_plural': 'Accommodations',
            },
        ),
    ]
