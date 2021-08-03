import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(battery_power,ram,three_g,dual_sim):   
    prediction=classifier.predict([[battery_power,ram,three_g,dual_sim]])
    print(prediction)
    return prediction



def main():
    st.title("Mobile Price Predictor")
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Mobile Price Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    battery_power = st.text_input("battery_power","Type Here")
    ram = st.text_input("ram","Type Here")
    three_g = st.text_input("three_g","Type Here")
    dual_sim = st.text_input("dual_sim","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(battery_power,ram,three_g,dual_sim)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
