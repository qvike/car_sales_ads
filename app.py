import pandas as pd
data = pd.read_csv('vehicles_us.csv')

# Eliminate duplicates in 'model' column
for model in data['model'].unique():
    if "ford f" in model.lower():
        print(model)

for model in data['model'].unique():
    if "ford" in model.lower() and "150" in model.lower():
        print(model)
        
wrong_ford_150 = ['ford f150','ford f150 supercrew cab xlt'] 
correct_ford_150 = 'ford f-150' 

def replace_wrong_ford_150(wrong_ford_150, correct_ford_150):
    for pattern in wrong_ford_150:
        data['model'] = data['model'].str.replace(rf'\b{pattern}\b', correct_ford_150, regex=True)
        
replace_wrong_ford_150(wrong_ford_150, correct_ford_150)

for model in data['model'].unique():
    if "ford" in model.lower() and "150" in model.lower():
        print(model)
        
for model in data['model'].unique():
    if "ford" in model.lower() and "250" in model.lower():
        print(model)
        
wrong_ford_250 = ['ford f250 super duty','ford f250'] 
correct_ford_250 = 'ford f-250' 

def replace_wrong_ford_250(wrong_ford_250, correct_ford_250):
    for pattern in wrong_ford_250:
        data['model'] = data['model'].str.replace(rf'\b{pattern}\b', correct_ford_250, regex=True)
    data['model'] = data['model'].str.replace(r'(?i)super duty', 'sd', regex=True)

replace_wrong_ford_250(wrong_ford_250, correct_ford_250)

for model in data['model'].unique():
    if "ford" in model.lower() and "250" in model.lower():
        print(model)
        
for model in data['model'].unique():
    if "ford" in model.lower() and "350" in model.lower():
        print(model)
        
wrong_ford_350 = ['ford f350 sd','ford f350'] 
correct_ford_350 = 'ford f-350' 

def replace_wrong_ford_350(wrong_ford_350, correct_ford_350):
    for pattern in wrong_ford_350:
        data['model'] = data['model'].str.replace(rf'\b{pattern}\b', correct_ford_350, regex=True)

replace_wrong_ford_350(wrong_ford_350, correct_ford_350)

for model in data['model'].unique():
    if "ford" in model.lower() and "350" in model.lower():
        print(model)
        
print(data['model'].sort_values().unique())

# Replace missing values in column 'paint_color' by 'unknown'
data['paint_color']=data['paint_color'].fillna('unknown')
print(data['paint_color'].unique())

# Create custom function to replace missing 'model_year' by the mean value of the corresponding 'model'
mean_model_year = data.groupby('model')['model_year'].mean().round(1)
print(mean_model_year)

def fill_missing_model_year(row):
    if pd.isna(row['model_year']):
        return mean_model_year.get(row['model'],row['model_year'])
    else:
        return row['model_year']

data['model_year']=data.apply(fill_missing_model_year, axis=1)
print(data['model_year'].isna().sum())

# Replace missing values in column 'cylinders' by '0.0'
data['cylinders']=data['cylinders'].fillna(0.0)
print(data['cylinders'].isna().sum())
print(data['cylinders'].unique())

# Create custom function to replace missing 'odometer' by the mean value of the corresponding 'model'
mean_model_distance = data.groupby('model')['odometer'].mean().round(1)
print(mean_model_distance)

def fill_missing_odometer(row):
    if pd.isna(row['odometer']):
        return mean_model_distance.get(row['model'],row['odometer'])
    else:
        return row['odometer']

data['odometer']=data.apply(fill_missing_odometer, axis=1)
still_missing_odometer=data['odometer'].isna()
print(still_missing_odometer)

odometer_mean=data['odometer'].mean().round(1)
print(odometer_mean)

data.loc[still_missing_odometer, 'odometer'] = odometer_mean
print(data['odometer'].isna().sum())

# Create custom function to replace missing 'is_4wd'
missing_4wd = data['is_4wd'].isna()
print(missing_4wd)
print(data['model'].sort_values().unique())

model_4x4=['bmw x5', 'buick enclave', 'cadillac escalade', 'chevrolet colorado', 'chevrolet equinox', 'chevrolet silverado', 
           'chevrolet silverado 1500', 'chevrolet silverado 2500hd', 'chevrolet silverado 3500hd', 'chevrolet suburban', 
           'chevrolet tahoe', 'chevrolet trailblazer', 'chevrolet traverse', 'dodge dakota', 'ford expedition', 'ford explorer', 
           'ford f-150', 'ford f-250', 'ford f-250 sd', 'ford f-350', 'ford f-350 sd', 'gmc acadia', 'gmc sierra', 'gmc sierra 1500', 
           'gmc sierra 2500hd', 'gmc yukon', 'honda cr-v', 'honda pilot', 'hyundai santa fe', 'jeep cherokee', 'jeep grand cherokee', 
           'jeep grand cherokee laredo', 'jeep liberty', 'jeep wrangler', 'jeep wrangler unlimited', 'kia sorento', 'nissan frontier', 
           'nissan frontier crew cab sv', 'nissan murano', 'nissan rogue', 'ram 1500', 'ram 2500', 'ram 3500', 'subaru forester', 
           'subaru impreza', 'subaru outback', 'toyota 4runner', 'toyota highlander', 'toyota rav4', 'toyota tacoma', 'toyota tundra']

for index, row in data[missing_4wd].iterrows():
    if row['model'] in model_4x4:
        data.at[index, 'is_4wd'] = 1 
    else:
        data.at[index, 'is_4wd'] = 0

print(data[['model', 'is_4wd']].head())

# Remove outliers in price = keep the rows that stay between the price borders
data_filtered = data[(data['price'] >= 1) & (data['price'] <= 100000)]
print(data_filtered)

# Remove outliers in model_year = keep the rows with the year, greater than 1970
data_filtered_year = data[(data['model_year'] >= 1970)] 
print(data_filtered_year)


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
