from dash import html

def get_footer():
    return html.Footer(html.Label(['© ', html.A('josipkovac.xyz', href='https://josipkovac.xyz/') , ". All rights reserved."]), style={"text-align": "center"})