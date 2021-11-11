#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: hamzafarooq@ MABA CLASS
"""

import streamlit as st

st.title("Jessica Mohr: Assignment 1")
st.markdown("Project Idea:")
st.markdown("My project idea will be a movie recommendor system.")
st.markdown("The user will select 3 movies from a list that they like the most.")
st.markdown("A model will determine which movie they might like best based on these three selections.")
st.markdown("The output will be the model's prediction of which movie the user will like best.")
st.markdown("")
st.markdown("Reflection:")
st.markdown("I was able to install everything and use GitHub Desktop/Atom to edit the streamlit app.")
st.markdown("I also went through the entire Google Cloud Platform tutorial. ")
st.markdown("I don't think I was ever able to get the VisualStudio editor to work but others are working fine instead.")
st.markdown("Also I didn't get any further in the Deploying Streamlit word doc, but from what I understand we are starting that next week.")
st.markdown("What is working for me: github desktop, atom, google cloud platform, streamlitapp.")
st.markdown("")
st.markdown("Santoshi helped to confirm my app deployed properly.")







# EXAMPLE CODE BELOW
import pandas as pd
import plotly.express as px

st.title("Welcome to MABA Class")
st.markdown("This is a demo Streamlit app.")
st.markdown("My name is Jessica, hello world!..")
st.markdown("This is v2")

@st.cache(persist=True)
def load_data():
    df = pd.read_csv("https://datahub.io/machine-learning/iris/r/iris.csv")
    return(df)



def run():
    st.subheader("Iris Data Loaded into a Pandas Dataframe.")

    df = load_data()



    disp_head = st.sidebar.radio('Select DataFrame Display Option:',('Head', 'All'),index=0)



    #Multi-Select
    #sel_plot_cols = st.sidebar.multiselect("Select Columns For Scatter Plot",df.columns.to_list()[0:4],df.columns.to_list()[0:2])

    #Select Box
    #x_plot = st.sidebar.selectbox("Select X-axis Column For Scatter Plot",df.columns.to_list()[0:4],index=0)
    #y_plot = st.sidebar.selectbox("Select Y-axis Column For Scatter Plot",df.columns.to_list()[0:4],index=1)


    if disp_head=="Head":
        st.dataframe(df.head())
    else:
        st.dataframe(df)
    #st.table(df)
    #st.write(df)


    #Scatter Plot
    fig = px.scatter(df, x=df["sepallength"], y=df["sepalwidth"], color="class",
                 size='petallength', hover_data=['petalwidth'])

    fig.update_layout({
                'plot_bgcolor': 'rgba(0, 0, 0, 0)'})

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

    st.write("\n")
    st.subheader("Scatter Plot")
    st.plotly_chart(fig, use_container_width=True)


    #Add images
    #images = ["<image_url>"]
    #st.image(images, width=600,use_container_width=True, caption=["Iris Flower"])





if __name__ == '__main__':
    run()
