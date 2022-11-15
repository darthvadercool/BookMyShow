# Generated by Django 4.1.3 on 2022-11-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_moviegenre_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moviecertificationmap',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'MovieCertificationMap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Moviedimensionmap',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'MovieDimensionMap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Moviegenremap',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'MovieGenreMap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movielanguagemap',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'MovieLanguageMap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Agecategory',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('certification', models.CharField(db_column='Certification', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Certification',
                'db_table': 'AgeCategory',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='moviedimension',
            name='id',
            field=models.BooleanField(db_column='Id', primary_key=True, serialize=False),
        ),
    ]
