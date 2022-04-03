# Generated by Django 4.0 on 2022-03-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_delete_newlatest'),
    ]

    operations = [
        migrations.CreateModel(
            name='newlatest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('directer', models.CharField(max_length=50)),
                ('long', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=500)),
                ('sdesc', models.CharField(max_length=500)),
                ('ldesc', models.CharField(max_length=5000)),
                ('svedio', models.CharField(max_length=5000)),
                ('rating', models.FloatField()),
                ('image1', models.CharField(max_length=500)),
                ('image2', models.CharField(max_length=500)),
                ('image3', models.CharField(max_length=500)),
                ('image4', models.CharField(max_length=500)),
            ],
        ),
    ]
