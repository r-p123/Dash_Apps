from dash import Dash, html, dcc, Input, Output
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc



def init_app(url_path):
    app = Dash(requests_pathname_prefix = url_path, external_stylesheets=[dbc.themes.SPACELAB])
    app.title = "Multiple Input Currents App"

    heading = html.H4(
        "Multiple Input Currents", className="bg-primary text-white p-2"
    )


    thresh = html.Div(
        [
            dbc.Label("Threshold (mV)", html_for="thresh"),
            dcc.Slider(-65, -52, value=-54, marks = {-65:'-65', -52:'-52mV'}, id="thresh",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )



    control_panel_C0 = dbc.Card([
            dbc.CardBody("Adjust the threshold here, as well as the input current in the below 3 subplots to see the effects on the postsynaptic potential", className="", style={'display':'flex', 'align-items':'center', 'justify-content':'center'} ),
            dbc.CardBody(
                [thresh],
                className="bg-light",
            )
            
        ],
        style={"height": "15rem", "font-size":12, "border":0}
    )

    graph_C0 = dbc.Card(
        [html.Div(id="error_msg0", className="text-danger"), dcc.Graph(id="graph0")],
        style={"border":0}
    )

    start_C1 = html.Div(
        [
            dbc.Label("Start time (ms)", html_for="start_C1"),
            dcc.Slider(1, 800, value=100, marks = {1:'1', 500:'500ms'}, id="start_C1",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )


    duration_C1 = html.Div(
        [
            dbc.Label("Duration (ms)", html_for="duration_C1"),
            dcc.Slider(1, 400, value=100, marks = {1:'1', 400:'400ms'}, id="duration_C1",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )


    amplitude_C1 = html.Div(
        [
            dbc.Label("Amplitude", html_for="amplitude_C1"),
            dcc.Slider(-400, 400, value=100, marks = {-400:'-400', 400:'400nA'}, id="amplitude_C1",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )


    control_panel_C1 = dbc.Card([
            # dbc.CardBody("Input A", className="", style={'display':'flex', 'align-items':'center', 'justify-content':'center'} ),
            dbc.CardBody(
                [start_C1, duration_C1, amplitude_C1],
                className="bg-light",
            )
            
        ],
        style={"height": "15rem", "font-size":12, "border":0}
    )

    graph_C1 = dbc.Card(
        [html.Div(id="error_msg1", className="text-danger"), dcc.Graph(id="graph1")],
        style={"border":0}
    )

    start_C2 = html.Div(
    [
        dbc.Label("Start time (ms)", html_for="start_C2"),
        dcc.Slider(1, 800, value=250, marks = {1:'1', 500:'500ms'}, id="start_C2",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
    )


    duration_C2 = html.Div(
        [
            dbc.Label("Duration (ms)", html_for="duration_C2"),
            dcc.Slider(1, 400, value=100, marks = {1:'1', 400:'400ms'}, id="duration_C2",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )


    amplitude_C2 = html.Div(
        [
            dbc.Label("Amplitude", html_for="amplitude_C2"),
            dcc.Slider(-400, 400, value=100, marks = {-400:'-400', 400:'400nA'}, id="amplitude_C2",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )


    control_panel_C2 = dbc.Card([
            # dbc.CardBody("Input A", className="", style={'display':'flex', 'align-items':'center', 'justify-content':'center'} ),
            dbc.CardBody(
                [start_C2, duration_C2, amplitude_C2],
                className="bg-light",
            )
            
        ],
        style={"height": "15rem", "font-size":12, "border":0}
    )

    graph_C2 = dbc.Card(
        [html.Div(id="error_msg2", className="text-danger"), dcc.Graph(id="graph2")],
        style={"border":0}
    )


    start_C3 = html.Div(
    [
        dbc.Label("Start time (ms)", html_for="start_C3"),
        dcc.Slider(1, 800, value=400, marks = {1:'1', 500:'500ms'}, id="start_C3",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
    )


    duration_C3 = html.Div(
        [
            dbc.Label("Duration (ms)", html_for="duration_C3"),
            dcc.Slider(1, 400, value=100, marks = {1:'1', 400:'400ms'}, id="duration_C3",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )


    amplitude_C3 = html.Div(
        [
            dbc.Label("Amplitude", html_for="amplitude_C3"),
            dcc.Slider(-400, 400, value=100, marks = {-400:'-400', 400:'400nA'}, id="amplitude_C3",
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ],
        className="mt-2",
    )


    control_panel_C3 = dbc.Card([
            # dbc.CardBody("Input A", className="", style={'display':'flex', 'align-items':'center', 'justify-content':'center'} ),
            dbc.CardBody(
                [start_C3, duration_C3, amplitude_C3],
                className="bg-light",
            )
            
        ],
        style={"height": "15rem", "font-size":12, "border":0}
    )

    graph_C3 = dbc.Card(
        [html.Div(id="error_msg3", className="text-danger"), dcc.Graph(id="graph3")],
        style={"border":0}
    )


    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    app.layout = html.Div(
        [heading,
        dbc.Row([ dbc.Col(md=2), dbc.Col(control_panel_C0, md=3), dbc.Col(graph_C0, md=7), dbc.Col(md=1)]),
        html.Hr(style={'borderWidth': "0rem", "color": "black"}),
        dbc.Row([ dbc.Col(md=2), dbc.Col(control_panel_C1, md=3), dbc.Col(graph_C1, md=7), dbc.Col(md=1)]),
        html.Hr(style={'borderWidth': "0rem", "color": "black"}),
        dbc.Row([ dbc.Col(md=2), dbc.Col(control_panel_C2, md=3), dbc.Col(graph_C2, md=7), dbc.Col(md=1)]),
        html.Hr(style={'borderWidth': "0rem", "color": "black"}),
        dbc.Row([ dbc.Col(md=2), dbc.Col(control_panel_C3, md=3), dbc.Col(graph_C3, md=7), dbc.Col(md=1)]), html.Div()
        ]
    )
    init_callbacks(app)
    return app.server



##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# @app.callback(
#     Output("graph0", "figure"),
#     Output("error_msg0", "children"),
#     Input("start_C1", "value"),
#     Input("duration_C1", "value"),
#     Input("amplitude_C1", "value"),
#     Input("start_C2", "value"),
#     Input("duration_C2", "value"),
#     Input("amplitude_C2", "value"),
#     Input("start_C3", "value"),
#     Input("duration_C3", "value"),
#     Input("amplitude_C3", "value"),
#     Input("thresh", "value"),
# )

def init_callbacks(app):
    app.callback(   Output("graph0", "figure"),
                    Output("graph1", "figure"),
                    Output("graph2", "figure"),
                    Output("graph3", "figure"),

                    Input("thresh", "value"),
                    Input("start_C1", "value"),
                    Input("duration_C1", "value"),
                    Input("amplitude_C1", "value"),
                    Input("start_C2", "value"),
                    Input("duration_C2", "value"),
                    Input("amplitude_C2", "value"),
                    Input("start_C3", "value"),
                    Input("duration_C3", "value"),
                    Input("amplitude_C3", "value")           
    )(update_graph)

#postsynaptic cell response to three different current inputs

def update_graph(thresh, start_C1, duration_C1, amplitude_C1, start_C2, duration_C2, amplitude_C2, start_C3, duration_C3, amplitude_C3):

    Cm = 100
    Vm = -65
    Rm = 0.10
    reset = -75
    Tmax = 500   #1 seconds
    dt = 0.1   # 1 millisecond time step
    t = np.arange(0, Tmax, dt)

    V = np.zeros(t.size)
    V[0] = -65
   
    for i in range(0, t.size-1):
        I1 = amplitude_C1 if start_C1<=i<=start_C1+duration_C1 else 0
        I2 = amplitude_C2 if start_C2<=i<=start_C2+duration_C2 else 0
        I3 = amplitude_C3 if start_C3<=i<=start_C3+duration_C3 else 0
        I = (I1+I2+I3)
        V[i+1] = V[i] + dt*(   -(V[i] - Vm)/Rm + I   )/Cm
        if V[i+1] >= thresh:
            V[i+1] = reset
    fig = px.line(V)
    
    fig.update_layout(showlegend=False, title_text='', title_x=0.5,
        xaxis=dict( 
            title=dict(
                text="Time (ms)"
            )
        ),
        yaxis=dict(
            title=dict(
                text="Current A (nA)"
            )
        ),
        font=dict(
            # family="Courier New, monospace",
            size=12,
        )
    )
    fig.update_xaxes(range=[0, 1000])
    fig.update_yaxes(range=[-80, -40])
    fig.update_layout(height=16*15, width=600)
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    fig.add_vrect(x0=start_C1, x1=start_C1+duration_C1, 
              annotation_text="A", annotation_position="top left",
              fillcolor="red", opacity=0.25, line_width=0)
    fig.add_vrect(x0=start_C2, x1=start_C2+duration_C2, 
              annotation_text="B", annotation_position="top left",
              fillcolor="green", opacity=0.25, line_width=0)
    fig.add_vrect(x0=start_C3, x1=start_C3+duration_C3, 
              annotation_text="C", annotation_position="top left",
              fillcolor="blue", opacity=0.25, line_width=0)
    fig.add_hline(y=thresh, line_dash="dot",
              annotation_text="thresh", 
              annotation_position="bottom right")
    fig1 = update_graphC1(start_C1, duration_C1, amplitude_C1)
    fig2 = update_graphC2(start_C2, duration_C2, amplitude_C2)
    fig3 = update_graphC3(start_C3, duration_C3, amplitude_C3)

    return fig, fig1, fig2, fig3

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def init_callbacks(app):
#     app.callback(   Output("graph1", "figure"),
#                     Output("error_msg1", "children"),
#                     Input("start_C1", "value"),
#                     Input("duration_C1", "value"),
#                     Input("amplitude_C1", "value")
#     )(update_graphC1)


# @app.callback(
#     Output("graph1", "figure"),
#     Output("error_msg1", "children"),
#     Input("start_C1", "value"),
#     Input("duration_C1", "value"),
#     Input("amplitude_C1", "value"),
# )
def update_graphC1(start_C1, duration_C1, amplitude_C1):

    Tmax = 1   #1 seconds
    dt = 0.001   # 1 millisecond time step
    t = np.arange(0, Tmax, dt)

    I = np.zeros(t.size)
 
   
    for i in range(0, t.size-1):
        if start_C1<=i<=start_C1+duration_C1:
            I[i] = amplitude_C1
        else:
            I[i] = 0
    fig = px.line(I)
    
    fig.update_layout(showlegend=False, title_text='', title_x=0.5,
        xaxis=dict( 
            title=dict(
                text="Time (ms)"
            )
        ),
        yaxis=dict(
            title=dict(
                text="Current A (nA)"
            )
        ),
        font=dict(
            # family="Courier New, monospace",
            size=12,
        )
    )
    fig.update_xaxes(range=[0, 1000])
    fig.update_yaxes(range=[-400, 400])
    fig.update_layout(height=16*15, width=600)
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    # fig.update_layout(margin=dict(l=0,r=0,b=0,t=0))
    fig.add_vrect(x0=start_C1, x1=start_C1+duration_C1, 
              annotation_text="A", annotation_position="top left",
              fillcolor="red", opacity=0.25, line_width=0)
    return fig

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# def init_callbacks(app):
#     app.callback(   Output("graph2", "figure"),
#                     Output("error_msg2", "children"),
#                     Input("start_C2", "value"),
#                     Input("duration_C2", "value"),
#                     Input("amplitude_C2", "value")
#     )(update_graphC2)


# @app.callback(
#     Output("graph2", "figure"),
#     Output("error_msg2", "children"),
#     Input("start_C2", "value"),
#     Input("duration_C2", "value"),
#     Input("amplitude_C2", "value"),
# )
def update_graphC2(start_C2, duration_C2, amplitude_C2):

    Tmax = 1   #1 seconds
    dt = 0.001   # 1 millisecond time step
    t = np.arange(0, Tmax, dt)

    I = np.zeros(t.size)
 
   
    for i in range(0, t.size-1):
        if start_C2<=i<=start_C2+duration_C2:
            I[i] = amplitude_C2
        else:
            I[i] = 0
    fig = px.line(I)
    
    fig.update_layout(showlegend=False, title_text='', title_x=0.5,
        xaxis=dict( 
            title=dict(
                text="Time (ms)"
            )
        ),
        yaxis=dict(
            title=dict(
                text="Current B (nA)"
            )
        ),
        font=dict(
            # family="Courier New, monospace",
            size=12,
        )
    )
    fig.update_xaxes(range=[0, 1000])
    fig.update_yaxes(range=[-400, 400])
    fig.update_layout(height=16*15, width=600)
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    fig.add_vrect(x0=start_C2, x1=start_C2+duration_C2, 
              annotation_text="B", annotation_position="top left",
              fillcolor="green", opacity=0.25, line_width=0)
    return fig



##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# def init_callbacks(app):
#     app.callback(   Output("graph2", "figure"),
#                     Output("error_msg2", "children"),
#                     Input("start_C2", "value"),
#                     Input("duration_C2", "value"),
#                     Input("amplitude_C2", "value")
#     )(update_graphC3)


# @app.callback(
#     Output("graph3", "figure"),
#     Output("error_msg3", "children"),
#     Input("start_C3", "value"),
#     Input("duration_C3", "value"),
#     Input("amplitude_C3", "value"),
# )

def update_graphC3(start_C3, duration_C3, amplitude_C3):

    Tmax = 1   #1 seconds
    dt = 0.001   # 1 millisecond time step
    t = np.arange(0, Tmax, dt)

    I = np.zeros(t.size)
 
   
    for i in range(0, t.size-1):
        if start_C3<=i<=start_C3+duration_C3:
            I[i] = amplitude_C3
        else:
            I[i] = 0
    fig = px.line(I)
    
    fig.update_layout(showlegend=False, title_text='', title_x=0.5,
        xaxis=dict( 
            title=dict(
                text="Time (ms)"
            )
        ),
        yaxis=dict(
            title=dict(
                text="Current C (nA)"
            )
        ),
        font=dict(
            # family="Courier New, monospace",
            size=12,
        )
    )
    fig.update_xaxes(range=[0, 1000])
    fig.update_yaxes(range=[-400, 400])
    fig.update_layout(height=16*15, width=600)
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    fig.add_vrect(x0=start_C3, x1=start_C3+duration_C3, 
              annotation_text="C", annotation_position="top left",
              fillcolor="blue", opacity=0.25, line_width=0)
    return fig

# if __name__ == "__main__":
#     app.run_server(debug=True)

