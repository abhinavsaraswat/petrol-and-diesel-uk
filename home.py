import streamlit as st 
import pandas as pd 

title = "Petrol and diesel prices"
subheader = "Weekly average UK prices of unleaded petrol and diesel"

st.title(title)
st.subheader(subheader)

fn = r"data/petrol_diesel_prices_uk.csv"
date_colums = ['Date']

@st.cache_data
def read_data(file, date_cols=[]): 
    data = pd.read_csv(file)
    try: 
        for c in date_colums: 
            data[c] = pd.to_datetime(data[c],yearfirst=True)
    except: 
        pass 
    return data 

data = read_data(fn, date_cols=date_colums)

st.header("Data")
st.dataframe(data)


st.header("Chart")

options = list(data.set_index('Date').columns)
selection = st.multiselect('Select one or more options to plot',options)
st.line_chart(data=data, x='Date', y=selection)

source = "Published by Department for Energy Security and Net Zero"

st.text(source)