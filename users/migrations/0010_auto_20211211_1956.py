# Generated by Django 3.2.9 on 2021-12-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
