# Generated by Django 4.2.17 on 2024-12-11 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_about_me_profile_occupation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
