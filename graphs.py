import pandas as pd
from datetime import date
import plotly.graph_objects as go
import plotly.express as px
from data import get_data
from format_time import time_float_to_string

df = get_data()

def plot_total():
    _local_df = df.groupby("Category")["DurationHours"].sum().to_frame().sort_values(by="DurationHours").reset_index()
    _local_df["Duration"] = _local_df["DurationHours"].apply(time_float_to_string)


    total = _local_df["DurationHours"].sum()
    fig = px.bar(
        data_frame=_local_df,
        y="Category",
        x="DurationHours",
        template="plotly_white",
        custom_data=["Category", "Duration"],
        text="Duration"
    )

    fig.update_traces(
        hovertemplate="<br>".join([
            "Subject: <b>%{customdata[0]}</b>",
            "Duration: %{customdata[1]}"
        ]),
        marker_color="steelblue")



    fig.layout.xaxis.title = "Duration (hours)"
    fig.layout.yaxis.title = "Subject"
    # we don't need the zoom / + on mobile phone, zoom lowers user experience
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True  
    fig.layout.title = f"Total Hours Spent = {time_float_to_string(total)}"
    #fig.layout.paper_bgcolor = MAIN_COLOR
    #fig.layout.plot_bgcolor = MAIN_COLOR
    #fig.update_layout(font_color="white")
    return fig


def plot_year(year: int):

    _local_df = df.query(f"Year == {year}").groupby("Category")["DurationHours"].sum().to_frame().sort_values(by="DurationHours").reset_index()
    _local_df["Duration"] = _local_df["DurationHours"].apply(time_float_to_string)


    total = _local_df["DurationHours"].sum()
    fig = px.bar(
        data_frame=_local_df,
        y="Category",
        x="DurationHours",
        template="plotly_white",
        custom_data=["Category", "Duration"],
        text="Duration"
    )

    fig.update_traces(
        hovertemplate="<br>".join([
            "Subject: <b>%{customdata[0]}</b>",
            "Duration: %{customdata[1]}"
        ]),
        marker_color="#31697e")



    fig.layout.xaxis.title = "Duration (hours)"
    fig.layout.yaxis.title = "Subject"
    # we don't need the zoom / + on mobile phone, zoom lowers user experience
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True  
    fig.layout.title = f"Total Hours Spent = {time_float_to_string(total)} | YEAR = {year}"
    #fig.layout.paper_bgcolor = MAIN_COLOR
    #fig.layout.plot_bgcolor = MAIN_COLOR
    #fig.update_layout(font_color="white")
    return fig

def plot_subject(subject):

    _local_df = df.query(f"Category == '{subject}'").assign(Cumulative = lambda x: x.DurationHours.cumsum())
    _local_df["Duration"] = _local_df["Cumulative"].apply(time_float_to_string)
    _local_df["DateLabel"] = _local_df["Date"].dt.strftime("%Y-%m-%d")

    min_date = _local_df["Date"].min()


    total = _local_df["DurationHours"].sum()
    fig = px.line(
        data_frame=_local_df,
        x="Date",
        y="Cumulative",
        markers=True,
        template="plotly_white",
        custom_data=["DateLabel", "Duration"],
    )

    fig.update_traces(
        hovertemplate="<br>".join([
            "Date: %{customdata[0]}",
            "Total Time: %{customdata[1]}"
        ]),
        marker_color="black",
        line_color="#b44683",
        marker_size=5)
    
    fig.update_layout(
        xaxis_range=[f"{min_date:%Y-%m-%d}", date.today()]
    )

    fig.layout.yaxis.title = "Total Hours Spent (cumulative)"
    fig.layout.xaxis.title = "Date"
    # we don't need the zoom / + on mobile phone, zoom lowers user experience
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True  
    fig.layout.title = f"Total {subject} study = {time_float_to_string(total)}"
    return fig