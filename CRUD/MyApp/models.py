from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    salary = models.IntegerField()
    designation = models.CharField(max_length=20)
    city = models.CharField(max_length=20, default=None, blank=True, null=True)
    state = models.CharField(
        max_length=20, default=None, blank=True, null=True)
    country = models.CharField(
        max_length=20, default=None, blank=True, null=True)

    def __str__(self):
        return str(self.eid)+" is Employee ID , Name = "+self.name
