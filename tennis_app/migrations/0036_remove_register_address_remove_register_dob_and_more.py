# Generated by Django 4.2.4 on 2025-01-13 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis_app', '0035_alter_silauser_street_address_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='address',
        ),
        migrations.RemoveField(
            model_name='register',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='register',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='register',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='register',
            name='phone',
        ),
        migrations.AlterField(
            model_name='temporarytransactions',
            name='trans_id',
            field=models.CharField(default=4557415429, max_length=255),
        ),
    ]
