from streamlit_dynamic_filters import DynamicFilters
import streamlit as st
import pandas as pd

st.title("Test")
df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
filters = DynamicFilters(df, filters=['col1', 'col2'])
filters.display_filters()