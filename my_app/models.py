from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    email = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

