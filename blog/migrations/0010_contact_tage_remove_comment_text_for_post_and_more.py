# Generated by Django 5.0 on 2023-12-25 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_created_comment_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text_for_post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='msg',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='author',
            name='description',
        ),
        migrations.RemoveField(
            model_name='author',
            name='title',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='link',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=2, max_length=212),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=212)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='articles')),
                ('title', models.CharField(max_length=212)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tage')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.article'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
