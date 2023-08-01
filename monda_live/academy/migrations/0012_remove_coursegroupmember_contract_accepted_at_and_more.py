# Generated by Django 4.2.2 on 2023-07-24 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy', '0011_coursegroupmember_contract_accepted_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursegroupmember',
            name='contract_accepted_at',
        ),
        migrations.AddField(
            model_name='coursegroupmember',
            name='academy_accepted_contract_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='academy accepted contract at'),
        ),
        migrations.AddField(
            model_name='coursegroupmember',
            name='academy_representative',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accepted_course_members', to=settings.AUTH_USER_MODEL, verbose_name='academy representative'),
        ),
        migrations.AddField(
            model_name='coursegroupmember',
            name='user_accepted_contract_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='user accepted contract at'),
        ),
    ]