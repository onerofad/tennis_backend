# Generated by Django 4.2.4 on 2023-09-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default='', max_length=255),
        ),
    ]
