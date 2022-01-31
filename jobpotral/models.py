from django.db import models

# Create your models here.
class Job(models.Model):
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    salary = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.position

