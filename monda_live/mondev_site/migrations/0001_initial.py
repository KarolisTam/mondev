# Generated by Django 4.2.2 on 2023-07-05 12:04

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='updated at')),
                ('name', models.CharField(db_index=True, max_length=127, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=127, null=True, verbose_name='slug')),
                ('content', tinymce.models.HTMLField(verbose_name='content')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='published at')),
                ('is_public', models.BooleanField(default=True, verbose_name='publicly available')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]