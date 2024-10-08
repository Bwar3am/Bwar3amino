# Generated by Django 5.0.7 on 2024-08-25 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('profile_image', models.ImageField(null=True, upload_to='')),
                ('bio', models.CharField(max_length=300)),
            ],
        ),
    ]
