import pandas as pd
import streamlit as st
import seaborn as sns

# affiche un titre
st.title('Hello Wilders, welcome to my application !')

'''
# affiche une phrase
st.write('I enjoy to discover streamlit possibilities.')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"

df_weather = pd.read_csv(link)

# affiche la table df_weather
df_weather

# affiche le lineplot sur la temperature MAX
st.line_chart(df_weather['MAX_TEMPERATURE_C'])

# met une heatmap dans une variable
viz_correlation = sns.heatmap(df_weather.corr(),
                              center = 0,
                              cmap = sns.color_palette('vlag', as_cmap = True)
                              )

# affiche la variable-heatmap
st.pyplot(viz_correlation.figure)
'''

name = st.text_input('Please give me your name :')
name_length = len(name)
st.write('Your name has ', name_length, 'characters.')

