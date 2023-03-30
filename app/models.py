from django.db import models

# Create your models here.

class workers(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    worker_id=models.IntegerField()

    def __str__(self):

        return self.firstname