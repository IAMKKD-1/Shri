from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/shri')
def main():
    return render_template("shri.html")

@views.route('/api')
def api_docs():
    return render_template("apidoc.html")

@views.route('/api/<string:user_prompt>', methods=['GET'])
def api():
    pass