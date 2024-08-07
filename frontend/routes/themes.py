from os import getenv

from .. import app
from ..db import Session

from flask import request, render_template
from sqlalchemy import select

from requests import get, post

BACKEND_URL = getenv("BACKEND_URL")



@app.post("/theme/<string:balance_themes>")
def themes(balance_themes):
    select_theme_responce = get(f"{BACKEND_URL}/theme/{balance_themes}")
    if select_theme_responce.status_code == 200:
        selected_theme = select_theme_responce.json()
        if selected_theme:
            theme = selected_theme[0]['theme']
        else:
            theme = None
        return render_template("themes.html", selected_theme=selected_theme, theme=theme)
    # return "Error fetching theme data", select_theme_responce.status_code




