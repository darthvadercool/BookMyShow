from django.db import models

from multiplex.models import Screen, Multiplex
from movies.models import Movies
from payments.models import Coupon, Payment


class Seattype(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    numofseats = models.IntegerField(
        db_column='NumOfSeats', blank=True, null=True)
    # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'SeatType'


class Seats(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    created_on = models.DateTimeField(
        db_column='Created_on', blank=True, null=True)
    # Field name made lowercase.
    updated_on = models.DateTimeField(
        db_column='Updated_on', blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    screenid = models.ForeignKey(
        Screen, models.DO_NOTHING, db_column='ScreenId', blank=True, null=True)
    # Field name made lowercase.
    seattypeid = models.ForeignKey(
        Seattype, models.DO_NOTHING, db_column='SeatTypeId', blank=True, null=True)

    def __str__(self):
        return self.screenid.hall_name

    class Meta:
        managed = True
        db_table = 'Seats'
        verbose_name_plural = 'Seats'


class Showtiming(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    # Field name made lowercase.
    created_on = models.DateTimeField(
        db_column='Created_on', blank=True, null=True)
    # Field name made lowercase.
    updated_on = models.DateTimeField(
        db_column='Updated_on', blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    movieid = models.ForeignKey(
        Movies, models.DO_NOTHING, db_column='MovieId', blank=True, null=True)

    def __str__(self):
        return self.date

    class Meta:
        managed = True
        db_table = 'ShowTiming'


class Shows(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    showtimeid = models.ForeignKey(
        Showtiming, models.DO_NOTHING, db_column='ShowTimeid', blank=True, null=True)
    # Field name made lowercase.
    screenid = models.ForeignKey(
        Screen, models.DO_NOTHING, db_column='ScreenId', blank=True, null=True)
    # Field name made lowercase.
    seatid = models.ForeignKey(
        Seats, models.DO_NOTHING, db_column='SeatId', blank=True, null=True)
    # Field name made lowercase.
    multiplexid = models.ForeignKey(
        Multiplex, models.DO_NOTHING, db_column='MultiplexId', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Shows'
        verbose_name_plural = 'Shows'


class Booking(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    numberoftickets = models.IntegerField(
        db_column='NumberOfTickets', blank=True, null=True)
    # Field name made lowercase.
    totalcost = models.IntegerField(
        db_column='TotalCost', blank=True, null=True)
    # Field name made lowercase.
    showid = models.ForeignKey(
        'Shows', models.DO_NOTHING, db_column='ShowId', blank=True, null=True)
    # Field name made lowercase.
    paymentid = models.ForeignKey(
        Payment, models.DO_NOTHING, db_column='PaymentId', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Booking'


class Ticket(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    seatid = models.ForeignKey(
        Seats, models.DO_NOTHING, db_column='SeatId', blank=True, null=True)
    # Field name made lowercase.
    bookingid = models.ForeignKey(
        Booking, models.DO_NOTHING, db_column='BookingId', blank=True, null=True)
    # Field name made lowercase.
    couponid = models.ForeignKey(
        Coupon, models.DO_NOTHING, db_column='CouponId', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Ticket'
