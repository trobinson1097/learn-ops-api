# Generated by Django 4.2.8 on 2024-02-22 04:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("LearningAPI", "0041_students_by_cohort_db_function"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="learningrecord",
            unique_together={("student", "weight")},
        ),
    ]