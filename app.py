import streamlit as st, pandas as pd
import matplotlib.pyplot as plt
st.title("Student Performance Dashboard")
f=st.file_uploader("Upload CSV with Name and Marks columns",type="csv")
df=pd.read_csv(f) if f else pd.DataFrame({"Name":["Asha","Ravi","Mina","Arun"],"Marks":[82,67,91,74]})
st.dataframe(df)
if "Marks" in df and "Name" in df:
 df["Marks"]=pd.to_numeric(df["Marks"],errors="coerce")
 st.metric("Average marks",f"{df.Marks.mean():.1f}")
 fig,ax=plt.subplots(); ax.bar(df.Name.astype(str),df.Marks); ax.set_ylabel("Marks"); st.pyplot(fig)
