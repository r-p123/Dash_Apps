from dash import Dash, html, dcc, Input, Output
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc




def init_app(url_path):
    app = Dash(requests_pathname_prefix = url_path, external_stylesheets=[dbc.themes.SPACELAB])
    app.title = "Passive Membrane Equation"

    # heading = html.H4(
    #     "Passive Membrane Equation", className="bg-primary text-white p-2"
    # )


    membrane_capacitance = html.Div(
        [
            dbc.Label("Membrane Capacitance (pF)", html_for="mem_cap"),
            dcc.Slider(0, 5, value=2, id="mem_cap",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )


    initial_voltage = html.Div(
        [
            dbc.Label("Initial Voltage (mV)", html_for="init_v"),
            dcc.Slider(-80, -40, value=-65, id="init_v",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )


    resistance = html.Div(
        [
            dbc.Label("Resistance (M" + u"\u03a9" + ")", html_for="res"),
            dcc.Slider(0, 1, value=0.25, id="res",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )


    current = html.Div(
        [
            dbc.Label("Current (nA)", html_for="curr"),
            dcc.Slider(0, 100, value=50, id="curr",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )


    control_panel = dbc.Card([
            dbc.CardBody("Use the below sliders to experiment with different parameters. How can you make the trace flat?", className="bg-light"),
            dbc.CardBody(
                [membrane_capacitance, initial_voltage, resistance, current],
                className="bg-light",
            )
        ]
    )

    graph = dbc.Card(
        [dcc.Graph(id="graph")]
    )

    app.layout = html.Div(
        [
        dbc.Row([ dbc.Col(md=2), dbc.Col(control_panel, md=3), dbc.Col(graph, md=5), dbc.Col(md=1)]),
        ]
    )
    init_callbacks(app)
    return app.server



# @app.callback(
#     Output("graph", "figure"),
#     Output("error_msg", "children"),
#     Input("mem_cap", "value"),
#     Input("init_v", "value"),
#     Input("res", "value"),
#     Input("curr", "value"),
# )

def init_callbacks(app):
    app.callback(   
        Output("graph", "figure"),
        Input("mem_cap", "value"),
        Input("init_v", "value"),
        Input("res", "value"),
        Input("curr", "value")        
    )(update_graph)

def update_graph(mem_cap, init_v, res, curr):

    # Cm = 200*1e-12 #picoFarads
    # Vm = -0.065     #milliVolts
    # Rm = 4*10e6     #MegaOhms
    # I = 1*10e-9     #nanoAmperes

    Cm = mem_cap
    Vm = init_v
    Rm = res #0.25
    I = curr

    Tmax = 5   #500 ms
    dt = 0.001   # 1 millisecond time step
    t = np.arange(0, Tmax, dt)

    V = np.zeros(t.size)
    V[0] = -65
   
    for i in range(0, t.size-1):
        #v[i+1] = v[i] + dt*function
        V[i+1] = V[i] + dt*(   -(V[i] - Vm)/Rm + I   )/Cm
    fig = px.line(V)
    
    fig.update_layout(showlegend=False, title_text='Voltage Trace', title_x=0.5,
    xaxis=dict( 
        title=dict(
            text="Time (ms)"
        )
    ),
    yaxis=dict(
        title=dict(
            text="Voltage (mV)"
        )
    ),
    font=dict(
        # family="Courier New, monospace",
        size=12,
    )
    )
    return fig

