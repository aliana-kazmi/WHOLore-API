# Generated by Django 4.0.6 on 2022-10-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0026_alter_alienrace_featured_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='alienrace',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]