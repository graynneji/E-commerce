# Generated by Django 3.1 on 2021-08-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='grid_size',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
