import pandas as pd
import plotly.express as px
df = pd.read_csv("data@.csv")
height = df["Height"].tolist()
weight = df["Weight"].tolist()
fig = px.scatter(x=height, y=weight)
fig.show()
