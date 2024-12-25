import streamlit as st
import pandas as pd

st.write("AVD 22yuygchguiu")

data = {
    "Task": ["Extract", "Transform", "Load"],
    "Status" : ["Completed", "InProgress", "Pending"]
}

df = pd.DataFrame(data)
st.write("ETL Pipeline")
st.write(df)
