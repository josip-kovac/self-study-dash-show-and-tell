from dash import Dash, html, dcc, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate

# custom components
from data import get_data
from footer import get_footer
from graphs import plot_total, plot_year, plot_subject
from comments import dict_additional_info
from navbar import navbar

# plotly
import plotly.graph_objects as go
import plotly.express as px

# call once
df = get_data()
df_max_date = df["Date"].max()

# Intro Markdown

intro_markdown = dcc.Markdown(f"""
This is the summary of my Self-Study Journey, **after** I've attained my Master's degree (2017).

My study methodology involves using the [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique), with the use of noise cancelling headphones, along with some good old [static noise](https://www.youtube.com/watch?v=FcWgjCDPiP4) or deep ambient music. Long time follower of [deep work](https://www.amazon.com/Deep-Work-Focused-Success-Distracted/dp/1455586692). 👨🏻‍💻 🎧 ☕

The data below consists mainly of books and personal development of code libraries that I use in my day-to-day life.

Last update of data was on {df_max_date:%Y-%m-%d}.

""")

intro_current_focus = dcc.Markdown(f"For more info about past years, select from the dropdown menu below: ")

final_words = dcc.Markdown(f"""
These study hours were converted into massive dividends, whether through time/money that was saved, or through the delivery of high quality Reports. But, studying for me personally is so much more than that. I've achieved personal growth by understanding the value of discipline/sacrifice and time (*why, oh why does day only last 24 hours?*). We live in an amazing world that is full of hidden gold nuggets. It is up to us to find them, and to prepare ourselves for the challenges that are ahead of us.""")


# dropdown

dropdown_subjects = sorted(df.Category.unique())
dropdown_subjects_dash = dcc.Dropdown(
    id="dropdown_subject",
    options=[{"label": subject, "value": subject} for subject in dropdown_subjects],
    placeholder="Select subject ...",
    searchable=False
)

slider_marks = {int(i): str(i) for i in df.Year.unique()}

slider_dash = dcc.Slider(
    min=df.Year.min(),
    max=df.Year.max(),
    step=None,
    value=2022,
    id="slider_year",
    marks=slider_marks
)


# colors
MAIN_COLOR = "darkgray"
GRID_COLOR = "black"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Study Stats | josipkovac.xyz"
server = app.server


app.layout = html.Div(
    children=[
        navbar,
        html.Br(),
        intro_markdown,
        html.H2("Progress so far ..."),
        dcc.Graph(figure=plot_total()),
        html.H2("Total study per year ..."),
        html.Br(),
        slider_dash,
        dcc.Graph(id="plot_year"),
        html.H2("Additional Information"),
        dcc.Markdown("Want to find out more? Select subject below!", style={"color": "steelblue", "font-weight": "bold"}),
        dropdown_subjects_dash,
        html.Br(),
        html.Div(id="comment"),
        html.Br(),
        dcc.Graph(id="plot_subject"),
        final_words,
        get_footer()

    ],
    style={"margin": "1.0%"}
)

@app.callback(
    Output("plot_subject", "figure"),
    Input("dropdown_subject", "value")
)
def plot_subject_wrapper(subject):
    if not subject:
        raise PreventUpdate
    return plot_subject(subject)

@app.callback(
    Output("plot_year", "figure"),
    Input("slider_year", "value")
)
def plot_year_wrapper(year: int):
    return plot_year(year)

@app.callback(
    Output("comment", "children"),
    Input("dropdown_subject", "value")
)
def get_comment(subject):
    if not subject:
        raise PreventUpdate
    out = dict_additional_info.get(subject)
    return dcc.Markdown(out, style={"padding": "5px", "border": "1px solid black", "background-color": "#f1dae7", "color": "black"})

if __name__ == "__main__":
    app.run_server(debug=True)
