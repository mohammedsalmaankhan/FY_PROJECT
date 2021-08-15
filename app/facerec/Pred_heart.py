import pandas as pd
import seaborn as sns
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import statistics
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split



def pred_heart():
    file="/home/ahmed/MainProject/MAIN/app/facerec/Heart_dataset/heart.csv"
    df=pd.read_csv(file)
    a = pd.get_dummies(df['cp'], prefix = "cp")
    b = pd.get_dummies(df['thal'], prefix = "thal")
    c = pd.get_dummies(df['slope'], prefix = "slope")
    frames = [df, a, b, c]
    df = pd.concat(frames, axis = 1)
    df = df.drop(columns = ['cp', 'thal', 'slope'])
    y = df.target.values
    x_data = df.drop(['target'], axis = 1)
    x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data)).values
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=0)
    x_train = x_train.T
    y_train = y_train.T
    x_test = x_test.T
    y_test = y_test.T
    model = SVC()
    model.fit(x_train.T, y_train.T)

    acc = model.score(x_test.T,y_test.T)*100

    print("Support Vector Machine Accuracy Score : {:.2f}%".format(acc))



    # Pickle model
    pd.to_pickle(model,r'new_model.pickle')

pred_heart()
