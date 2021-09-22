from django.db import models

# Create your models here.


class Product(models.Model):
    index = models.AutoField(db_column='index',primary_key=True)
    P_id = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    ratingscore = models.FloatField(db_column='ratingScore', blank=True, null=True)  # Field name made lowercase.
    totalcount = models.FloatField(db_column='totalCount', blank=True, null=True)  
# Field name made lowercase.
    categoryhierarchy = models.TextField(db_column='categoryHierarchy', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.BigIntegerField(db_column='categoryId', blank=True, null=True)  # Field name made lowercase.
    categoryname = models.TextField(db_column='categoryName', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(blank=True, null=True)
    sellingppice = models.FloatField(db_column='sellingpPice', blank=True, null=True)  # Field name made lowercase.
    originalprice = models.FloatField(db_column='originalPrice', blank=True, null=True)  # Field name made lowercase.
    discountedprice = models.FloatField(db_column='discountedPrice', blank=True, null=True)  # Field name made lowercase.
    freecargo = models.BooleanField(db_column='freeCargo', blank=True, null=True)  
# Field name made lowercase.
    addedtime = models.DateTimeField(db_column='addedTime', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.P_id)

    class Meta:
        managed = False
        db_table = 'JsonProduct'