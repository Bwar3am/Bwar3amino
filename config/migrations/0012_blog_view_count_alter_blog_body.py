# Generated by Django 5.0.7 on 2024-08-20 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0011_rename_authors_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(max_length=10000),
        ),
    ]