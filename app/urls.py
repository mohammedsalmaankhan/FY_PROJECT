from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_photos/', views.add_photos, name='add_photos'),
    path('add_photos/<slug:pt_id>/', views.click_photos, name='click_photos'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('Check_medical/', views.Check_medical ,name='check_medical'),
#   path('Check_medical/<slug:pt_id>/add_medical', views.add_medical, name='add_medical'),
    path('identify/', views.identify, name='identify'),
    path('identify/identified/', views.identify, name='identified'),
    path('train/', views.train, name='train'),
    path('heart_pred/', views.heart_pred, name='heart_pred'),
    path('heart_pred/result/', views.heart_pred, name='heart_pred'),
    path('DiabetesPrediction/', views.diabetes, name='diabetes'),
    path('DiabetesPrediction/<slug:pt_id>/result/', views.diabetes, name='diabetes'),

]
