import csv
import pandas as pd
import plotly.figure_factory as ff
import scipy
import plotly_express
df = pd.read_csv('data.csv')
data=df['Mobile Brand'].tolist()
fig = ff.create_distplot([data],['Avg Rating'],show_hist=False)
fig.show()