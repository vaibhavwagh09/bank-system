from django.db import models


# Create your models here.

class Users(models.Model):
    account_number = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    balance = models.FloatField()

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = "Users"


class Transfer(models.Model):
    from_cust = models.CharField(max_length=120)
    to_cust = models.CharField(max_length=120)
    cust_amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.from_cust