# Generated by Django 3.2.4 on 2021-07-04 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0009_remove_citizen_citizen_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='citizen_img',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]
