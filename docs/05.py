import plotly
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

external_stylesheets = [dbc.themes.FLATLY]  # CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)



# Posted On, BHK, Rent, Size,         Floor,      Area Type,   Area Locality,   City,    Furnishing Status, Tenant Preferred, Bathroom, Point of Contact
# 2022-05-18,2.0, 15000,1000. 0,    3 out of 5,  Carpet Area,   Bandam Kommu,  Hyderabad,    Semi-Furnished,Bachelors/Family,    2,      Contact Owner

url = 'https://github.com/DSNote/fastcampus/raw/main/rent.csv'
df = pd.read_csv(url)

app.layout = dbc.Container([
    dcc.Graph(figure=px.box(data_frame=df[df.Rent<20000], y='Rent'))
])

if __name__ == '__main__':
    app.run(debug=True)