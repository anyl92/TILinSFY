# Generated by Django 2.2.6 on 2019-10-21 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
