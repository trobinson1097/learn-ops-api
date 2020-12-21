# Generated by Django 3.1.4 on 2020-12-21 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('slack_channel', models.CharField(max_length=55)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('break_start_date', models.DateField()),
                ('break_end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='CourseBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='LearningAPI.course')),
            ],
        ),
        migrations.CreateModel(
            name='LearningObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swbat', models.CharField(max_length=255)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectives', to='LearningAPI.bookchapter')),
            ],
        ),
        migrations.CreateModel(
            name='LightningExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningAPI.coursebook')),
            ],
        ),
        migrations.CreateModel(
            name='NssUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_handle', models.CharField(max_length=55)),
                ('github_handle', models.CharField(max_length=55)),
                ('capstone_mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.nssuser')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='ProposalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_url', models.CharField(max_length=256)),
                ('nss_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='studentprojects', to='LearningAPI.nssuser')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='studentprojects', to='LearningAPI.project')),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.course')),
                ('nss_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.nssuser')),
                ('proposal_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.proposalstatus')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectiveTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectivetags', to='LearningAPI.learningobjective')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectivetags', to='LearningAPI.tag')),
            ],
        ),
        migrations.CreateModel(
            name='NssUserCohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.cohort')),
                ('nss_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.nssuser')),
            ],
        ),
        migrations.CreateModel(
            name='LightningTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lightningtags', to='LearningAPI.lightningexercise')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lightningtags', to='LearningAPI.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ChapterNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markdown_text', models.TextField()),
                ('public', models.BooleanField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningAPI.bookchapter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningAPI.nssuser')),
            ],
        ),
        migrations.AddField(
            model_name='bookchapter',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='LearningAPI.coursebook'),
        ),
        migrations.AddField(
            model_name='bookchapter',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='LearningAPI.project'),
        ),
    ]
