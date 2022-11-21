# Generated by Django 4.1.3 on 2022-11-17 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_moviecertificationmap_moviedimensionmap_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('updated_on', models.DateTimeField(blank=True, db_column='Updated_on', null=True)),
                ('created_on', models.DateTimeField(blank=True, db_column='Created_on', null=True)),
                ('is_deleted', models.IntegerField(blank=True, null=True)),
                ('firstname', models.CharField(blank=True, db_column='Firstname', max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, db_column='Lastname', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Actor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movieactormap',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Movieactormap',
                'db_table': 'MovieActorMap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('review_comment', models.CharField(db_column='Review_comment', max_length=255)),
                ('ratings_date', models.DateField(blank=True, db_column='Ratings_date', null=True)),
                ('isuser', models.BooleanField(blank=True, db_column='isUser', default=False, null=True)),
            ],
            options={
                'verbose_name_plural': 'Reviews',
                'db_table': 'Reviews',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='moviecertificationmap',
            options={'managed': False, 'verbose_name_plural': 'Moviecertificationmap'},
        ),
        migrations.AlterModelOptions(
            name='moviedimensionmap',
            options={'managed': False, 'verbose_name_plural': 'Moviedimensionmap'},
        ),
        migrations.AlterModelOptions(
            name='moviegenremap',
            options={'managed': False, 'verbose_name_plural': 'Moviegenremap'},
        ),
        migrations.AlterField(
            model_name='moviedimension',
            name='id',
            field=models.AutoField(db_column='Id', primary_key=True, serialize=False),
        ),
    ]
