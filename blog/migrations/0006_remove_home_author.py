# Generated by Django 5.0 on 2023-12-24 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_comment_website_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='author',
        ),
    ]
