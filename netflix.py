import pandas as pd # used for data preparation
import numpy as np  # used for linear operations
import textblob as TextBlob # used for sentiment analysis
import plotly.express as px  # used for data visualization

df = pd.read_csv(r"C:\Users\songb\Documents\pythonscripts\netflix-analysis\netflix_titles.csv")

print(df.shape)

print(df.head)

print(df.columns)

x = df.groupby(['rating']).size().reset_index(name = 'count')

print(x)

pieChart = px.pie(x, values = 'count', names = 'rating', title = 'Distribution of content ratings on Netflix')
pieChart.show()

df['director'] =df['director'].fillna('Director Not Specified')
df.head()

# 11:44 approximate timestamp in video at https://www.youtube.com/watch?v=1ZftU-eU4VA&t=555s