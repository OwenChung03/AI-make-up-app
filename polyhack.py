import streamlit as st
import numpy as np
import time
import pandas as pd
import plotly.express as px
import base64
import matplotlib.pyplot as plt
import seaborn as sns
name_dict = {
    'Name' : ['Company A', 'Company B', 'Company C', 'Company D'],
    'Score' : [90, 80, 95, 20]
}

df = pd.DataFrame(name_dict)


st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2020))))


st.set_page_config(
    page_title = 'Real-Time FairTrade Dashboard',
    page_icon = 'polyhack_logo.png',
    layout = 'wide'
)
st.title("Free Trade Dashboard in stations")

company_filter = st.select("Select the job", pd.unique(df['job']))

placeholder = st.empty()
df = df[df['job'] == company_filter]
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df.to_csv('output.csv', index = False)
    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize = (7, 5))
        ax = sns.heatmap(corr, mask = mask, vmax = 1, square = True)
st.pyplot()
for seconds in range(200):
    df['bean_price'] = df['bean_price'] * np.random.choice*(range(1,5))
    df['Trade_rating'] = df['Trade_rating'] * np.random.choice(range(1,5))
    avg_price = np.mean(df['bean_price'])
    count_of_violation = int(df[df["Natural Language Processor"] == "Natural Language Processor"]).count() + np.random(1,5)
    avg_rating = np.mean(df['Trade_Rating'])
quantity = input("Input the quantity: ")
with placeholder.container():
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label = "average bean price", value = round(avg_price), delta = round(avg_price) - 10)
    kpi2.metric(label = "average rating", value = round(avg_rating), delta = round(avg_rating) - 10)
    kpi3.metric(label = "Your return", value = round(avg_price)* quantity, delta = round(avg_price)* quantity - 10)
    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        st.markdown("### First Chart")
        fig = px.densiy_heatmap(data_frame = df, y = 'new_price', x = 'Rating')
        st.write(fig)
    with fig_col2:
        st.markdown("### Second chart")
        fig2 = px.histogram(data_frame = df, x = 'new_price')
        st.write(fig2)
    st.markdown("### Detailed Data View")
    st.dataframe(df)
    time.sleep(1)



