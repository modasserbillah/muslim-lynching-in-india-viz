
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash("Muslim Lynchings in India")
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
df = pd.read_csv('Lynchings.csv')

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Img(src="http://tribune-intl.com/wp-content/uploads/2016/03/india-executions.jpg",
                style={
                    'height': '250px',
                    'float': 'right',
                    'position': 'relative',
                    'bottom': '-10px'

}),
    html.H1(children='Mob attacks and Lynchings on Muslims in India',
            style={
            'textAlign': 'center',
            'color': colors['text']
        }),
        html.Div(children='Hover mouse on map markers to get specific event details. Zoom in to get clearer view.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Div(id='text-content'),
    dcc.Graph(id='map', figure={
        'data': [{
            'lat': df['Lat'],
            'lon': df['Long'],
            'name': df['Victim'],
            'marker': {
                'color': 'red',
                'size': 15,
                'opacity': 0.6
            },
            'customdata': df['Serial'],
            'type': 'scattermapbox'
        }],
        'layout': {
            'mapbox': {
                'accesstoken': 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3MDBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw'
            },
            'hovermode': 'closest',
            'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}
        }
    })
])

@app.callback(
    dash.dependencies.Output('text-content', 'children'),
    [dash.dependencies.Input('map', 'hoverData')])
def update_text(hoverData):
    s = df[df['Serial'] == hoverData['points'][0]['customdata']]
    return html.Div([
    html.H2('Victim(s): {}'.format(s.iloc[0]['Victim']),
                style={
                    'position': 'relative',
                    'top': '0px',
                    'left': '10px',
                    'font-family': 'Dosis',
                    'display': 'inline',
                    'font-size': '4.0rem',
                    'color': '#4D637F'
}),
html.Br(),
    html.H3(
        'Killed in {}.'.format(
            s.iloc[0]['Place']),
            style={
                    'position': 'relative',
                    'top': '0px',
                    'left': '10px',
                    'font-family': 'Dosis',
                    'display': 'inline',
                    'font-size': '3.0rem',
                    'color': '#4D637F'
}),
html.Br(),
    html.H2('{}'.format(s.iloc[0]['Description']),
                style={
                    'position': 'relative',
                    'top': '0px',
                    'left': '10px',
                    'font-family': 'Dosis',
                    'display': 'inline',
                    'font-size': '3.0rem',
                    'color': '#4D637F'
}),
html.Br(),
    html.A('News Link',
            href=s.iloc[0]['Link to News'],
            target="_blank",
            style={
                'position': 'relative',
                'top': '0px',
                'left': '10px',
                'font-family': 'Dosis',
                'display': 'inline',
                'font-size': '3.0rem',
                'color': 'blue'
            })
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
