from django.db import models

# Create your models here.


class Job(models.Model):
    company = models.CharField(max_length=250)
    join_date = models.DateField()
    end_date = models.DateField()
    position = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='image/', default='')

    def __str__(self):
        return self.company
