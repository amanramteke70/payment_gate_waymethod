from django.db import models

# Create your models here.
class Details(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postcode = models.IntegerField()
    country = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

