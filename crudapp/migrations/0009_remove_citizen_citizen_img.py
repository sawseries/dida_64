# Generated by Django 3.2.4 on 2021-07-04 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0008_auto_20210703_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='citizen_img',
        ),
    ]