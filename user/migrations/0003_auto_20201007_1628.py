# Generated by Django 3.0.5 on 2020-10-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_signup_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='id',
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
    ]
