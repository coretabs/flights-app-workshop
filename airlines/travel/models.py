from django.db import models
import time
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError


class Plane(models.Model):
    name           = models.CharField(max_length=50,unique=True)
    num_of_seats   = models.IntegerField()
    available      = models.BooleanField(default=True)

    def __str__(self):                           
	    return self.name   


def present_or_future_date(value):
    if value < timezone.now():
        raise ValidationError("The date cannot be in the past!")
    return value


class Flight(models.Model):
    plane_name     = models.ForeignKey(Plane,on_delete=models.CASCADE)
    from_city      = models.CharField(max_length=50)
    to_city        = models.CharField(max_length=50)
    from_time      = models.DateTimeField(validators=[present_or_future_date])
    to_time        = models.TimeField()


    def __str__(self):
        return '{} - {}'.format(self.from_city,self.to_city)


class Passenger(models.Model):
    full_name      = models.CharField(max_length=100)
    age            = models.IntegerField()
    GENDER_CHOICES = [('M','Male'),('F','Female')]
    gender         = models.CharField(choices=GENDER_CHOICES,max_length=1)


    def __str__(self):
        return self.full_name

class Ticket(models.Model):
    passenger      = models.ForeignKey(Passenger,on_delete=models.CASCADE)
    flight         = models.ForeignKey(Flight,on_delete=models.CASCADE)


    def __str__(self):
        return '{}  --> ({})'.format(self.passenger,self.flight)


class User_Info(models.Model):
    name           = models.CharField(max_length=50)
    email          = models.EmailField()


    def __str__(self):
        return self.name