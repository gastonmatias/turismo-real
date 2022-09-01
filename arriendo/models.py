from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    rut = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class CustomerAccount(models.Model):
    user_id = models.ForeignKey(Customer, on_delete=models.PROTECT) #no permite borrar un Customer si tiene 1 cuenta
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    regular_customer = models.BooleanField()
