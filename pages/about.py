import streamlit as st
import streamlit.components.v1 as components


st.title("About")
st.header("Data source informaton")
info = """
Published by: Department for Energy Security and Net Zero

Data licence: 
Contains public sector information licensed under the Open Government Licence v3.0.
"""

st.markdown(info)