
import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='My App',
    layout='wide',
    page_icon=':rocket:',
)


st.markdown("<h1 style='text-align: center; color: red;'>Migraine Predictor App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Enter Details Below</h1>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
global location , character , nausea ,family_bg , tinnitus , vomit, vertigo, age

with col1:
  
 
    age = st.text_input("Enter Age: ")
   
    duration = st.radio("Duration in Days:",('1','2','3'))
    frequency= st.selectbox('Enter frequency in a month:',('1', '2', '3','4','5'))
    dur= st.radio("Duration in Days:",('None','Unilateral','Bilateral'))

    if dur == 'None':
        location=0
    elif dur == 'Unilateral':
        location=1
    elif dur== 'Bilateral':
        location=2

    chr= st.radio("Enter Character", ('None','Throbbing','Constant Pain'))

    if chr == 'None':
        character=0
    elif chr == 'Throbbing':
        character=1
    elif chr== 'Constant Pain':
        character=2
    

    

with col2:
    nausea= st.radio("Are you having nauseaous? ",('Yes','No'))

    if nausea== 'Yes':
        nausea=1
    elif nausea== 'No':
        nausea=0
    
    vomit= st.radio("Are you having Vomiting? ",('Yes','No'))
    if vomit== 'Yes':
        vomit=1
    elif vomit== 'No':
        vomit=0
    
    vertigo= st.radio("Are you having Vertigo? ",('Yes','No'))
    if vertigo== 'Yes':
        vertigo=1
    elif vertigo== 'No':
        vertigo=0
   
    tinnitus= st.radio("Are you having Tinnitus? ",('Yes','No'))
    if tinnitus== 'Yes':
        tinnitus=1
    elif tinnitus== 'No':
        tinnitus=0
    
    family_bg= st.radio("Does anyone in your family have the same issue?",('Yes','No'))
    if family_bg== 'Yes':
        family_bg=1
    elif family_bg== 'No':
        family_bg=0

    intensity= st.radio("Enter Pain Intensity ",('0','1','2','3'))


try:
    df = np.array(
    [
        age,
        duration,
        frequency,
        location,
        character,
        intensity,
        nausea,
        vomit,
        vertigo,
        tinnitus,
        family_bg,
    ]
    )

    with open(r"final.pkl", "rb") as f:
        model = pickle.load(f)

    pred = model.predict(df.reshape(1, -1))
    if pred == 0:
        st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE SPORADIC HEMIPLEGIC MIGRAINE</h2>", unsafe_allow_html=True)
      
    elif pred == 1:
        st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE TYPICAL AURA WITHOUT MIGRAINE</h2>", unsafe_allow_html=True)
       
    elif pred == 2:
        st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE  MIGRAINE WITHOUT AURA</h2>", unsafe_allow_html=True)
        
    elif pred == 3:
        st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE BASILAR TYPE AURA MIGRAINE</h2>", unsafe_allow_html=True)
       
    elif pred == 4:
        st.markdown("<h2 style='text-align: center; color: green;'>You have some other type of migraine, please go to an actual medical professional.</h2>", unsafe_allow_html=True)

    elif pred == 5:
        st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE TYPICAL AURA WITH MIGRAINE</h2>", unsafe_allow_html=True)
        
    elif pred == 6:
        st.markdown("<h2 style='text-align: center; color: green;'>YOU HAVE FAMILIAL HEMIPLEGIC MIGRAINE</h2>", unsafe_allow_html=True)


except ValueError:
    st.error("Please enter a valid age")


