# Generated by Django 4.0.4 on 2022-05-28 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('INDIGGator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questionHeading',
            new_name='question',
        ),
    ]
