# Generated by Django 2.2.2 on 2019-06-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
        migrations.AddField(
            model_name='project',
            name='app_link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='backend_github_link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='blog_link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='frontend_github_link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]