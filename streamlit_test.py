import pandas as pd
import streamlit as st

data_list = [[1, 2], [2, 3], [3, 4], [4, 5]]
dummy_df = pd.DataFrame(data_list, columns=['a', 'b'])

st.dataframe(dummy_df)