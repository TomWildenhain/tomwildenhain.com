# Generated by Django 2.0 on 2017-12-28 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name_plural': 'education'},
        ),
        migrations.RemoveField(
            model_name='education',
            name='index',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='index',
        ),
        migrations.RemoveField(
            model_name='experiencedescription',
            name='index',
        ),
        migrations.RemoveField(
            model_name='honor',
            name='index',
        ),
        migrations.RemoveField(
            model_name='project',
            name='index',
        ),
        migrations.RemoveField(
            model_name='projectdescription',
            name='index',
        ),
        migrations.AddField(
            model_name='education',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='experience',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='experiencedescription',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='honor',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='projectdescription',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
