# Generated by Django 2.2.6 on 2019-10-22 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]