from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class ModelPatient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    picture = models.ImageField(upload_to='PatientPics')
    doctor = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    
class ModelVisit(models.Model):
    date      = models.DateField(default=timezone.now)
    patient   = models.ForeignKey(to=ModelPatient, on_delete=models.CASCADE)
    disease   = models.CharField(max_length=250)
    advice    = models.TextField()
    medicine  = models.CharField(max_length=250)
    tests     = models.CharField(max_length=250)
    follow_up = models.DateField(default=datetime.datetime.now() + datetime.timedelta(days=30)) 
    charges   = models.IntegerField() # will be input dynamically in the view
    doctor    = models.ForeignKey(to=User, on_delete=models.CASCADE)
    report    = models.FileField(default='report.txt')
    report_ready = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.patient) +'\'' + ' visit'
