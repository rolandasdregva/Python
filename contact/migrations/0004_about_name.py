# Generated by Django 4.0.4 on 2022-07-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_about_imageabout_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]