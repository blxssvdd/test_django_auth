from django.db import models

# Create your models here.


class Planner(models.Model):
    user = models.ForeignKey("UserManager.MySuperUser", on_delete=models.CASCADE)
    contact = models.ForeignKey("PhoneBook.Contact", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    title = models.CharField(max_length=500, null=True, blank=True, default=None)
    address = models.CharField(max_length=200, null=True, blank=True, default="Online")
    link = models.URLField(max_length=300, null=True, blank=True, default=None)
    accepted = models.BooleanField(default=None, null=True, blank=True)
