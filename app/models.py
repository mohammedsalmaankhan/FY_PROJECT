from django.db import models
from datetime import datetime
import os




class Patient(models.Model):
	id = models.CharField(primary_key=True, max_length=10)
	Aadhar_num = models.CharField(max_length=16)
	name = models.CharField(max_length=50)
	contact_number = models.CharField(max_length=50)
	date_of_birth = models.CharField(max_length=50)
	gender = models.CharField(max_length=8)
	email = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	def num_photos(self):
		try:
			DIR = f"app/facerec/dataset/{self.name}_{self.id}"
			img_count = len(os.listdir(DIR))
			return img_count
		except:
			return 0

class Medical(models.Model):
	id = models.CharField(primary_key=True, max_length=10)
	name = models.CharField(max_length=50)
	blood_group = models.CharField(max_length=50)
	height = models.CharField(max_length=50)
	weight = models.CharField(max_length=8)
	medical_condition1 = models.CharField(max_length=50)
	medical_condition2 = models.CharField(max_length=50)
	medical_condition3 = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Heart(models.Model):
	id = models.CharField(primary_key=True, max_length=10)
	name = models.CharField(max_length=50)
	age = models.CharField(max_length=5)
	gender =models.CharField(max_length=10)
	chest_pain = models.CharField(max_length=5)
	blood_pressure = models.CharField(max_length=5)
	cholestoral = models.CharField(max_length=5)
	fasting_blood = models.CharField(max_length=5)
	restecg = models.CharField(max_length=5)
	max_heart= models.CharField(max_length=5)
	exang = models.CharField(max_length=5)
	old_peak = models.CharField(max_length=5)
	slope=models.CharField(default=0,max_length=2)
	ca=models.CharField(default=0,max_length=1)
	thal=models.CharField(default=1,max_length=2)

	def __str__(self):
		return self.name

class Diabetes(models.Model):
	id = models.CharField(primary_key=True, max_length=10)
	name = models.CharField(max_length=50)
	age = models.CharField(max_length=5)
	glucose =  models.CharField(max_length=5)
	blood_pressure =  models.CharField(max_length=5)
	skin_thickness =  models.CharField(max_length=5)
	insulin =  models.CharField(max_length=5)
	BMI =  models.CharField(max_length=5)
	DiabetesPedigreeFunction =  models.CharField(max_length=5)


	def __str__(self):
		return self.name
