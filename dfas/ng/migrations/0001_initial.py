# Generated by Django 4.1.3 on 2022-12-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('rilis', models.DateField()),
                ('pengembang', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
            ],
        ),
    ]
