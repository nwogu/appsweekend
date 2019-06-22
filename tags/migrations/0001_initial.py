# Generated by Django 2.2.2 on 2019-06-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('colour', models.CharField(blank=True, max_length=255)),
                ('projects', models.ManyToManyField(related_name='tags', to='projects.Project')),
            ],
        ),
    ]