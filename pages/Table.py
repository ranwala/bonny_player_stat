import streamlit as st
from backend import get_table_data

table_data = get_table_data()

st.title('WDCV Regionalliga West 2025')

st.dataframe(table_data, hide_index=True)