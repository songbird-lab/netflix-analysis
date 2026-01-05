import pandas as pd # used for data preparation
import numpy as np  # used for linear operations
import textblob as TextBlob # used for sentiment analysis
import plotly.express as px  # used for data visualization
from pathlib import Path

# Get the directory where the script lives
BASE_DIR = Path(__file__).parent

# Load the CSV using a relative path, not absolute path.

df = pd.read_csv(BASE_DIR / "netflix_titles.csv")

print(df.shape)

print(df.head())

print(df.columns)

x = df.groupby(['rating']).size().reset_index(name = 'count')

print(x)

pieChart = px.pie(x, values = 'count', names = 'rating', title = 'Distribution of content ratings on Netflix')
pieChart.show()

df['director'] =df['director'].fillna('Director Not Specified') # takes our director column and clean the missing NA values
print(df.head())

directors_list = pd.DataFrame()
print(directors_list) # produces empty dataframe for testing

directors_list = df['director'].str.split(',', expand = True).stack()
print(directors_list)

directors_list = directors_list.to_frame(name = 'director')
directors_list = directors_list.reset_index(drop = True)
print(directors_list)