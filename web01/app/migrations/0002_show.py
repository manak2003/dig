# Generated by Django 4.1.1 on 2022-09-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('year', models.IntegerField()),
                ('season_count', models.IntegerField()),
                ('rating', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
