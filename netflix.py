# Import Libraries and Data

import pandas as pd # used for data preparation
import numpy as np  # used for linear operations
import textblob as TextBlob # used for sentiment analysis
import plotly.express as px  # used for data visualization
from pathlib import Path # used to set relative paths

# Get the directory where the script lives
BASE_DIR = Path(__file__).parent

# Load the CSV using a relative path, not absolute path.

df = pd.read_csv(BASE_DIR / "netflix_titles.csv")

# Checking shape, columns and rows of data

print(df.shape)

print(df.head())

print(df.columns)

x = df.groupby(['rating']).size().reset_index(name = 'count')

print(x)

# Visualizing the Data

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

directors_list.columns = ['Director'] # Naming the column
print(directors_list)

directors = directors_list.groupby(['Director']).size().reset_index(name = 'Total Count') 
print(directors)

directors = directors[directors.Director != 'Director Not Specified'] # removes some rows for clarity
print(directors)

directors = directors.sort_values(by = ['Total Count'], ascending = False)
print(directors)

top5Directors = directors.head()
print(top5Directors)

top5Directors = top5Directors.sort_values(by = ['Total Count'])
barChart = px.bar(top5Directors, x = 'Total Count', y = 'Director', title = 'Top 5 Directors on Netflix')
barChart.show()

df['cast'] = df['cast'].fillna('No cast specified')
cast_df = pd.DataFrame()
cast_df = df['cast'].str.split(",", expand = True).stack()
cast_df = cast_df.to_frame()
cast_df.columns = ['Actor']
actors = cast_df.groupby(['Actor']).size().reset_index(name = 'Total Count')
actors = actors[actors.Actor != 'No cast specified']
actors = actors.sort_values(by = ['Total Count'], ascending = False)
top5Actors = actors.head()
top5Actors = top5Actors.sort_values(by = ['Total Count'])
barChart2 = px.bar(top5Actors, x = 'Total Count', y = 'Actor', title = 'Top 5 Actors on Netflix')
barChart2.show()

# 31:06