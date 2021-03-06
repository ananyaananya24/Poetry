# Generated by Django 3.2.2 on 2021-05-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JustWrite', '0002_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='about',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
