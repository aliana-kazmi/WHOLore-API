# Generated by Django 4.0.6 on 2022-10-03 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('gender', models.CharField(default='male', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Companion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('nickname', models.CharField(max_length=65)),
                ('image', models.ImageField(upload_to='images/Companions')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('season_no', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('start_yr', models.DateField()),
                ('end_yr', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('Episode_type', models.CharField(choices=[('Special', 'Special'), ('Regular', 'Regular')], default='Regular', max_length=7)),
                ('synopsis', models.TextField()),
                ('original_air_date', models.DateField()),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.season')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('number', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('fav_clothing', models.TextField()),
                ('image', models.ImageField(upload_to='images/Doctor')),
                ('companions', models.ManyToManyField(to='characters.companion')),
                ('featured_in', models.ManyToManyField(to='characters.season')),
                ('played_by', models.ManyToManyField(to='characters.actor')),
            ],
        ),
        migrations.AddField(
            model_name='companion',
            name='featured_in',
            field=models.ManyToManyField(to='characters.episode'),
        ),
        migrations.AddField(
            model_name='companion',
            name='played_by',
            field=models.ManyToManyField(to='characters.actor'),
        ),
        migrations.CreateModel(
            name='Ally',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('featured_in', models.ManyToManyField(to='characters.episode')),
                ('played_by', models.ManyToManyField(to='characters.actor')),
            ],
        ),
    ]
