from django.shortcuts import render, redirect
from .forms import FormPatient, FormVisit
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def show_patient_form(request):
    if request.method == 'POST':
        form_instance = FormPatient(request.POST, request.FILES)
        if form_instance.is_valid():
            name = form_instance.cleaned_data.get('name')
            form_instance.instance.doctor = request.user  # will save the doctor object in the patient's record
            form_instance.save()
            messages.success(request, f"Details of patient {name} saved in records")
            return redirect('profile')            
        else:
            messages.error(request, form_instance.errors)
            return render(request, 'patient/patient-form.html', {'patient_form':FormPatient()})
    else:
        return render(request, 'patient/patient-form.html', {'patient_form':FormPatient()})
    

@login_required
def show_visit_form(request):    
    if request.method == 'POST':
        form_instance = FormVisit(request.POST)
        if form_instance.is_valid():
            name = form_instance.cleaned_data.get('patient')
            form_instance.instance.charges = request.user.doctorprofile.fees
            form_instance.instance.doctor = request.user
            form_instance.save()
            messages.success(request, f"Details of {name}'s visit saved in records")
            return redirect('visits')
        else:
            messages.error(request, form_instance.errors)
            return render(request, 'patient/visit-form.html', {'vist_form':FormVisit()})
    else:
        return render(request, 'patient/visit-form.html', {'vist_form':FormVisit()})
    


def home_view(request):
    return render(request, 'patient/home.html', {})