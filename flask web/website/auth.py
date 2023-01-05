from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/tournaments')
def login():
    return render_template("tournaments.html")


@auth.route('/leaguegames')
def logout():
    return render_template("league.html")


@auth.route('/seasonstats')
def sign_up():
    return render_template("seasonstats.html")
