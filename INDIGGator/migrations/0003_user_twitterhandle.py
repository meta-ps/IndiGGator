# Generated by Django 4.0.4 on 2022-05-29 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INDIGGator', '0002_games_coursecompleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='twitterHandle',
            field=models.CharField(max_length=255, null=True),
        ),
    ]