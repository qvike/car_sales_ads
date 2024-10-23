import urllib.request
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

data=pd.read_csv('vehicles_us.csv')
st.subheader('Use this app to select a car based on the preferred parameters.')

import urllib.request
from PIL import Image

urllib.request.urlretrieve(
    'https://www.linearity.io/blog/content/images/2023/06/how-to-create-a-car-NewBlogCover.png',
    "gfg.png")

img = Image.open("gfg.png")

st.image(img)

st.caption(':red[Choose your parameters here]')


price_range = st.slider(
     "What is your price range?",
     value=(2, 100000))

actual_range=list(range(price_range[0],price_range[1]+1))

excellent_condition = st.checkbox('Only excellent condition, like new or new')

if excellent_condition:
    filtered_data=data[data.price.isin(actual_range)]
    filtered_data = filtered_data[filtered_data['condition'].isin(['excellent', 'new', 'like new'])]
else:
    filtered_data=data[data.price.isin(actual_range)]


st.write('Here are your options with a split by price and condition')

fig = px.scatter(filtered_data, x="price", y="condition")           
st.plotly_chart(fig)


st.write('Distribution of distnace driven of filtered cars')
fig2 = px.histogram(filtered_data, x="odometer")
st.plotly_chart(fig2)


st.write('Here is the list of recommended cars')
st.dataframe(filtered_data.sample(40))
