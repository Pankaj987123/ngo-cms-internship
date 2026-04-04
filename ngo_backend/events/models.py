from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/', null=True, blank=True)

    def __str__(self):
        return self.title


class Donation(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name