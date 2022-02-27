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
loaded_model = pickle.load(open('C:/Users/Adithya/Desktop/Ineuron/Omsairam_Projects_Resume/Parkinson_disease_prediction/rf_model_parkinson.pkl', 'rb'))


# creating a function for Prediction

def parkinson_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    MDVP_Fo, PPE, spread1, MDVP_Flo, spread2,MDVP_Fhi, D2, MDVP_Jitter, Jitter_DDP, Shimmer_DDA = input_data_as_numpy_array


    MDVP_Fo_1_conv = np.log(float(MDVP_Fo) +1)
    PPE_1_conv = np.log(float(PPE) +1)
    spread1_1_conv = np.log(float(spread1) +1)
    MDVP_Flo_1_conv = np.log(float(MDVP_Flo) +1)
    spread2_1_conv = np.log(float(spread2) +1)
    MDVP_Fhi_1_conv = np.log(float(MDVP_Fhi) +1)
    D2_1_conv = np.log(float(D2) +1)
    MDVP_Jitter_1_conv = np.log(float(MDVP_Jitter) + 1)
    Jitter_DDP_1_conv = np.log(float(Jitter_DDP) + 1)
    Shimmer_DDA_1_conv = np.log(float(Shimmer_DDA) + 1)

    input_data_as_numpy_array = np.asarray([MDVP_Fo_1_conv, PPE_1_conv,spread1_1_conv,MDVP_Flo_1_conv,
                                            spread2_1_conv,MDVP_Fhi_1_conv,D2_1_conv,MDVP_Jitter_1_conv,
                                            Jitter_DDP_1_conv,Shimmer_DDA_1_conv])
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
        return 'The person has parkinson'
    else:
        return 'The person don\'t have parkinson'


def main():
    try:
        # giving a title
        st.title('Parkinson Prediction Web App')

        # getting the input data from the user

        MDVP_Fo = st.text_input('MDVP:Fo(Hz) level')
        PPE = st.text_input('PPE')
        spread1 = st.text_input('spread1')
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
        spread2 = st.text_input('spread2')
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
        D2 = st.text_input('D2')
        MDVP_Jitter = st.text_input('MDVP:Jitter(Abs)')
        Jitter_DDP = st.text_input('Jitter:DDP')
        Shimmer_DDA = st.text_input('Shimmer:DDA')

        # code for Prediction
        diagnosis = ''

        # creating a button for Prediction

        if st.button('Parkinson Result'):
            diagnosis = parkinson_prediction(
                [MDVP_Fo,PPE,spread1,MDVP_Flo,spread2,
           MDVP_Fhi, D2, MDVP_Jitter, Jitter_DDP, Shimmer_DDA])

        st.success(diagnosis)
    except:
        st.error('Please enter the correct details')


if __name__ == '__main__':
    main()