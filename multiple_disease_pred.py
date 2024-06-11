# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:37:34 2024

@author: jaggu
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
diabetes_model = pickle.load(open('C:/Users/user/Desktop/Multiple_Disease/multiple_dis_pred_system/sav files/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('C:/Users/user/Desktop/Multiple_Disease/multiple_dis_pred_system/sav files/heart_model.sav', 'rb'))
parkinson_model = pickle.load(open('C:/Users/user/Desktop/Multiple_Disease/multiple_dis_pred_system/sav files/parkinson_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes prediction page
if selected == "Diabetes Prediction":
    st.title('Diabetes Prediction using ML')
    
    # Getting the input data from the user
    cols1, cols2, cols3 = st.columns(3)
    
    with cols1:
        Pregnancies = st.text_input('Number of Pregnancies')
        Glucose = st.text_input('Glucose Level')
        BloodPressure = st.text_input('Blood Pressure')
        
    with cols2:
        SkinThickness = st.text_input('Skin Thickness')
        Insulin = st.text_input('Insulin Level')
        BMI = st.text_input('BMI')
        
    with cols3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
        Age = st.text_input('Age')
        
    # Code for Prediction
    diab_diagnosis = ''
    
    # Creating a Button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

# Heart disease prediction page
if selected == "Heart Disease Prediction":
    st.title('Heart Disease Prediction using ML')
    
    # Getting the input data from the user
    cols1, cols2, cols3 = st.columns(3)
    
    with cols1:
        Age = st.text_input('Age')
        Sex = st.text_input('Sex (1 = male; 0 = female)')
        ChestPainType = st.text_input('Chest Pain Type (0-3)')
        
    with cols2:
        RestingBP = st.text_input('Resting Blood Pressure')
        Cholesterol = st.text_input('Serum Cholesterol')
        FastingBS = st.text_input('Fasting Blood Sugar (> 120 mg/dl, 1 = true; 0 = false)')
        
    with cols3:
        RestingECG = st.text_input('Resting Electrocardiographic Results (0-2)')
        MaxHR = st.text_input('Maximum Heart Rate Achieved')
        ExerciseAngina = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
        
        
        
    cols4, cols5 = st.columns(2)
    
    with cols4:
        MajorVessels = st.text_input('Number of Major Vessels (0-3) Colored by Fluoroscopy')
        Oldpeak = st.text_input('Oldpeak')
        
    with cols5:
        Thal = st.text_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)')
        ST_Slope = st.text_input('Slope of the Peak Exercise ST Segment (0-2)')
    # Code for Prediction
    heart_diagnosis = ''
    
    # Creating a Button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope, MajorVessels, Thal]])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
        
    st.success(heart_diagnosis)

# Parkinson's disease prediction page
if selected == "Parkinson Prediction":
    st.title('Parkinson Prediction using ML')
    
    # Getting the input data from the user
    cols1, cols2, cols3 = st.columns(3)
    
    with cols1:
        MDVP_Fo_Hz = st.text_input('MDVP: Fo (Hz)')
        MDVP_Fhi_Hz = st.text_input('MDVP: Fhi (Hz)')
        MDVP_Flo_Hz = st.text_input('MDVP: Flo (Hz)')
        
    with cols2:
        MDVP_Jitter_percent = st.text_input('MDVP: Jitter (%)')
        MDVP_Jitter_Abs = st.text_input('MDVP: Jitter (Abs)')
        MDVP_RAP = st.text_input('MDVP: RAP')
        
    with cols3:
        MDVP_PPQ = st.text_input('MDVP: PPQ')
        Jitter_DDP = st.text_input('Jitter: DDP')
        MDVP_Shimmer = st.text_input('MDVP: Shimmer')
       
        
    cols4, cols5 = st.columns(2)
    
    with cols4:
        Shimmer_APQ3 = st.text_input('Shimmer: APQ3')
        Shimmer_APQ5 = st.text_input('Shimmer: APQ5')
        MDVP_APQ = st.text_input('MDVP: APQ')
        
    with cols5:
        Shimmer_DDA = st.text_input('Shimmer: DDA')
        NHR = st.text_input('NHR')
        HNR = st.text_input('HNR')
        
    cols6, cols7 = st.columns(2)
    
    with cols6:
        RPDE = st.text_input('RPDE')
        DFA = st.text_input('DFA')
        MDVP_Shimmer_dB = st.text_input('MDVP: Shimmer (dB)')
        
    with cols7:
        spread1 = st.text_input('Spread1')
        spread2 = st.text_input('Spread2')
        D2 = st.text_input('D2')
        PPE = st.text_input('PPE')
    
    # Code for Prediction
    parkinson_diagnosis = ''
    
    # Creating a Button for Prediction
    if st.button('Parkinson Test Result'):
        parkinson_prediction = parkinson_model.predict([[MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = 'The person has Parkinson\'s disease'
        else:
            parkinson_diagnosis = 'The person does not have Parkinson\'s disease'
        
    st.success(parkinson_diagnosis)
