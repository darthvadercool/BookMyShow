# Generated by Django 4.1.3 on 2022-11-17 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='seats',
            options={'managed': True, 'verbose_name_plural': 'Seats'},
        ),
        migrations.AlterModelOptions(
            name='seattype',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='shows',
            options={'managed': True, 'verbose_name_plural': 'Shows'},
        ),
        migrations.AlterModelOptions(
            name='showtiming',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'managed': True},
        ),
    ]