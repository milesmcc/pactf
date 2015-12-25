# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0002_auto_20151225_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctfproblem',
            name='description_html',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ctfproblem',
            name='hint_html',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='ctfproblem',
            name='grader',
            field=models.FilePathField(help_text='Path to the grading script', match='.*\\.py', path="/Volumes/Yatharth's Internal PD/Workspace/andover/pactf/framework/django/ctfproblems", recursive=True),
        ),
    ]
