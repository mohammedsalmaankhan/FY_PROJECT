import pandas as pd
import seaborn as sns
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import statistics
from scipy.stats import ttest_1samp
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
def pred_diabetes():
    file="/home/ahmed/MainProject/MAIN/app/facerec/Diabetes_dataset/diabetes.csv"
    df=pd.read_csv(file)
    df=df.drop(columns = ['Pregnancies'])
    index_names= df[(df['BMI']>50)].index
    df.drop(index_names,inplace=True)
    index_names= df[(df['BMI']<10)].index
    df.drop(index_names,inplace=True)
    index_names= df[(df['BloodPressure']<40)].index
    df.drop(index_names,inplace=True)
    index_names= df[(df['Glucose']<25)].index
    df.drop(index_names,inplace=True)
    index_names= df[(df['SkinThickness']>85)].index
    df.drop(index_names,inplace=True)
    index_names= df[(df['Insulin']>600)].index
    df.drop(index_names,inplace=True)
    index_names= df[(df['DiabetesPedigreeFunction']>2.0)].index
    df.drop(index_names,inplace=True)
    X = df.drop(columns=['Outcome'])
    y = df['Outcome']
    sm = SMOTE(random_state = 2)
    X, y = sm.fit_resample(X, y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

    model = RandomForestClassifier(n_estimators = 1000, random_state = 1)
    model.fit(X_train, y_train)

    acc = model.score(X_test,y_test)*100

    print("Random Forest Algorithm Accuracy Score : {:.2f}%".format(acc))



    # Pickle model
    pd.to_pickle(model,r'new_diabetes_model.pickle')

pred_diabetes()
