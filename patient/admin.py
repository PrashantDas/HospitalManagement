from django.contrib import admin
from .models import ModelPatient, ModelVisit
admin.site.register([ModelPatient, ModelVisit])

