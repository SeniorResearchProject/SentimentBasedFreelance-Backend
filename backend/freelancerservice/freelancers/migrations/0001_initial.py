# Generated by Django 5.0.4 on 2024-06-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('experience', models.IntegerField(blank=True, help_text='Experience in years', null=True)),
                ('user_id', models.IntegerField()),
                ('profession', models.CharField(blank=True, max_length=255, null=True)),
                ('education_level', models.CharField(blank=True, max_length=255, null=True)),
                ('available', models.BooleanField(default=True, help_text='Availability for new projects')),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('cv', models.FileField(blank=True, null=True, upload_to='files/')),
                ('Nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('salary_range', models.CharField(blank=True, max_length=255, null=True)),
                ('employeeType', models.CharField(blank=True, choices=[('FULL-TIME', 'FULL-TIME'), ('PART-TIME', 'PART-TIME')], max_length=255, null=True)),
                ('skill', models.TextField(blank=True, null=True)),
                ('rate', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freelancer', models.IntegerField()),
                ('freelancer_name', models.CharField(max_length=255)),
                ('job_id', models.IntegerField()),
                ('job_title', models.CharField(max_length=255)),
                ('dateApplied', models.DateTimeField(auto_now=True)),
                ('milestone', models.PositiveIntegerField(default=2)),
                ('cv', models.FileField(blank=True, null=True, upload_to='files/')),
                ('cover_letter', models.TextField()),
                ('application_status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TaskSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freelancer', models.IntegerField()),
                ('freelancer_name', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('job_applied', models.IntegerField()),
                ('job_id', models.IntegerField()),
                ('milestone', models.PositiveIntegerField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='submissions/%Y/%m/%d/')),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
