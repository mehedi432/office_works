from django.db import models


# Create your models here.
class Purchase(models.Model):
    title = models.CharField(max_length=21)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    @property
    def total(self):
        return self.price * self.quantity

    def __str__(self):
        return self.title
