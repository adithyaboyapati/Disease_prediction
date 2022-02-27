import numpy as np
import pickle
import streamlit as st

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
loaded_model = pickle.load(open('C:/Users/Adithya/Desktop/Ineuron/Omsairam_Projects_Resume/Thy_latest/rf_model.pkl', 'rb'))


# creating a function for Prediction

def thyroid_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    TSH_1, FTI_1, TT4_1, age_1, T4U_1, T3_1, on_thyroxine_1, sex_1 = input_data_as_numpy_array

    if sex_1 == 'Male':
        sex_con = 1
    else:
        sex_con = 0

    if on_thyroxine_1 =='Yes':
        on_thyroxine_conv = 1
    else:
        on_thyroxine_conv = 0

    TSH_1_conv = np.log(float(TSH_1) +1)
    FTI_1_conv = np.log(float(FTI_1) +1)
    TT4_1_conv = np.log(float(TT4_1) +1)
    age_1_conv = np.log(int(age_1) +1)
    T4U_1_conv = np.log(float(T4U_1) +1)
    T3_1_conv = np.log(float(T3_1) +1)

    input_data_as_numpy_array = np.asarray([TSH_1_conv, FTI_1_conv, TT4_1_conv, age_1_conv, T4U_1_conv, T3_1_conv, on_thyroxine_conv, sex_con])
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person has thyroid'
    else:
        return 'The person don\'t have thyroid'


def main():
    try:

        # giving a title
        st.title('Thyroid Prediction Web App')

        # getting the input data from the user

        TSH = st.text_input('Thyroid stimulating Hormone level')
        FTI = st.text_input('FTI level')
        TT4 = st.text_input('TT4 value')
        age = st.text_input('age of the person')
        T4U = st.text_input('T4U level')
        T3 = st.text_input('T3')
        on_thyroxine = st.selectbox('select on_thyroxine ',('Yes','No'))
        sex = st.selectbox('select Sex',('Male','Female'))

        # code for Prediction
        diagnosis = ''

        # creating a button for Prediction

        if st.button('Thyroid Test Result'):
            diagnosis = thyroid_prediction(
                [TSH, FTI , TT4, age , T4U , T3 , on_thyroxine, sex])

        st.success(diagnosis)
    except:
        st.error('Please enter the correct details')


if __name__ == '__main__':
    main()