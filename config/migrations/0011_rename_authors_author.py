# Generated by Django 5.0.7 on 2024-08-14 16:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0010_alter_authors_username'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='author',
        ),
    ]
