from django.db import models


class Country(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Country'
        verbose_name_plural = 'Countries'


class State(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'State'
        verbose_name_plural = 'States'


class City(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    city_name = models.CharField(max_length=20)
    pincode = models.IntegerField(
        db_column='Pincode', blank=True, null=True)
    state = models.ForeignKey(
        State, models.DO_NOTHING, db_column='StateId', blank=True, null=True,  related_name='state')  # change
    country = models.ForeignKey(
        Country, models.DO_NOTHING, db_column='CountryId', blank=True, null=True, related_name="country")

    def __str__(self):
        return self.city_name

    class Meta:
        managed = True
        db_table = 'City'
        verbose_name_plural = 'Cities'


class Multiplex(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    multiplex_name = models.CharField(
        db_column='Multiplex_name', max_length=100)
    updated_on = models.DateTimeField(
        db_column='Updated_on', blank=True, null=True)
    created_on = models.DateTimeField(
        db_column='Created_on', blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    cityid = models.ForeignKey(
        City, on_delete=models.CASCADE, db_column='CityId', blank=True, null=True)

    def __str__(self):
        return self.multiplex_name

    class Meta:
        managed = True
        db_table = 'Multiplex'
        verbose_name_plural = 'Multiplexes'


class Screen(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    hall_name = models.CharField(max_length=100)
    number_of_seats = models.IntegerField(
        db_column='Number_of_seats', blank=True, null=True)
    ishousefull = models.IntegerField(
        db_column='isHouseFull', blank=True, null=True)
    multiplexid = models.ForeignKey(
        'Multiplex', models.DO_NOTHING, db_column='MultiplexId', blank=True, null=True)

    def __str__(self):
        return self.hall_name

    class Meta:
        managed = True
        db_table = 'Screen'
        verbose_name_plural = 'Screens'
