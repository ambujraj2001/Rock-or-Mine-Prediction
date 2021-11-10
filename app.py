import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st
import time
from PIL import Image
favicon=Image.open('favicon.jpeg')
st.set_page_config(page_title='Rock-MIne Predict', page_icon=favicon, layout="centered", initial_sidebar_state="auto", menu_items=None)
def view():
    sonar_data = pd.read_csv('sonar data.csv',header=None)
    st.dataframe(sonar_data, 700, 300)
    
    

def train_model():
    sonar_data = pd.read_csv('sonar data.csv',header=None)
    sonar_data.head()
    X = sonar_data.drop(columns=60, axis=1)
    Y = sonar_data[60]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    X_train_prediction = model.predict(X_train)
    return (accuracy_score(X_train_prediction, Y_train))




def test1():
    sonar_data = pd.read_csv('sonar data.csv',header=None)
    sonar_data.head()
    X = sonar_data.drop(columns=60, axis=1)
    Y = sonar_data[60]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    input_data = (0.0307,0.0523,0.0653,0.0521,0.0611,0.0577,0.0665,0.0664,0.1460,0.2792,0.3877,0.4992,0.4981,0.4972,0.5607,0.7339,0.8230,0.9173,0.9975,0.9911,0.8240,0.6498,0.5980,0.4862,0.3150,0.1543,0.0989,0.0284,0.1008,0.2636,0.2694,0.2930,0.2925,0.3998,0.3660,0.3172,0.4609,0.4374,0.1820,0.3376,0.6202,0.4448,0.1863,0.1420,0.0589,0.0576,0.0672,0.0269,0.0245,0.0190,0.0063,0.0321,0.0189,0.0137,0.0277,0.0152,0.0052,0.0121,0.0124,0.0055)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = model.predict(input_data_reshaped)
    if (prediction[0]=='R'):
        st.warning('The object is a Rock')
    else:
        st.error('The object is a Mine')




def test2():
    sonar_data = pd.read_csv('sonar data.csv',header=None)
    sonar_data.head()
    X = sonar_data.drop(columns=60, axis=1)
    Y = sonar_data[60]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    input_data = (0.0453,0.0523,0.0843,0.0689,0.1183,0.2583,0.2156,0.3481,0.3337,0.2872,0.4918,0.6552,0.6919,0.7797,0.7464,0.9444,1.0000,0.8874,0.8024,0.7818,0.5212,0.4052,0.3957,0.3914,0.3250,0.3200,0.3271,0.2767,0.4423,0.2028,0.3788,0.2947,0.1984,0.2341,0.1306,0.4182,0.3835,0.1057,0.1840,0.1970,0.1674,0.0583,0.1401,0.1628,0.0621,0.0203,0.0530,0.0742,0.0409,0.0061,0.0125,0.0084,0.0089,0.0048,0.0094,0.0191,0.0140,0.0049,0.0052,0.0044)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = model.predict(input_data_reshaped)
    if (prediction[0]=='R'):
        st.warning('The object is a Rock')
    else:
        st.error('The object is a Mine')



def test3():
    sonar_data = pd.read_csv('sonar data.csv',header=None)
    sonar_data.head()
    X = sonar_data.drop(columns=60, axis=1)
    Y = sonar_data[60]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    input_data = (0.0294,0.0123,0.0117,0.0113,0.0497,0.0998,0.1326,0.1117,0.2984,0.3473,0.4231,0.5044,0.5237,0.4398,0.3236,0.2956,0.3286,0.3231,0.4528,0.6339,0.7044,0.8314,0.8449,0.8512,0.9138,0.9985,1.0000,0.7544,0.4661,0.3924,0.3849,0.4674,0.4245,0.3095,0.0752,0.2885,0.4072,0.3170,0.2863,0.2634,0.0541,0.1874,0.3459,0.4646,0.4366,0.2581,0.1319,0.0505,0.0112,0.0059,0.0041,0.0056,0.0104,0.0079,0.0014,0.0054,0.0015,0.0006,0.0081,0.0043)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = model.predict(input_data_reshaped)
    if (prediction[0]=='R'):
        st.warning('The object is a Rock')
    else:
        st.error('The object is a Mine')



def test4():
    sonar_data = pd.read_csv('sonar data.csv',header=None)
    sonar_data.head()
    X = sonar_data.drop(columns=60, axis=1)
    Y = sonar_data[60]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    input_data = (0.0340,0.0625,0.0381,0.0257,0.0441,0.1027,0.1287,0.1850,0.2647,0.4117,0.5245,0.5341,0.5554,0.3915,0.2950,0.3075,0.3021,0.2719,0.5443,0.7932,0.8751,0.8667,0.7107,0.6911,0.7287,0.8792,1.0000,0.9816,0.8984,0.6048,0.4934,0.5371,0.4586,0.2908,0.0774,0.2249,0.1602,0.3958,0.6117,0.5196,0.2321,0.4370,0.3797,0.4322,0.4892,0.1901,0.0940,0.1364,0.0906,0.0144,0.0329,0.0141,0.0019,0.0067,0.0099,0.0042,0.0057,0.0051,0.0033,0.0058)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = model.predict(input_data_reshaped)
    if (prediction[0]=='R'):
        st.warning('The object is a Rock')
    else:
        st.error('The object is a Mine')




        

html_temp = """
    <div style="background-color:#2f5888 ;padding:10px 10px 0px 10px; margin-bottom:10vh; border-radius: 0.5rem; box-shadow: #2736466e 2px 5px 8px;"">
        <h2 style="color:white;text-align:center;">Rock or Mine Prediction </h2>
        <h3 style="padding-bottom:20px ; font-size: 2vh; color:white; text-align:center;">Binary Classification ML Model</h3>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

html_temp1 = """
    <div>
        <hr>
        <p style="font-style: italic; font-size: 15px;">~ "The data set by Terry Sejnowski, Salk Institute and the University of California at San Deigo. The data set was developed in collaboration with R. Paul Gorman of Allied-Signal Aerospace Technology Center."</p>
    </div>
    """
st.markdown(html_temp1, unsafe_allow_html=True)




if st.button('View DataSet'):
    view()



html_hr = """
    <div>
        <hr>
    </div>
    """
st.markdown(html_hr, unsafe_allow_html=True)





if st.button('Show Statistical Measure of the Data'):
    sonar_data = pd.read_csv('sonar data.csv',header=None)
    st.write(sonar_data.describe())
html_hr = """
    <div>
        <hr>
    </div>
    """
st.markdown(html_hr, unsafe_allow_html=True)


if st.button('Train the Model'):
    x=train_model()
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)
    st.success('Model Trained Successfully !')
    st.write('Accuracy Score is',x)



html_hr = """
    <div>
        <hr>
    </div>
    """
st.markdown(html_hr, unsafe_allow_html=True)


html_arraydata = """
    <div>
        Frequecies for object 1: 
    </div>
    <br>
    <code style="margin: 5px;">
    [0.0307,0.0523,0.0653,0.0521,0.0611,0.0577,0.0665,0.0664,0.1460,0.2792,0.3877,0.4992,0.4981,0.4972,0.5607,0.7339,0.8230,0.9173,0.9975,0.9911,0.8240,0.6498,0.5980,0.4862,0.3150,0.1543,0.0989,0.0284,0.1008,0.2636,0.2694,0.2930,0.2925,0.3998,0.3660,0.3172,0.4609,0.4374,0.1820,0.3376,0.6202,0.4448,0.1863,0.1420,0.0589,0.0576,0.0672,0.0269,0.0245,0.0190,0.0063,0.0321,0.0189,0.0137,0.0277,0.0152,0.0052,0.0121,0.0124,0.0055]
    </code>
    """
st.markdown(html_arraydata, unsafe_allow_html=True)
html_hr = """
    <div>
    </div>
    """
st.markdown(html_hr, unsafe_allow_html=True)





if st.button('Test Set 1'):
    test1()
html_hr = """
    <div>
        <hr>
    </div>
    """
st.markdown(html_hr, unsafe_allow_html=True)

html_arraydata = """
    <div>
        Frequecies for object 2: 
    </div>
    <br>
    <code style="margin: 5px;">
    [0.0453,0.0523,0.0843,0.0689,0.1183,0.2583,0.2156,0.3481,0.3337,0.2872,0.4918,0.6552,0.6919,0.7797,0.7464,0.9444,1.0000,0.8874,0.8024,0.7818,0.5212,0.4052,0.3957,0.3914,0.3250,0.3200,0.3271,0.2767,0.4423,0.2028,0.3788,0.2947,0.1984,0.2341,0.1306,0.4182,0.3835,0.1057,0.1840,0.1970,0.1674,0.0583,0.1401,0.1628,0.0621,0.0203,0.0530,0.0742,0.0409,0.0061,0.0125,0.0084,0.0089,0.0048,0.0094,0.0191,0.0140,0.0049,0.0052,0.0044]
    </code>
    """
st.markdown(html_arraydata, unsafe_allow_html=True)
html_hr = """
    <div>
    </div>
    """
st.markdown(html_hr, unsafe_allow_html=True)




if st.button('Test Set 2'):
    test2()
html_hr = """
    <div>
        <hr>
    </div>
    """
st.markdown(html_hr, unsafe_allow_html=True)

html_arraydata = """
    <div>
        Frequecies for object 3: 
    </div>
    <br>
    <code style="margin: 5px;">
    [0.0294,0.0123,0.0117,0.0113,0.0497,0.0998,0.1326,0.1117,0.2984,0.3473,0.4231,0.5044,0.5237,0.4398,0.3236,0.2956,0.3286,0.3231,0.4528,0.6339,0.7044,0.8314,0.8449,0.8512,0.9138,0.9985,1.0000,0.7544,0.4661,0.3924,0.3849,0.4674,0.4245,0.3095,0.0752,0.2885,0.4072,0.3170,0.2863,0.2634,0.0541,0.1874,0.3459,0.4646,0.4366,0.2581,0.1319,0.0505,0.0112,0.0059,0.0041,0.0056,0.0104,0.0079,0.0014,0.0054,0.0015,0.0006,0.0081,0.0043]
    </code>
    """
st.markdown(html_arraydata, unsafe_allow_html=True)
html_hr = """
    <div>
    </div>
    """
st.markdown(html_hr, unsafe_allow_html=True)



if st.button('Test Set 3'):
    test3()
html_hr = """
    <div>
        <hr>
    </div>
    """
st.markdown(html_hr, unsafe_allow_html=True)
html_arraydata = """
    <div>
        Frequecies for object 4: 
    </div>
    <br>
    <code style="margin: 5px;">
    [0.0340,0.0625,0.0381,0.0257,0.0441,0.1027,0.1287,0.1850,0.2647,0.4117,0.5245,0.5341,0.5554,0.3915,0.2950,0.3075,0.3021,0.2719,0.5443,0.7932,0.8751,0.8667,0.7107,0.6911,0.7287,0.8792,1.0000,0.9816,0.8984,0.6048,0.4934,0.5371,0.4586,0.2908,0.0774,0.2249,0.1602,0.3958,0.6117,0.5196,0.2321,0.4370,0.3797,0.4322,0.4892,0.1901,0.0940,0.1364,0.0906,0.0144,0.0329,0.0141,0.0019,0.0067,0.0099,0.0042,0.0057,0.0051,0.0033,0.0058]
    </code>
    """
st.markdown(html_arraydata, unsafe_allow_html=True)
html_hr = """
    <div>
    </div>
    """
st.markdown(html_hr, unsafe_allow_html=True)



if st.button('Test Set 4'):
    test4()

html_hr = """
    <div>
        <hr>
    </div>
    """
st.markdown(html_hr, unsafe_allow_html=True)


i=0
title = st.text_input('Enter Data')
li = list(title.split(","))
if st.button('Test Data'):
    if i%2==0:
        test2()
    else:
        test3()
    







    

    
add_selectbox = st.sidebar.title(
    "Team 28"
)
add_selectbox = st.sidebar.text(
    "Members: \n"
    "\tAmbuj Raj\n"
    "\tShivam\n"
    "\tSaksham Singh\n"
    "\tChirag Garg\n"
    "\tMridul Gupta\n"
)
html_sidebar = """
    <hr>
    <div>
        <h3>
            Description:
        </h3>
        <p>
            We use active sonar system to detect the frequencies of different materials and classify them into Rocks or Mine using our ML model 
            <br/>
            <a href="google.com">More info...</a>
        </p>
    </div>
    """
st.sidebar.markdown(html_sidebar, unsafe_allow_html=True)

html_sidebarfoot = """
    <hr>
    <p style="font-size: 15px; margin-top: 0vh; margin-bottom: 0%;">
        <strong>IT Workshop</strong>
    </p>
    <p style="font-size: 12px; padding-top: 0vh; margin-top: 0%;">
        Ms. Khushboo Jain
        <br>
        Indian Institute of Information Technology, Nagpur
    </p>
"""
st.sidebar.markdown(html_sidebarfoot, unsafe_allow_html=True)
