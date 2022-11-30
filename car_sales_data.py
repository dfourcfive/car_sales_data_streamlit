import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

@st.cache
def get_autos_data():
    dcsv = pd.read_csv("data/autos.csv", encoding = 'ISO-8859-1')
    df_filtered = dcsv.set_index('brand').sort_values(by=['price'], ascending=True)
    #converting and sorting the price column
    df_filtered = df_filtered[df_filtered['price'].str.replace('$', '',regex=True).replace(',', '',regex=True).astype(float) > 0]
    df_filtered['price'] = df_filtered['price'].str.replace('$', '',regex=True).replace(',', '',regex=True)
    df_filtered['price'] = pd.to_numeric(df_filtered['price'])
    df_filtered= df_filtered.sort_values(by=['price'])
    #converting the date time column
    df_filtered['dateCrawled'] = pd.to_datetime(df_filtered['dateCrawled'])
    #remove unnecessary columns
    #df_filtered.drop(columns=['dateCrawled','seller','offerType'],axis=1,inplace=True)
    return df_filtered

df = get_autos_data()
df.index.name='brand'

st.title('Cars prices by brand')
cars = st.selectbox(
    "Select a brand",list(np.unique(df.index)),0
)

data = df.loc[cars]
st.write("cars data by brand ", data.sort_index())
#data= data[data['dateCrawled'].str.split(' ')]
dtframe = pd.DataFrame(data)
df_melted = pd.melt(dtframe,id_vars=['price','dateCrawled'])


st.title('Cars prices by date crawled graph')
st.line_chart(df_melted,x='dateCrawled',y='price')