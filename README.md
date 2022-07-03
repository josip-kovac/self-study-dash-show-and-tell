# Self Study Journey - Dash/Plotly web app (Show and Tell)

This repository serves as a template for [the web app I made](https://self-study-jk.herokuapp.com/). Also, big thanks to:
* [Elias Dabbas](https://www.linkedin.com/search/results/all/?keywords=elias%20dabbas&origin=RICH_QUERY_SUGGESTION&position=0&searchId=a91fd9d2-ceae-4acf-a75a-26f0fdfdcc02&sid=%3AAb) for the [great book on Plotly and Dash](https://www.amazon.com/gp/product/B08XMW45VY/ref=dbs_a_def_rwt_hsch_vapi_tkin_p1_i0).
* [Adam Schroeder](https://www.linkedin.com/feed/update/urn:li:activity:6947657882075078656?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A6947657882075078656%2C6947955282467573760%29) for the invitation.

# Motivation

For the last 5 years, I have been recording the time spent on studying various subjects. The goal was to have accountability and control over the personal time expenditure in order to have the best use of one's (limited) time.

The analysis of data was run in R/Python locally, and I've made various conclusions about my study habits.

After tinkering with Hugo ([personal blog](https://josipkovac.xyz/)) and LaTeX ([CV which is close to impossible to reproduce in Word](https://www.josipkovac.xyz/cv.pdf)), I've made a decision to make my study stats public. Not knowing about Dash/Plotly, I've made my stats public through Jupyter notebook (to be more precise, static HTML file).

But, all of that changed after I've stumbled onto *Interactive Dashboards and Data Apps with Plotly and Dash* from Elias Dabbas. 

The [app](https://self-study-jk.herokuapp.com/) has been made public, and this repository serves as a template for your own app. This code does not fully reproduce my own web app:
* `data/main_data.xlsx` has Activity column masked due to the privacy concerns. Each entry in Activity specifies what book has been read, which library has been developed etc.
* `comments.py` has same Lorem Ipsum text.

# Installation

Pretty standard:

> pip install -r requirements.txt

# App Logic

The structure of the app is as follows:
1. Navigation bar with links to the GitHub, LinkedIn, personal blog and CV (`navbar.py`). Change accordingly.
2. Intro written using `dcc.Markdown` in `app.py`.
3. First graph: total hours spent on different subjects.
4. Second graph: total study per year, with Sliders where you can choose particular year. Be very careful that the numbers on the slider are of type `int`, otherwise every year will have label `2k`.
5. Third graph: dropdown menu where you can select various subjects (as found in `main_data.xlsx`). Upon selection, comment in red box will be shown for the additional information.

Templates for all graphs are in `graphs.py`.

The colors for the app were not picked at random: `steelblue` is the main color, and all other colors are are connected to that color through various presets ([link here](https://colors.muz.li/color/steel-blue)).

# How to start App?

> python app.py

# Final Remarks

Good luck in your studies and personal development. Hard study pays off, but don't forget:
* To rest
* To have fun
* To exercise
* To study subjects that are not in the business domain (try to make that new dish!)