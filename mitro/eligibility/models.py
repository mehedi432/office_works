from django.db import models

# Create your models here.
class Eligibility(models.Model):
    date = models.CharField(max_length=21)
    name = models.CharField(max_length=55)
    mobile_number = models.CharField(max_length=55)
    address = models.CharField(max_length=55)
    age = models.PositiveIntegerField()
    comments = models.CharField(max_length=144)
    area = models.CharField(max_length=55)


    def __str__(self):
        return self.name

    def get_success_url(self):
        return reversed("admin/")


