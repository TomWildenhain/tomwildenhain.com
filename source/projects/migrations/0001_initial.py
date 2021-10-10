# Generated by Django 2.0 on 2017-12-28 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('start_date', models.CharField(blank=True, default='', max_length=200)),
                ('end_date', models.CharField(blank=True, default='', max_length=200)),
                ('project_description', models.TextField()),
                ('github_link', models.CharField(blank=True, default='', max_length=200)),
                ('index', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SkillToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200)),
                ('index', models.PositiveIntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]