# Generated by Django 4.0.6 on 2022-10-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_actor_episode'),
        ('characters', '0037_alter_alienrace_featured_in_and_more'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                name='Actor',
                ),
            ],
            database_operations=[],
        ),
        
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name='companion',
                    name='played_by',
                    field=models.ManyToManyField(to='api.actor'),
                ),
            ],
            database_operations=[],
        ),
        
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name='doctor',
                    name='played_by',
                    field=models.ManyToManyField(to='api.actor'),
                ),
            ],
            database_operations=[],
        ),
        
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name='villain',
                    name='played_by',
                    field=models.ManyToManyField(to='api.actor'),
                ),
            ],
            database_operations=[],
        ),
        
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Episode',
                ),
            ],
            database_operations=[],
        ),
        
    ]
