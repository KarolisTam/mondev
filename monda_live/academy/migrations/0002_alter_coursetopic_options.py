# Generated by Django 4.2.2 on 2023-07-03 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursetopic',
            options={'ordering': ('order', 'course', 'topic'), 'verbose_name': 'course topic', 'verbose_name_plural': 'course topics'},
        ),
    ]