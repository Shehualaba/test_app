# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 00:05:59 2022

@author: SHEHU ALABA RASHEED
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Exploratory Data analysis')
st.write("""* This data describes the median house prices in California by districts  
            * Each observation represent a single district  
            * median_house_value represent the median price of house by district    
            **Note:**  
            * The data is from 1995, hence metrics might not generalize to the current time
            * This is just a project to practice web app creation
         """)
data = pd.read_csv('train_set.csv', nrows=1000, index_col=0)
num_data = data.select_dtypes(include='number')
st.subheader('Bar plot of income by ocean_proximity')
fig = px.bar(data_frame=data, y='median_house_value', x = 'ocean_proximity')
st.plotly_chart(fig, use_container_width=True)
choice = st.selectbox('Choose the type of numerical plot',
                      ('Individual Plot', 'Relationship plot'))
if choice == 'Individual Plot':
    st.subheader('Individual Plots')
    nums_data = num_data.drop(columns=['longitude', 'latitude'])
    filter_num = tuple(nums_data.columns)
    num = st.selectbox('Choose the feature to visualize', filter_num)
    box = st.checkbox('Click if you want boxplot as a margin on histogram')
    rug = st.checkbox('Click if you want rug as a margin on histogram')
    violin = st.checkbox('Click if you want violinplot as a margin on histogram')
    if box :
        var = 'box'
        fig_num = px.histogram(data_frame=nums_data, x=num, marginal=var)
        st.plotly_chart(fig_num, use_container_width=True)
    if rug :
        var = 'rug'
        fig_num = px.histogram(data_frame=nums_data, x=num, marginal=var)
        st.plotly_chart(fig_num, use_container_width=True)
    if violin :
        var = 'violin'
        fig_num = px.histogram(data_frame=nums_data, x=num, marginal=var)
        st.plotly_chart(fig_num, use_container_width=True)
    
if choice == 'Relationship plot':
    st.header('Relationship plot')
    st.subheader('Correlation_plot_of_numeric_data')
    fig_1 = px.imshow(num_data.corr(),
                      width=600, height=600, aspect= 'equal')
    st.plotly_chart(fig_1)
    st.subheader('Scatter plot of Total_rooms against Population')
    fig_2 = px.scatter(data, x='total_rooms', y='population',
                           size='median_house_value', color = 'ocean_proximity')
    st.plotly_chart(fig_2, use_container_width=True)
    st.subheader('Location of Houses')
    fig_3 = px.scatter_geo(data,
                           lat = 'latitude',
                           lon = 'longitude',
                           size = 'median_house_value',
                           center= dict(lat=37.2296, lon=-120.0475))
    fig_3.update_layout( geo_scope='usa')
    st.plotly_chart(fig_3, use_container_width=True)
st.subheader('Click button to display summary statistics')
if st.button('Display Summary Statistics Table'):
    summary_table = data.describe(include='all')
    st.dataframe(summary_table)
st.subheader('Click button to get summary of the analysis')
if st.button('Final Summary'):
    st.markdown(
        """
        ## Summary
        * housing_median_age is normally distributed
        * Most of the numeric data are rightly skewed
        * Most of the data are weakly correlated with home price
        * median_income is moderately positively correlated with house_price,
        hences it will be a good predictor of price
        * Although the numeric data are weakly correlated with home price, they are
        highly correlated to each other, this would introduce multicollinearity
        in the model, which isn't good hence the data must be decorrelated before
        modelling
        * It can be seen that house price increase as house get close to the coast
        """)

