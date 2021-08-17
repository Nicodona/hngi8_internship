from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=252)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=12)
    date_of_birth = models.CharField(max_length=20)
    description = models.TextField
    job = models.CharField(max_length=512)
    degree = models.CharField(max_length=256)
    dod = models.CharField(max_length=20)
    experience = models.CharField(max_length=512)
    YoE = models.CharField(max_length=20)
    job_desc = models.TextField


    def __str__(self):
        return self.name
