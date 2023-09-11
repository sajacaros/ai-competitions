import plotly
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.FLATLY]  # CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

# https://vincentarelbundock.github.io/Rdatasets/doc/reshape2/tips.html
# 'total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'
#     16.99     1.01   Female    No      Sun   Dinner    2
df = plotly.data.tips()

@callback(
    Output(component_id='bar_graph', component_property='figure'),
    Input(component_id='radio_input', component_property='value')
)
def select_smoker(is_smoker):
    return px.histogram(
        data_frame=df[df['smoker'] == is_smoker],
        x='day',
        y='tip',
        color='sex',
        barmode='group',
        histfunc='avg'
    )


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Row([
            dbc.RadioItems(id='radio_input', options={'Yes': 'smoker', 'No': 'non smoker'}, inline=True, value='No')
        ]), width=2),
        dbc.Col(dbc.Row([
            dcc.Graph(id='bar_graph', figure={})
        ]), width=10),
    ])

    # seaborn
    # data, x, y, hue
    # plotly
    # data_frame, x, y, color
    # dcc.Graph(figure=px.histogram(
    #     data_frame=df,
    #     x='day',
    #     y='tip',
    #     color='sex',
    #     barmode='group',
    #     histfunc='avg'
    # ))
], style={'backgroundColor':'yellow'}, fluid=True)

if __name__ == '__main__':
    app.run(debug=True)
