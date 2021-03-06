# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 13:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('trainer', 'trainer'), ('trainee', 'trainee')], max_length=7)),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Person')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='plan',
            name='user',
        ),
        migrations.AlterField(
            model_name='exercise',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Person'),
        ),
    ]
