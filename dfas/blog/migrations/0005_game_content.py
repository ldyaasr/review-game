# Generated by Django 4.1.3 on 2022-12-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_game_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
