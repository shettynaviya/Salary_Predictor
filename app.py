import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from pathlib import Path
from plotly import graph_objs as go
from PIL import Image
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv("Salary_Data.csv")
x = np.array(data['YearsExperience']).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data['Salary']))


st.title("Salary Predictor")

nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])
if nav == "Home":
    img_path = Path(__file__).parent / "data" / "sal.jpg"
    img = Image.open(img_path)
    st.image(img, use_container_width=True)
    if st.checkbox("Show Table"):
        st.table(data)

    graph = st.selectbox("What kind of Graph ?", ["Non-Interactive", "Interactive"])
    
    val = st.slider("Filter data using years",0,20)
    data = data.loc[data["YearsExperience"]>= val]
    if graph == "Non-Interactive":
        fig, ax = plt.subplots(figsize=(10,5))
        ax.scatter(data["YearsExperience"], data["Salary"])
        ax.set_ylim(0)
        ax.set_xlabel("Years of Experience")
        ax.set_ylabel("Salary")
        st.pyplot(fig)

    if graph == "Interactive":
        layout = go.Layout(
            xaxis = dict(range=[0,16]),
            yaxis = dict(range =[0,210000])
        )
        fig = go.Figure(data=go.Scatter(x=data["YearsExperience"],y=data["Salary"],mode="markers"),
                        layout = layout)
        st.plotly_chart(fig)

if nav == "Prediction":
    st.header("Know Your Salary")
    val = st.number_input("Enter Your Experience",0.00,20.00,step = 0.25)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your Predicted Salary is {round(pred)}")

if nav == "Contribute":
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter Your Experience",0.0,20.0)
    sal = st.number_input("Enter Your Salary",0.00,1000000.00,step = 1000.0)
    if st.button("Submit"):
        to_add = pd.DataFrame({"YearsExperience":[ex], "Salary":[sal]})
        to_add.to_csv("Salary_Data.csv", mode="a",header=False,index=False)
        st.success("Submitted")

        data = pd.read_csv("Salary_Data.csv")
        st.table(data.tail())