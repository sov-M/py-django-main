# Generated by Django 5.1.2 on 2024-10-17 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_articles_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='file',
        ),
    ]