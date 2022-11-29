import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

@st.cache
def get_autos_data():
    dcsv = pd.read_csv("data/autos.csv", encoding = 'ISO-8859-1')
    df_filtered = dcsv.set_index('brand').sort_values(by=['price'], ascending=True)
    df_filtered = df_filtered[df_filtered['price'].str.replace(r'\D', '').astype(float) > 0]
    #remove unnecessary columns
    df_filtered.drop(columns=['dateCrawled','seller','offerType'],axis=1,inplace=True)
    return df_filtered

df = get_autos_data()
st.title('Cars prices by brand')
cars = st.selectbox(
    "Select a brand",list(np.unique(df.index)),0
)

data = df.loc[cars]
st.write("cars data by brand ", data.sort_index())