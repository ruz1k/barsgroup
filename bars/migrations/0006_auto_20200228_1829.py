# Generated by Django 3.0 on 2020-02-28 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0005_auto_20200228_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='answer',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]