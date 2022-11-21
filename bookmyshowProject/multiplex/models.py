from django.db import models


class State(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'State'
        verbose_name_plural = 'States'


class Country(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Country'
        verbose_name_plural = 'Countries'


class City(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    city_name = models.CharField(max_length=20)
    # Field name made lowercase.
    pincode = models.IntegerField(
        db_column='Pincode', blank=True, null=True)
    # Field name made lowercase.
    state = models.ForeignKey(
        'State', models.DO_NOTHING, db_column='StateId', blank=True, null=True,  related_name='cities')
    # Field name made lowercase.
    country = models.ForeignKey(
        'Country', models.DO_NOTHING, db_column='CountryId', blank=True, null=True, related_name="country")

    def __str__(self):
        return self.city_name

    class Meta:
        managed = True
        db_table = 'City'
        verbose_name_plural = 'Cities'


class Multiplex(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    multiplex_name = models.CharField(
        db_column='Multiplex_name', max_length=100)
    # Field name made lowercase.
    updated_on = models.DateTimeField(
        db_column='Updated_on', blank=True, null=True)
    # Field name made lowercase.
    created_on = models.DateTimeField(
        db_column='Created_on', blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    # Field name made lowercase.
    cityid = models.ForeignKey(
        City, models.DO_NOTHING, db_column='CityId', blank=True, null=True)

    def __str__(self):
        return self.multiplex_name

    class Meta:
        managed = True
        db_table = 'Multiplex'
        verbose_name_plural = 'Multiplexes'


class Screen(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    hall_name = models.CharField(max_length=100)
    # Field name made lowercase.
    number_of_seats = models.IntegerField(
        db_column='Number_of_seats', blank=True, null=True)
    # Field name made lowercase.
    ishousefull = models.IntegerField(
        db_column='isHouseFull', blank=True, null=True)
    # Field name made lowercase.
    multiplexid = models.ForeignKey(
        Multiplex, models.DO_NOTHING, db_column='MultiplexId', blank=True, null=True)

    def __str__(self):
        return self.hall_name

    class Meta:
        managed = True
        db_table = 'Screen'
        verbose_name_plural = 'Screens'
