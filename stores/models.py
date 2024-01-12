from django.db import models


class StoreType(models.Model):
    name = models.CharField(max_length=20)


class Store(models.Model):
    store_type = models.ForeignKey(StoreType, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    minimum_purchase = models.PositiveIntegerField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

class Schedule(models.Model):
    days = (
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wendesday", "Wendesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday")
    )
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=days)
    start_time = models.TimeField()
    end_time = models.TimeField()
