# Generated by Django 4.0 on 2022-01-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=264, unique=True)),
                ('lastName', models.CharField(max_length=264)),
                ('email', models.CharField(max_length=264)),
            ],
        ),
    ]
