from django.db import models


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
