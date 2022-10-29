# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 02:22:38 2022

@author: SHEHU ALABA RASHEED
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.header('st.write')
st.write('## Dispaly text')
st.write('Hello,*World!* :sun_glasses:')
st.write('## Display number')
st.write(1234)
st.write('## Display DataFrame')
st.write(pd.DataFrame({
                       'first column': [1,2,3,4],
                       'second column': [10, 20, 30, 40]
}))
st.write('# Accept multiple arguement', 'Below is a DataFrame:',
         pd.DataFrame({
                                'first column': [1,2,3,4],
                                'second column': [10, 20, 30, 40]}),
         'Above is a DataFrame')
a = np.random.uniform(-3, 3, size=100)
b = np.random.uniform(-3, 3, size=100)
c= np.random.uniform(-2, 2, size=100)
st.write(px.scatter(x=a, y=b))