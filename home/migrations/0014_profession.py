# Generated by Django 4.2.2 on 2023-07-04 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_image_userprofile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
