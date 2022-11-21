# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class Actor(models.Model):
#     # Field name made lowercase.
#     id = models.AutoField(db_column='Id', primary_key=True)
#     # Field name made lowercase.
#     updated_on = models.DateTimeField(
#         db_column='Updated_on', blank=True, null=True)
#     # Field name made lowercase.
#     created_on = models.DateTimeField(
#         db_column='Created_on', blank=True, null=True)
#     is_deleted = models.IntegerField(blank=True, null=True)
#     # Field name made lowercase.
#     firstname = models.CharField(
#         db_column='Firstname', max_length=50, blank=True, null=True)
#     # Field name made lowercase.
#     lastname = models.CharField(
#         db_column='Lastname', max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Actor'


# class Agecategory(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     certification = models.CharField(db_column='Certification', max_length=20)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AgeCategory'


# class Booking(models.Model):
#     # Field name made lowercase.
#     id = models.AutoField(db_column='Id', primary_key=True)
#     # Field name made lowercase.
#     numberoftickets = models.IntegerField(
#         db_column='NumberOfTickets', blank=True, null=True)
#     # Field name made lowercase.
#     totalcost = models.IntegerField(
#         db_column='TotalCost', blank=True, null=True)
#     # Field name made lowercase.
#     showid = models.ForeignKey(
#         'Shows', models.DO_NOTHING, db_column='ShowId', blank=True, null=True)
#     # Field name made lowercase.
#     paymentid = models.ForeignKey(
#         'Payment', models.DO_NOTHING, db_column='PaymentId', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Booking'


# class City(models.Model):
#     # Field name made lowercase.
#     id = models.AutoField(db_column='Id', primary_key=True)
#     city_name = models.CharField(max_length=20)
#     # Field name made lowercase.
#     pincode = models.IntegerField(db_column='Pincode', blank=True, null=True)
#     # Field name made lowercase.
#     stateid = models.ForeignKey(
#         'State', models.DO_NOTHING, db_column='StateId', blank=True, null=True)
#     # Field name made lowercase.
#     countryid = models.ForeignKey(
#         'Country', models.DO_NOTHING, db_column='CountryId', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'City'


# class Country(models.Model):
#     # Field name made lowercase.
#     id = models.AutoField(db_column='Id', primary_key=True)
#     name = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Country'


# class Coupon(models.Model):
#     # Field name made lowercase.
#     id = models.AutoField(db_column='Id', primary_key=True)
#     name = models.CharField(max_length=25, blank=True, null=True)
#     discount = models.CharField(max_length=255, blank=True, null=True)
#     # Field name made lowercase.
#     validtill = models.DateTimeField(
#         db_column='validTill', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Coupon'


# class Movieactormap(models.Model):
#     # Field name made lowercase.
#     id = models.AutoField(db_column='Id', primary_key=True)
#     # Field name made lowercase.
#     movieid = models.ForeignKey(
#         'Movies', models.DO_NOTHING, db_column='MovieId', blank=True, null=True)
#     # Field name made lowercase.
#     actorid = models.ForeignKey(
#         Actor, models.DO_NOTHING, db_column='ActorId', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'MovieActorMap'


# class Moviecertificationmap(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     movieid = models.ForeignKey('Movies', models.DO_NOTHING, db_column='MovieId', blank=True, null=True)  # Field name made lowercase.
#     certificationid = models.ForeignKey(Agecategory, models.DO_NOTHING, db_column='CertificationId', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MovieCertificationMap'


# class Moviedimension(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     dimension = models.CharField(db_column='Dimension', max_length=20)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MovieDimension'


# class Moviedimensionmap(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     movieid = models.ForeignKey('Movies', models.DO_NOTHING, db_column='MovieId', blank=True, null=True)  # Field name made lowercase.
#     moviedimensionid = models.ForeignKey(Moviedimension, models.DO_NOTHING, db_column='MovieDimensionId', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MovieDimensionMap'


# # class Moviegenre(models.Model):
# #     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
# #     genre_name = models.CharField(db_column='Genre_name', max_length=20)  # Field name made lowercase.

# #     class Meta:
# #         managed = False
#         db_table = 'MovieGenre'


# class Moviegenremap(models.Model):
#     id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     movieid = models.ForeignKey('Movies', models.DO_NOTHING, db_column='MovieId', blank=True, null=True)  # Field name made lowercase.
#     moviegenreid = models.ForeignKey(Moviegenre, models.DO_NOTHING, db_column='MovieGenreId', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MovieGenreMap'


# class Movielanguagemap(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     movieid = models.ForeignKey('Movies', models.DO_NOTHING, db_column='MovieId', blank=True, null=True)  # Field name made lowercase.
#     movielanguageid = models.ForeignKey('Movielanguages', models.DO_NOTHING, db_column='MovieLanguageId', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MovieLanguageMap'


# class Movielanguages(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     language = models.CharField(db_column='Language', max_length=20)  # Field name made lowercase.
#     updated_on = models.DateTimeField(db_column='Updated_on', blank=True, null=True)  # Field name made lowercase.
#     created_on = models.DateTimeField(db_column='Created_on', blank=True, null=True)  # Field name made lowercase.
#     is_deleted = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'MovieLanguages'


# class Movies(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     movies_name = models.CharField(db_column='Movies_name', max_length=100)  # Field name made lowercase.
#     about = models.CharField(db_column='About', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     release_date = models.DateTimeField(db_column='Release_date', blank=True, null=True)  # Field name made lowercase.
#     duration = models.BigIntegerField(db_column='Duration')  # Field name made lowercase.
#     created_on = models.DateTimeField(db_column='Created_on', blank=True, null=True)  # Field name made lowercase.
#     updated_on = models.DateTimeField(db_column='Updated_on', blank=True, null=True)  # Field name made lowercase.
#     is_deleted = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Movies'


# class Multiplex(models.Model):
#     # Field name made lowercase.
#     id = models.AutoField(db_column='Id', primary_key=True)
#     # Field name made lowercase.
#     multiplex_name = models.CharField(
#         db_column='Multiplex_name', max_length=100)
#     # Field name made lowercase.
#     updated_on = models.DateTimeField(
#         db_column='Updated_on', blank=True, null=True)
#     # Field name made lowercase.
#     created_on = models.DateTimeField(
#         db_column='Created_on', blank=True, null=True)
#     is_deleted = models.IntegerField(blank=True, null=True)
#     # Field name made lowercase.
#     cityid = models.ForeignKey(
#         City, models.DO_NOTHING, db_column='CityId', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Multiplex'


# class Payment(models.Model):
#     # Field name made lowercase.
#     id = models.AutoField(db_column='Id', primary_key=True)
#     transaction_type = models.CharField(max_length=50, blank=True, null=True)
#     transaction_id = models.CharField(max_length=50, blank=True, null=True)
#     transaction_date = models.DateTimeField(blank=True, null=True)
#     payment_status = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Payment'


# class Reviews(models.Model):
#     # Field name made lowercase.
#     id = models.AutoField(db_column='Id', primary_key=True)
#     # Field name made lowercase.
#     movieid = models.ForeignKey(
#         Movies, models.DO_NOTHING, db_column='MovieId', blank=True, null=True)
#     # Field name made lowercase.
#     review_comment = models.CharField(
#         db_column='Review_comment', max_length=255)
#     # Field name made lowercase.
#     ratings_date = models.DateField(
#         db_column='Ratings_date', blank=True, null=True)
#     # Field name made lowercase.
#     isuser = models.IntegerField(db_column='isUser', blank=True, null=True)
#     # Field name made lowercase.
#     userid = models.ForeignKey(
#         'User', models.DO_NOTHING, db_column='UserId', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Reviews'


# class Screen(models.Model):
#     # Field name made lowercase.
#     id = models.IntegerField(db_column='Id', primary_key=True)
#     hall_name = models.CharField(max_length=100)
#     # Field name made lowercase.
#     number_of_seats = models.IntegerField(
#         db_column='Number_of_seats', blank=True, null=True)
#     # Field name made lowercase.
#     ishousefull = models.IntegerField(
#         db_column='isHouseFull', blank=True, null=True)
#     # Field name made lowercase.
#     multiplexid = models.ForeignKey(
#         Multiplex, models.DO_NOTHING, db_column='MultiplexId', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Screen'


# class Seattype(models.Model):
#     # Field name made lowercase.
#     id = models.IntegerField(db_column='Id', primary_key=True)
#     # Field name made lowercase.
#     name = models.CharField(
#         db_column='Name', max_length=25, blank=True, null=True)
#     # Field name made lowercase.
#     numofseats = models.IntegerField(
#         db_column='NumOfSeats', blank=True, null=True)
#     # Field name made lowercase.
#     price = models.IntegerField(db_column='Price', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'SeatType'


# class Seats(models.Model):
#     # Field name made lowercase.
#     id = models.IntegerField(db_column='Id', primary_key=True)
#     # Field name made lowercase.
#     created_on = models.DateTimeField(
#         db_column='Created_on', blank=True, null=True)
#     # Field name made lowercase.
#     updated_on = models.DateTimeField(
#         db_column='Updated_on', blank=True, null=True)
#     is_deleted = models.IntegerField(blank=True, null=True)
#     # Field name made lowercase.
#     screenid = models.ForeignKey(
#         Screen, models.DO_NOTHING, db_column='ScreenId', blank=True, null=True)
#     # Field name made lowercase.
#     seattypeid = models.ForeignKey(
#         Seattype, models.DO_NOTHING, db_column='SeatTypeId', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Seats'


# class Showtiming(models.Model):
#     # Field name made lowercase.
#     id = models.IntegerField(db_column='Id', primary_key=True)
#     date = models.DateTimeField(blank=True, null=True)
#     starttime = models.DateTimeField(blank=True, null=True)
#     endtime = models.DateTimeField(blank=True, null=True)
#     # Field name made lowercase.
#     created_on = models.DateTimeField(
#         db_column='Created_on', blank=True, null=True)
#     # Field name made lowercase.
#     updated_on = models.DateTimeField(
#         db_column='Updated_on', blank=True, null=True)
#     is_deleted = models.IntegerField(blank=True, null=True)
#     # Field name made lowercase.
#     movieid = models.ForeignKey(
#         Movies, models.DO_NOTHING, db_column='MovieId', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'ShowTiming'


# class Shows(models.Model):
#     # Field name made lowercase.
#     id = models.IntegerField(db_column='Id', primary_key=True)
#     # Field name made lowercase.
#     showtimeid = models.ForeignKey(
#         Showtiming, models.DO_NOTHING, db_column='ShowTimeid', blank=True, null=True)
#     # Field name made lowercase.
#     screenid = models.ForeignKey(
#         Screen, models.DO_NOTHING, db_column='ScreenId', blank=True, null=True)
#     # Field name made lowercase.
#     seatid = models.ForeignKey(
#         Seats, models.DO_NOTHING, db_column='SeatId', blank=True, null=True)
#     # Field name made lowercase.
#     multiplexid = models.ForeignKey(
#         Multiplex, models.DO_NOTHING, db_column='MultiplexId', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Shows'


# class State(models.Model):
#     # Field name made lowercase.
#     id = models.AutoField(db_column='Id', primary_key=True)
#     name = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'State'


# class Ticket(models.Model):
#     # Field name made lowercase.
#     id = models.AutoField(db_column='Id', primary_key=True)
#     # Field name made lowercase.
#     seatid = models.ForeignKey(
#         Seats, models.DO_NOTHING, db_column='SeatId', blank=True, null=True)
#     # Field name made lowercase.
#     bookingid = models.ForeignKey(
#         Booking, models.DO_NOTHING, db_column='BookingId', blank=True, null=True)
#     # Field name made lowercase.
#     couponid = models.ForeignKey(
#         Coupon, models.DO_NOTHING, db_column='CouponId', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Ticket'


class User(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)
    # Field name made lowercase.
    updated_on = models.DateTimeField(
        db_column='Updated_on', blank=True, null=True)
    # Field name made lowercase.
    created_on = models.DateTimeField(
        db_column='Created_on', blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    firstname = models.CharField(
        db_column='Firstname', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    lastname = models.CharField(
        db_column='Lastname', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    phonenumber = models.IntegerField(
        db_column='PhoneNumber', blank=True, null=True)
    # Field name made lowercase.
    password = models.CharField(
        db_column='Password', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# # class AuthPermission(models.Model):
# #     name = models.CharField(max_length=255)
# #     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
# #     codename = models.CharField(max_length=100)

# #     class Meta:
# #         managed = False
# #         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'
