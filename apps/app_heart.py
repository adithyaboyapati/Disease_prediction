import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler

import base64


def set_bg_hack_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://ghantee.com/wp-content/uploads/2020/07/tree-wallpaper-illustration-fantasy-HD.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
set_bg_hack_url()




# loading the saved model
loaded_model = pickle.load(open('heart_pred.pkl', 'rb'))
sc = pickle.load(open('transform.pkl', 'rb'))

# creating a function for Prediction

def heart_disease_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    input_data_as_numpy_array = sc.transform([input_data_as_numpy_array])

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
        return 'The person has heart disease'
    else:
        return 'The person don\'t have heart disease'


def main():
    try:
        # giving a title
        st.title('Heart Disease Prediction Web App')

        # getting the input data from the user
        age = st.text_input('age')
        sex = st.selectbox('sex',(0,1))
        chest_pain_type = st.selectbox('chest_pain_type',(0,1,2,3))
        resting_blood_sugar = st.text_input('resting_blood_sugar')
        cholesterol = st.text_input('cholesterol')
        fasting_blood_sugar = st.selectbox('fasting_blood_sugar', (0,1))
        rest_ecg = st.selectbox('rest_ecg',(0,1,2,3))
        max_heart_rate_achieved = st.text_input('max_heart_rate_achieved')
        exercise_induced_angina = st.selectbox('exercise_induced_angina', (0,1))
        st_depression = st.text_input('st_depression')
        st_slope = st.selectbox('st_slope', (0, 1, 2))
        num_major_vessels = st.selectbox('num_major_vessels',(0,1,2,3,4))
        thalassemia = st.selectbox('thalassemia',(0,1,2,3))



        # code for Prediction
        diagnosis = ''

        # creating a button for Prediction

        if st.button('Heart Disease Test Result'):
            diagnosis = heart_disease_prediction(
                [age,sex,chest_pain_type,resting_blood_sugar,cholesterol,
           fasting_blood_sugar, rest_ecg,max_heart_rate_achieved,
           exercise_induced_angina,st_depression, st_slope,
           num_major_vessels, thalassemia])

        st.success(diagnosis)
    except:
        st.error('Please enter the correct details')


if __name__ == '__main__':
    main()