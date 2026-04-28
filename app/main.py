import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data


#Load data

df = load_data()

#title for the app

st.title("Africa Climate Change Dashboard (COP32 Analysis)")


#sidebar Filters

countries = st.sidebar.multiselect(
    "Select Countries",
    df["Country"].unique(),
    default=df["Country"].unique()
)


year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["YEAR"].min()),
    int(df["YEAR"].max()),
    (2015, 2026)
)


variable = st.sidebar.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)


#filter data

filtered_df = df[
    (df["Country"].isin(countries)) &
    (df["YEAR"].between(year_range[0], year_range[1]))
]

#Temperature Trend Line Chart

st.subheader("Temperature Trend")

temp_trend = filtered_df.groupby(["YEAR", "Country"])["T2M"].mean().reset_index()

fig, ax = plt.subplots()

for c in countries:
    data = temp_trend[temp_trend["Country"] == c]
    ax.plot(data["YEAR"], data["T2M"], label=c)

ax.set_xlabel("Year")
ax.set_ylabel("Temperature")
ax.legend()

st.pyplot(fig)


#percipiation Boxplot

st.subheader("Precipitation Distribution")

fig, ax = plt.subplots()
sns.boxplot(x="Country", y="PRECTOTCORR", data=filtered_df, ax=ax)

st.pyplot(fig)


#Variable Visualization

st.subheader(f"{variable} Trend")

var_data = filtered_df.groupby(["YEAR", "Country"])[variable].mean().reset_index()

fig, ax = plt.subplots()

for c in countries:
    data = var_data[var_data["Country"] == c]
    ax.plot(data["YEAR"], data[variable], label=c)

ax.legend()
st.pyplot(fig)