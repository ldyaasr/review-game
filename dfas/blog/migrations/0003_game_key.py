# Generated by Django 4.1.3 on 2022-12-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='key',
            field=models.TextField(null=True),
        ),
    ]
