from django.db import models


class Payment(models.Model):

    id = models.AutoField(db_column='Id', primary_key=True)
    transaction_type = models.CharField(max_length=50, blank=True, null=True)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Payment'


class Coupon(models.Model):

    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    discount = models.CharField(max_length=255, blank=True, null=True)

    validtill = models.DateTimeField(
        db_column='validTill', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Coupon'
