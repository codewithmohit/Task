# Generated by Django 3.0.5 on 2020-10-07 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]
