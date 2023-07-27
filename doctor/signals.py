from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DoctorProfile

# triggers creation of a profile for a new user which is added
@receiver(post_save, sender=User)
def make_a_profile_automatically(sender, instance, created, **kwargs):
    if created:
        DoctorProfile.objects.create(name=instance)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.doctorprofile.save()