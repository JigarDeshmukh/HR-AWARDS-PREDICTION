import streamlit as sl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


sl.title("HR DASHBOARD")
data=pd.read_csv("datset_hr_encode")

x=data.drop(["Unnamed: 0","awards"],axis=1)
y=data.iloc[:,-2]
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)

sl.write('''THIS IS THE PREDICTOR OF AWARDS ON BASIS OF CANDIDIATE PERFORMANCE IN DIFFERENT SECTORS

                                SELECT FROM LEFT COLUMNS FOR ANY INFORMATION''')
sl.image("human.jpg")
def user():
    department = sl.sidebar.selectbox("department",['Sales & Marketing', 'operation', 'Procurement', 'Technology', 'Analytics','Finance', 'HR', 'R&D', 'Legal'])
    education = sl.sidebar.selectbox("Education Qualifications", ['Bachelor', 'Masters and above', 'Below Secondary'])
    gender = sl.sidebar.selectbox("Gender", ["Male", "Female"])
    Recuritment = sl.sidebar.selectbox("Recuritment", ["other", "sourcing", "referred"])
    Training = sl.sidebar.slider("Select the Training Years", 1, 9)
    Age = sl.sidebar.slider("Select the Age", 1, 61)
    Rating = sl.sidebar.slider("Select Previous Year Rating", 1, 5)
    Length_of_Service = sl.sidebar.slider("Length of Service", 1, 34)
    KPI_ABOVE_80 = sl.sidebar.selectbox("KPI", ['select',1,0])
    Training_score = sl.sidebar.slider("Select Training score of candidate", 1, 99)


    user={
        "department":department,
        "education":education,
        "gender":gender,
        "Recuritmment":Recuritment,
        "Training":Training,
        "Age":Age,
        "Rating":Rating,
        "Length_of_Service":Length_of_Service,
        "KPI_ABOVE_80":KPI_ABOVE_80,
        "Training_score":Training_score
    }

    report_data=pd.DataFrame(user,index=[0])


    for i in report_data:
        le=LabelEncoder()
        report_data[i]=le.fit_transform(report_data[i])
    return report_data

user_data=user()
rf=RandomForestClassifier(bootstrap=True,max_depth=90,max_features=3,min_samples_leaf=3,min_samples_split=8,n_estimators=200)
rf.fit(xtrain,ytrain)
user_result=rf.predict(user_data)
sl.subheader('PREDICTION OF THE POINT YOU GIVEN ARE AS FOLLOW')

output=''
if (user_result[0]==0):
    output="NO HE WONT"
    sl.write(output)

else:
    output="HE CAN BE GIVEN AN AWARD"
    sl.write(output)
