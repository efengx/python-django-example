# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

class Vehicles(models.Model):
    load_id = models.TextField(blank=True, null=True)
    reference_id = models.CharField(max_length=255, blank=True, null=True)
    vehicle = models.TextField(blank=True, null=True)
    pickup = models.TextField(blank=True, null=True)
    delivery = models.TextField(blank=True, null=True)
    mileage = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    hour = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    posted = models.TextField(blank=True, null=True)
    ship = models.TextField(blank=True, null=True)
    scraped_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        # 该表不需要更新数据库
        managed = False
        db_table = 'vehicles'


class Trailer(models.Model):
    trailer = models.TextField(blank=True, null=True)
    capacity = models.TextField(blank=True, null=True)
    miles_per_gallon = models.TextField(blank=True, null=True)
    cost_per_gallon = models.TextField(blank=True, null=True)
    pick_up_state = models.TextField(blank=True, null=True)
    pick_up_city = models.TextField(blank=True, null=True)
    pick_up_radius = models.TextField(blank=True, null=True)
    delivery = models.TextField(blank=True, null=True)
    delivery_radius = models.TextField(blank=True, null=True)
    minimum_cost_per_mile = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    update_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    # owner = models.ForeignKey('auth.User', related_name='trailer', on_delete=models.CASCADE)
    # highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(Trailer, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'trailer'
        ordering = ('create_date',)
