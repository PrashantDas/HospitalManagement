from django.urls import path
from .views import (create_doctor,
                    view_doctor_profile,
                    edit_doctor_profile,
                    DoctorLoginView,
                    DoctorLogoutView,
                    view_patient_visits,
                    DeletePatientView, DeleteVisit)

urlpatterns = [
    path('create/', create_doctor, name='create'),
    path('accounts/profile/', view_doctor_profile, name='profile'),
    path('edit/', edit_doctor_profile, name='edit'),
    path('login/', DoctorLoginView.as_view(), name='login'),
    path('logout/', DoctorLogoutView.as_view(), name='logout'),
    path('visits/', view_patient_visits, name='visits'),
    path('patient/<int:pk>/', DeletePatientView.as_view(), name='delete'),
    path('delvisit/<int:pk>/', DeleteVisit.as_view(), name='delvisit'),
]

