# Generated by Django 3.1.2 on 2020-10-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PdfApp', '0009_auto_20201006_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='logo',
            field=models.ImageField(blank=True, default='logos/emart.png', upload_to='logos'),
        ),
    ]
