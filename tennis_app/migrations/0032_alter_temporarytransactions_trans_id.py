# Generated by Django 4.2.4 on 2024-10-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis_app', '0031_alter_temporarytransactions_trans_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporarytransactions',
            name='trans_id',
            field=models.CharField(default=9594091352, max_length=255),
        ),
    ]