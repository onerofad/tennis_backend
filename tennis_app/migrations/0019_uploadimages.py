# Generated by Django 4.2.4 on 2023-09-19 00:49

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis_app', '0018_alter_signup_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('imageurl', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
    ]
