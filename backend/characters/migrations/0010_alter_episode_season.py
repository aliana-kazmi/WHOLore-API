# Generated by Django 4.0.6 on 2022-10-03 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_episode_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.season'),
        ),
    ]
