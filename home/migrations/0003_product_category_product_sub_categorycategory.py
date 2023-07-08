# Generated by Django 4.2.2 on 2023-06-17 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_Categorycategory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.sub_category'),
        ),
    ]
