import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title="My App", layout="wide", page_icon=":rocket:")


st.markdown(
    "<h1 style='text-align: center; color: red;'>Migraine Predictor App</h1>",
    unsafe_allow_html=True,
)
# st.title("Migraine Predictor App")
st.markdown(
    "<h2 style='text-align: center; color: black;'>General Information</h2>",
    unsafe_allow_html=True,
)
# st.header("General Information")

tab1, tab2 = st.tabs(["About Migraine", "About Dataset"])

with tab1:
    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.write("")

    with col2:
        image1 = Image.open("./images/types_headaches.png")
        st.image(
            image1,
            caption=None,
            width=700,
            clamp=False,
            channels="RGB",
            output_format="auto",
        )

    with col3:
        st.write("")

    st.markdown(
        "<h2 style='text-align: center; color: black;'>What is a Migraine?</h2>",
        unsafe_allow_html=True,
    )
    st.write(
        "A migraine is usually a moderate or severe headache felt as a throbbing pain on 1 side of the head. Many people also have symptoms such as feeling sick, being sick and increased sensitivity to light or sound. Migraine is a common health condition, affecting around 1 in every 5 women and around 1 in every 15 men. They usually begin in early adulthood."
    )

    st.markdown(
        "<h3 style='text-align: left; color: black;'>Types of Migraine Headaches</h3>",
        unsafe_allow_html=True,
    )
    st.write(
        "The two major categories are migraine with aura called classical migraines and migraine without aura formerly known as common migraines. Aura usually includes visual symptoms like lines, shapes, or flashes. You may even lose some of your vision for 10 to 30 minutes. You could also feel tingling in your arms and legs. Auras can even affect smell, taste, touch, or speech.Aura happens to about 1 in 4 people who get migraine headaches. It usually starts before the head pain begins and lasts up to an hour."
    )

    st.markdown(
        "<h4 style='text-align: left; color: black;'>1.With Brainstem Aura</h4>",
        unsafe_allow_html=True,
    )

    st.write(
        "This used to be called basilar type migraine. It includes visual, sensory, or speech or language symptoms and at least two of the following: slurred speech, vertigo (a sensation of spinning or dizziness), tinnitus (ringing in the ears), double vision, unsteadiness, and a severe sensitivity to sound."
    )

    st.markdown(
        "<h4 style='text-align: left; color: black;'>2.Episodic</h4>",
        unsafe_allow_html=True,
    )
    st.write(
        "This is the general pattern for most people with migraine. It means you get migraine attacks from time to time – up to about 7 days out of the month. In general, if you have a headache or migraine attack on more than 7 days out of the month, you may have a more serious form of migraine like high-frequency episodic migraine or chronic migraine "
    )

    st.markdown(
        "<h4 style='text-align: left; color: black;'>3.Chronic</h4>",
        unsafe_allow_html=True,
    )
    st.write(
        "This is a headache that happens 15 or more days a month for more than 3 months. It includes migraine symptoms on at least 8 of those days each month."
    )

    st.markdown(
        "<h4 style='text-align: left; color: black;'>4.Hemiplegic</h4>",
        unsafe_allow_html=True,
    )
    st.write(
        "This word mean paralysis on one side of the body. The aura that comes along with these headaches causes temporary (less than 72 hours) weakness on one side of the body. The aura symptoms usually go away within 24 hours.The symptoms are very similar to a stroke but cause no lasting nerve damage."
    )

    st.markdown(
        "<h4 style='text-align: left; color: black;'>5.Migraine Without Headache (Silent Migraine)</h4>",
        unsafe_allow_html=True,
    )
    st.write(
        "Yes, you can have a migraine without head pain. It's often called a silent migraine. Aura is usually the main warning sign of this type of migraine. But you may also have nausea and other migraine symptoms. It usually lasts only about 20-30 minutes."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        image = Image.open("./images/Migraine1.jpg")
        st.image(
            image,
            caption=None,
            use_column_width="always",
            clamp=False,
            channels="RGB",
            output_format="auto",
        )

    with col2:
        image = Image.open("./images/migraine2.jfif")
        st.image(
            image,
            caption=None,
            use_column_width="always",
            clamp=False,
            channels="RGB",
            output_format="auto",
        )

    with col3:
        image = Image.open("./images/migraine3.webp")
        st.image(
            image,
            caption=None,
            use_column_width="always",
            clamp=False,
            channels="RGB",
            output_format="auto",
        )

    st.markdown(
        "<h3 style='text-align: center; color: black;'>When to get medical advice</h3>",
        unsafe_allow_html=True,
    )
    st.write("You should see a GP if you have frequent or severe migraine symptoms.")
    st.write(
        "Simple painkillers, such as paracetamol or ibuprofen, can be effective for migraine.Try not to use the maximum dosage of painkillers on a regular or frequent basis as this could make it harder to treat headaches over time.You should also make an appointment to see a GP if you have frequent migraines (on more than 5 days a month), even if they can be controlled with medicines, as you may benefit from preventative treatment."
    )

    st.write(
        "You should call 999 for an ambulance immediately if you or someone you're with experiences:"
    )
    st.write("1. Paralysis or weakness in 1 or both arms or 1 side of the face")
    st.write("2. Slurred or garbled speech")
    st.write(
        "3. A sudden agonising headache resulting in a severe pain unlike anything experienced before headache along with a high temperature (fever), stiff neck, mental confusion, seizures, double vision and a rash"
    )
with tab2:
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.subheader("About Dataset")
        st.write(
            "Database comprising 400 medical records of users diagnosed with various pathologies associated with migraines. Data were recorded by trained medical personnel at the Centro Materno Infantil de Soledad during the first quarter of 2013.The compiled database contains information regarding symptoms or variable of interest required for the classification of migraines."
        )
        st.subheader("About Model")

        st.write(
            "We have created a Random Forest Classifier Predictor (RFC) on the above dataset. We have performed Exploratory Data Analysis (EDA) on the kaggle Migraine dataset and made some insightful assumption regarding the various atrributes present in dataset out of which we used 11 attributes out of 24 attributes in building our RFC model. Our model is giving 94.6 accuracy. "
        )

        st.markdown(
            "<h3 style='text-align: left; color: black;'>Random Forest Classifier </h4>",
            unsafe_allow_html=True,
        )
        st.write(
            "Random Forest Algorithm is bets example for bagging technique but with little tweak.  Random Forest models decide where to split based on a random selection of features. Rather than splitting at similar features at each node throughout, Random Forest models implement a level of differentiation because each tree will split based on different features. This level of differentiation provides a greater ensemble to aggregate over, ergo producing a more accurate predictor."
        )
        st.markdown(
            "<h4 style='text-align: left; color: black;'> Advantages of using Random Forest technique:</h4>",
            unsafe_allow_html=True,
        )
        st.write("1. Handles higher dimensionality data very well.")
        st.write("2. Handles missing values and maintains accuracy for missing data.")
        st.markdown(
            "<h4 style='text-align: left; color: black;'> Disadvantages of using Random Forest technique:</h4>",
            unsafe_allow_html=True,
        )
        st.write(
            "1. Since final prediction is based on the mean predictions from subset trees, it won’t give precise values for the regression model."
        )

    with col2:
        image = Image.open("./images/migraine-headache.jpeg")
        st.image(
            image,
            caption=None,
            use_column_width="always",
            clamp=False,
            channels="RGB",
            output_format="auto",
        )

        image1 = Image.open("./images/rfc.png")
        st.image(
            image1,
            caption=None,
            use_column_width="always",
            clamp=False,
            channels="RGB",
            output_format="auto",
        )
