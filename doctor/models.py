from django.db import models
from django.contrib.auth.models import User

# model for Doctor's profile
class DoctorProfile(models.Model):
    name           = models.OneToOneField(to=User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100, default='ENT')
    fees           = models.IntegerField(default=1000)

    def __str__(self) -> str:
        return super().__str__() + str(self.name)
