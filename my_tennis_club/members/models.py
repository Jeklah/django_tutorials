from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    # This method is used to return the string representation of the object
    # This is a python magic method that is called when the object is printed
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
