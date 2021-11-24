# Generated by Django 3.2.8 on 2021-11-24 16:27

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
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('is_qa', models.BooleanField()),
                ('is_project', models.BooleanField()),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Capstone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal_url', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='LearningAPI.book')),
            ],
        ),
        migrations.CreateModel(
            name='ChapterNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markdown_text', models.TextField()),
                ('public', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningAPI.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True)),
                ('slack_channel', models.CharField(max_length=55, unique=True)),
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
            name='LearningObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swbat', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LearningRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=55)),
                ('obtained_from', models.CharField(choices=[('ONEON', 'Student 1 on 1'), ('SCORE', 'Assessment score'), ('CLASS', 'Github Classroom')], default='ONEON', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='LearningWeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=127)),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LightningExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NssUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_handle', models.CharField(blank=True, max_length=55, null=True)),
                ('github_handle', models.CharField(blank=True, max_length=55, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('implementation_url', models.CharField(max_length=256)),
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
            name='TaxonomyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_url', models.CharField(max_length=256)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='students', to='LearningAPI.project')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='LearningAPI.nssuser')),
            ],
        ),
        migrations.CreateModel(
            name='StudentMentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capstone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningAPI.capstone')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='LearningAPI.nssuser')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentors', to='LearningAPI.nssuser')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projecttags', to='LearningAPI.project')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projecttags', to='LearningAPI.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningAPI.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningAPI.nssuser')),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portion', models.CharField(choices=[('CLI', 'Client side'), ('SER', 'Server side')], default='CLI', max_length=3)),
                ('start_date', models.DateField()),
                ('message', models.TextField()),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ta_opportunities', to='LearningAPI.cohort')),
                ('senior_instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coaching_opportunities', to='LearningAPI.nssuser')),
            ],
        ),
        migrations.CreateModel(
            name='OneOnOneNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
                ('session_date', models.DateField(auto_now=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coach_notes', to='LearningAPI.nssuser')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='LearningAPI.nssuser')),
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
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='members', to='LearningAPI.cohort')),
                ('nss_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cohorts', to='LearningAPI.nssuser')),
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
            name='LearningRecordWeights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weights', to='LearningAPI.learningrecord')),
                ('weight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='LearningAPI.learningweight')),
            ],
        ),
        migrations.AddField(
            model_name='learningrecord',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningAPI.nssuser'),
        ),
        migrations.AddField(
            model_name='learningobjective',
            name='bloom_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectives', to='LearningAPI.taxonomylevel'),
        ),
        migrations.CreateModel(
            name='FavoriteNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voters', to='LearningAPI.chapternote')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_notes', to='LearningAPI.nssuser')),
            ],
        ),
        migrations.CreateModel(
            name='ChapterObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectives', to='LearningAPI.chapter')),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='LearningAPI.learningobjective')),
            ],
        ),
        migrations.AddField(
            model_name='chapternote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningAPI.nssuser'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='LearningAPI.project'),
        ),
        migrations.CreateModel(
            name='CapstoneTimeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('capstone', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.capstone')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.proposalstatus')),
            ],
        ),
        migrations.AddField(
            model_name='capstone',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.course'),
        ),
        migrations.AddField(
            model_name='capstone',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='capstones', to='LearningAPI.nssuser'),
        ),
        migrations.AddField(
            model_name='book',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='LearningAPI.course'),
        ),
        migrations.CreateModel(
            name='AssessmentObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectives', to='LearningAPI.assessment')),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='LearningAPI.learningobjective')),
            ],
        ),
    ]
