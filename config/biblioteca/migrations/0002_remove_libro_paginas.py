# Generated by Django 2.2 on 2020-05-14 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='paginas',
        ),
    ]
