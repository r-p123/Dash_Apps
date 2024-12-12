# import the Flask class from the flask module
from flask import Flask, render_template, render_template_string
from dash_apps import Passive_Membrane, Multiple_Inputs
from werkzeug.middleware.dispatcher import DispatcherMiddleware


DASH_APPS_ = {
    '/Passive_Membrane': (Passive_Membrane.init_app, "Passive Membrane App"),
    '/Multiple_Inputs': (Multiple_Inputs.init_app, "Multiple Inputs App")
}

# print("DASH_APPS: ", DASH_APPS_)
# create the application object
flask_app = Flask(__name__)
flask_app.static_folder = 'static'
flask_app.template_folder = 'templates'

with flask_app.app_context():
    dash_mw_input = {}
    list_items = ""

    for url in DASH_APPS_:
        dash_mw_input[url] = DASH_APPS_[url][0](url + "/")
        list_items += "<li><a href=\"" + url + "/\">" + DASH_APPS_[url][1] + "</a></li>\n"
    application = DispatcherMiddleware(flask_app, dash_mw_input)
    
# print("dash_mw_input", dash_mw_input)

@flask_app.route('/')
def load_home():
    # return render_template('home.html')  # render a template
    return render_template_string(f"""
        <h1>Fask Apps</h1>
        <ul>
            {list_items}
        </ul>""")


# gunicorn --bind 0.0.0.0:80 --workers=1 --threads=4 application