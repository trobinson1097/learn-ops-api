# Generated by Django 4.0.3 on 2022-12-16 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0021_cohortcourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='cohortcourse',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
