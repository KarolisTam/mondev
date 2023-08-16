# Generated by Django 4.2.2 on 2023-08-04 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0016_coursegroupmember_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGroupSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='updated at')),
                ('name', models.CharField(db_index=True, max_length=127, verbose_name='name')),
                ('date', models.DateField(null=True, verbose_name='date')),
                ('stream_url', models.URLField(null=True, verbose_name='stream url')),
                ('course_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_groups', to='academy.coursegroup', verbose_name='course group')),
                ('course_topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_topics', to='academy.coursetopic', verbose_name='course topic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField(verbose_name='check in')),
                ('check_out', models.DateTimeField(verbose_name='check out')),
                ('course_group_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_group_members', to='academy.coursegroupmember', verbose_name='course group member')),
                ('course_group_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_group_sessions', to='academy.coursegroupsession', verbose_name='course group session')),
            ],
        ),
    ]