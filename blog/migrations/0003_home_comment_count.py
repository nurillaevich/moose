# Generated by Django 5.0 on 2023-12-24 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='comment_count',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
            preserve_default=False,
        ),
    ]
