# Generated by Django 4.1.3 on 2022-11-11 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movies_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='is_deleted',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]