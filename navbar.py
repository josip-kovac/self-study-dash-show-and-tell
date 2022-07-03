import dash_bootstrap_components as dbc
from dash import html
from dash_iconify import DashIconify

# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/

GITHUB_LOGO = "/static/logo-github.png"
LINKEDIN_LOGO = "/static/logo-linkedin.png"

def create_logo_with_href(src, href):
    _out = html.A(
        children=[html.Img(src=src, height="30px")],
        href=href
    )

    return dbc.Col(_out)

logo_github = create_logo_with_href(
    GITHUB_LOGO, "https://github.com/josip-kovac"
)

logo_linkedin = create_logo_with_href(
    LINKEDIN_LOGO, "https://www.linkedin.com/in/josip-kova%C4%8D-632b21128/"
)

logo_blog = dbc.Col([html.A(DashIconify(icon="fa6-solid:blog", inline=False, height=30), href="https://josipkovac.xyz/")])
logo_user = dbc.Col([html.A(DashIconify(icon="carbon:document-pdf", inline=False, height=30), href="https://www.josipkovac.xyz/cv.pdf")])

navbar = dbc.NavbarSimple(
    brand="Self Study Journey of Josip Kovač ⬆️",
    brand_href="https://josipkovac.xyz/",
    dark=False,
    color="light",
    children=dbc.Container(
        [
            dbc.Row(
                [logo_github, logo_linkedin, logo_blog, logo_user]
            )
        ]
    ), fluid=True)