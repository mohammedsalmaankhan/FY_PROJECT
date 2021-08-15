from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .facerec.click_photos import click
from .facerec.identify import identify2
from .models import Patient,Medical,Heart,Diabetes
from .forms import PatientForm,MedicalForm,HeartForm,DiabetesForm
from .facerec.train_model import trainer
import pandas as pd
import cv2
import datetime

def index(request):
    return render(request, 'app/index.html')


def add_photos(request):
	pt_list = Patient.objects.all()
	return render(request, 'app/add_photos.html', {'pt_list': pt_list})


def click_photos(request, pt_id):
	cam = cv2.VideoCapture(0)
	pt = get_object_or_404(Patient, id=pt_id)
	click(pt.name, pt.id, cam)
	return HttpResponseRedirect(reverse('add_photos'))

def identify(request):
    cap = cv2.VideoCapture(0)
    name=identify2(cap)
    cap.release()
    cv2.destroyAllWindows()
    if name == "unknown":
       return HttpResponseRedirect(reverse('index'))
    else:
       name=name.split('_')
       pt_id=name[1]
       pt = get_object_or_404(Patient, id=pt_id)
       mt = get_object_or_404(Medical, id=pt_id)
       return render(request, 'app/identified.html', {'Patient': pt, 'Medical': mt})



def train(request):
	trainer()
	return HttpResponseRedirect(reverse('index'))


def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            pt = form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PatientForm()
    return render(request, 'app/add_patient.html', {'form': form})

def add_medical(request):
	pt_list = Patient.objects.all()
	return render(request, 'app/Check_medical.html', {'pt_list': pt_list})



def Check_medical(request):

    if request.method == "POST":
        form = MedicalForm(request.POST)
        if form.is_valid():
            mt = form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = MedicalForm()
    return render(request, 'app/add_medical.html',{'form': form})

def diabetes(request):
    if request.method == "POST":
        form = DiabetesForm(request.POST)
        if form.is_valid():
            mt = form.save()
            id = mt.id
            name = mt.name
            age = mt.age
            glucose = mt.glucose
            blood_pressure = mt.blood_pressure
            skin_thickness = mt.skin_thickness
            insulin = mt.insulin
            BMI = mt.BMI
            DiabetesPedigreeFunction = mt.DiabetesPedigreeFunction
            pt = get_object_or_404(Patient, id=mt.id)
            print(pt)

            print(id,name,age,glucose,blood_pressure,skin_thickness,skin_thickness,BMI,DiabetesPedigreeFunction)
            model = pd.read_pickle(r"app/facerec/new_diabetes_model.pickle")
            result = model.predict([[ glucose,blood_pressure,skin_thickness,skin_thickness,BMI,DiabetesPedigreeFunction,age]])
            if result==0:
                print("Not Diabetic")
                r1 = "This Patient is NOT DIABETC"
            else:
                print("Diabetic")
                r1 = "This Patient is DIABETIC"
            return render(request, 'app/result.html',{'Patient':pt,'Result': r1})
    else:
        form = DiabetesForm()
    return render(request, 'app/diab_pred.html',{'Diabetes': form})


def heart_pred(request):
    if request.method == "POST":
        form = HeartForm(request.POST)
        if form.is_valid():
            mt = form.save()
            id = mt.id
            name = mt.name
            age = mt.age
            gender = mt.gender

            chest_pain = mt.chest_pain
            cp_0=0
            cp_1=0
            cp_2=0
            cp_3=0
            print(cp_0,cp_1,cp_2,cp_3)
            if(chest_pain==3):
                cp_3=1
            elif(chest_pain==2):
                cp_2=1
            elif(chest_pain==1):
                cp_1=1
            else:
                cp_0=1
            blood_pressure = mt.blood_pressure
            cholestoral = mt.cholestoral
            fasting_blood = mt.fasting_blood
            restecg = mt.restecg
            max_heart = mt.max_heart
            exang = mt.exang
            old_peak = mt.old_peak
            slope = mt.slope
            slope_0=0
            slope_1=0
            slope_2=0
            if(slope==2):
                slope_2=1
            elif(slope==1):
                slope_1=1
            else:
                slope_0=1
            ca = mt.ca
            thal = mt.thal
            thal_0=0
            thal_1=0
            thal_2=0
            thal_3=0
            if(thal==3):
                thal_3=1
            elif(thal==2):
                thal_2=1
            elif(thal==1):
                thal_1=1
            else:
                thal_0=1
            pt = get_object_or_404(Patient, id=mt.id)
            print(id,name,age,gender,chest_pain,blood_pressure,cholestoral,fasting_blood,restecg,max_heart,exang,old_peak,slope,ca)
            model = pd.read_pickle(r"app/facerec/new_model.pickle")
            result = model.predict([[ age, gender, blood_pressure,cholestoral,fasting_blood,restecg,max_heart,exang,old_peak,ca ,cp_0,cp_1,cp_2,cp_3,thal_0,thal_1,thal_2,thal_3,slope_0,slope_1,slope_2]])
            if result==0:
                print("Not Diabetic")
                r1 = "This Patient has more chances of getting Heart Diseases"
            else:
                print("Diabetic")
                r1 = "This Patient has lower chances of getting a Heart Disease"
            return render(request, 'app/result.html',{'Patient':pt,'Result': r1})
    else:
        form = HeartForm()
    return render(request, 'app/heart_pred.html',{'Heart': form})
