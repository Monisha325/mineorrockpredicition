# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 21:16:55 2025

@author: patna
"""

import numpy as np
import pickle 
import streamlit as st

#load the saved model
loaded_model = pickle.load(open('C:/Users/patna/OneDrive/Desktop/RockVsMinePredicition/trained_model.sav','rb'))

#creating a function for prediction

def rock_mine_prediction(input_data):
    
    #changing the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the np array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]=='R'):
      return 'The object is a Rock'
    else:
      return 'The object is a Mine'
  
def main():
    
    #giving a title
    st.title('Rock Vs Mine Prediction App')
    
    #getting input data from the user
    X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,X24,X25,X26,X27,X28,X29,X30,X31,X32,X33,X34,X35,X36,X37,X38,X39,X40,X41,X42,X43,X44,X45,X46,X47,X48,X49,X50,X51,X52,X53,X54,X55,X56,X57,X58,X59,X60
    
    X1=st.text_input('Enter the X1 value')
    X2=st.text_input('Enter the X2 value')
    X3=st.text_input('Enter the X3 value')
    X4=st.text_input('Enter the X4 value')
    X5=st.text_input('Enter the X5 value')
    X6=st.text_input('Enter the X6 value')
    X7=st.text_input('Enter the X7 value')
    X8=st.text_input('Enter the X8 value')
    X9=st.text_input('Enter the X9 value')
    X10=st.text_input('Enter the X10 value')
    X11=st.text_input('Enter the X11 value')
    X12=st.text_input('Enter the X12 value')
    X13=st.text_input('Enter the X13 value')
    X14=st.text_input('Enter the X14 value')
    X15=st.text_input('Enter the X15 value')
    X16=st.text_input('Enter the X16 value')
    X17=st.text_input('Enter the X17 value')
    X18=st.text_input('Enter the X18 value')
    X19=st.text_input('Enter the X19 value')
    X20=st.text_input('Enter the X20 value')
    X21=st.text_input('Enter the X21 value')
    X22=st.text_input('Enter the X22 value')
    X23=st.text_input('Enter the X23 value')
    X24=st.text_input('Enter the X24 value')
    X25=st.text_input('Enter the X25 value')
    X26=st.text_input('Enter the X26 value')
    X27=st.text_input('Enter the X27 value')
    X28=st.text_input('Enter the X28 value')
    X29=st.text_input('Enter the X29 value')
    X30=st.text_input('Enter the X30 value')
    X31=st.text_input('Enter the X31 value')
    X32=st.text_input('Enter the X32 value')
    X33=st.text_input('Enter the X33 value')
    X34=st.text_input('Enter the X34 value')
    X35=st.text_input('Enter the X35 value')
    X36=st.text_input('Enter the X36 value')
    X37=st.text_input('Enter the X37 value')
    X38=st.text_input('Enter the X38 value')
    X39=st.text_input('Enter the X39 value')
    X40=st.text_input('Enter the X40 value')
    X41=st.text_input('Enter the X41 value')
    X42=st.text_input('Enter the X42 value')
    X43=st.text_input('Enter the X43 value')
    X44=st.text_input('Enter the X44 value')
    X45=st.text_input('Enter the X45 value')
    X46=st.text_input('Enter the X46 value')
    X47=st.text_input('Enter the X47 value')
    X48=st.text_input('Enter the X48 value')
    X49=st.text_input('Enter the X49 value')
    X50=st.text_input('Enter the X50 value')
    X51=st.text_input('Enter the X41 value')
    X52=st.text_input('Enter the X42 value')
    X53=st.text_input('Enter the X43 value')
    X54=st.text_input('Enter the X44 value')
    X55=st.text_input('Enter the X45 value')
    X56=st.text_input('Enter the X46 value')
    X57=st.text_input('Enter the X47 value')
    X58=st.text_input('Enter the X48 value')
    X59=st.text_input('Enter the X49 value')
    X60=st.text_input('Enter the X50 value')
    
    #code for prediction
    result= ''
    
    #creating a button for prediction
    if st.button('Rock Vs Mine Prediction Result'):
        result= rock_mine_prediction([X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,X24,X25,X26,X27,X28,X29,X30,X31,X32,X33,X34,X35,X36,X37,X38,X39,X40,X41,X42,X43,X44,X45,X46,X47,X48,X49,X50,X51,X52,X53,X54,X55,X56,X57,X58,X59,X60])
    
    st.success(result)
    
if __name__=='__main__':
    main()