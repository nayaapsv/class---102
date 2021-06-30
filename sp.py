import pandas as py
import plotly_express as px

db = py.read_csv('coviddata.csv')
fig = px.scatter(db, x="date", y="cases", color="country", size_max=30)
fig.show()