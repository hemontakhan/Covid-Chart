import pandas as pd
import plotly.express as px

read = pd.read_csv('Covid Data.csv')
scatter = px.scatter(read,x='date',y='cases',color='country')