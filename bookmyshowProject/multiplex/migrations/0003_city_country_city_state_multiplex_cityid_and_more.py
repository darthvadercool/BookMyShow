# Generated by Django 4.1.3 on 2022-11-21 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0002_alter_city_options_alter_country_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, db_column='CountryId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='country', to='multiplex.country'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, db_column='StateId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cities', to='multiplex.state'),
        ),
        migrations.AddField(
            model_name='multiplex',
            name='cityid',
            field=models.ForeignKey(blank=True, db_column='CityId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='multiplex.city'),
        ),
        migrations.AddField(
            model_name='screen',
            name='multiplexid',
            field=models.ForeignKey(blank=True, db_column='MultiplexId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='multiplex.multiplex'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='id',
            field=models.AutoField(db_column='Id', primary_key=True, serialize=False),
        ),
    ]