# Generated by Django 4.1.3 on 2022-12-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_game_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='time',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
