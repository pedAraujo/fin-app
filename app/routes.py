from flask import redirect, session, render_template, Blueprint, flash
from .auth.routes import login_required

main = Blueprint("main", __name__)


@main.route("/index/")
@main.route("/")
@login_required
def index():
    error = None
    if "username" in session:
        return redirect("/finapp/")
        # return render_template("index.html", username=session["username"])
    error = "You must be logged in to view this page."
    flash(error)
    return render_template("index.html", error=error)
