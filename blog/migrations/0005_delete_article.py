# Generated by Django 3.0.8 on 2020-08-11 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogbuster'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]