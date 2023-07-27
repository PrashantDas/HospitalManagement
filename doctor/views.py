from django.shortcuts import render, redirect
from .forms import FormCreateDoctor, FormEditProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import DoctorProfile
from patient.models import ModelVisit
from patient.models import ModelPatient, ModelVisit
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.conf import settings

def create_doctor(request):
    """ Saves details of new doctors in the database """
    if request.method == 'POST':
        form_instance = FormCreateDoctor(request.POST)
        if form_instance.is_valid():
            first = form_instance.cleaned_data.get('first_name')
            last = form_instance.cleaned_data.get('last_name')
            form_instance.save()
            messages.success(request, f"Dr. {first} {last} registered")
            return redirect('home')
        else:
            messages.error(request, form_instance.errors)
            context = {'doctorform': FormCreateDoctor()}
            return render(request, 'doctor/create-doctor.html', context)
    else:
        context = {'doctorform': FormCreateDoctor()}
        return render(request, 'doctor/create-doctor.html', context)
    

@login_required
def view_doctor_profile(request):
    # details of the doctor pulled from 'user', details of patients passed in context
    my_patients = ModelPatient.objects.filter(doctor=request.user) # iexact cannot be used on foreign-key
    return render(request, 'doctor/doctor-profile.html',{'my_patients': my_patients})

@login_required
def view_patient_visits(request):
    my_visits = ModelVisit.objects.filter(doctor=request.user)
    return render(request, 'doctor/doctor-visits.html',{'my_visits': my_visits})

@login_required
def edit_doctor_profile(request):
    if request.method == 'POST':
        form_instance = FormEditProfile(request.POST, instance=request.user.doctorprofile)
        if form_instance.is_valid():
            form_instance.save()
            messages.success(request, 'Profile updated !')
            return redirect('profile')
        else:
            messages.error(request, form_instance.errors)
            context = {'FormProfile': FormEditProfile(instance=request.user.doctorprofile)}
            return render(request, 'doctor/edit-doctor-profile.html', context)
    else:
        context = {'FormProfile': FormEditProfile(instance=request.user.doctorprofile)}
        return render(request, 'doctor/edit-doctor-profile.html', context)
    


class DoctorLoginView(SuccessMessageMixin, LoginView):
    success_message = 'Login Successful'


class DoctorLogoutView(LogoutView):
    template_name = 'registration/logout.html'


class DeletePatientView(SuccessMessageMixin, DeleteView):
    model = ModelPatient
    success_message = 'Patient record was deleted'
    success_url = reverse_lazy('profile')


class DeleteVisit(SuccessMessageMixin, DeleteView):
    model = ModelVisit
    success_message = 'Visit record was deleted'
    success_url = reverse_lazy('visits')