from django.db import models

# Create your models here.

class Fitsname(models.Model):
    # dtnsanam, reference
    id = models.CharField(max_length=80, primary_key=True)
    
    # dtacqnam, full path to original filename
    source = models.CharField(max_length=256, null=True)
    
