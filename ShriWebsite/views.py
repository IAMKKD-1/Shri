from flask import Blueprint, render_template, session, redirect, jsonify, request
from .googlepalm import response_AI
import clipboard

views = Blueprint('views', __name__)
conversation = []

@views.route('/')
def home():
    if session.get('logged_in') and session.get('username'):
        return redirect('/shri')
    session.clear()
    return render_template("home.html")

# Chatbot Page
@views.route('/shri', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        user_prompt = request.form['message']
        ai_response = response_AI(user_prompt)     
        conversation.append({'user': user_prompt, 'response': ai_response, 'is_code': True})
    return render_template("shri.html", username= session.get('username'),conversation=conversation)

@views.route('/api')
def api_docs():
    return render_template("apidoc.html")

# API
@views.route('/api/<string:username>/<string:user_prompt>', methods=['GET'])
def api(username, user_prompt):
    
    if user_prompt == '':
        ai_response = 'No input provided'
    else:
        ai_response = response_AI(user_prompt)
    response = {
        'username': username,
        'user_prompt': user_prompt,
        'response': ai_response,
    }
    return jsonify(response)

# Clear Chatbot
@views.route('/clear')
def clear():
    conversation.clear()
    return redirect('/shri')

@views.route('/copy')
def copy():
    clipboard.copy(conversation[-1]['response'])
    return redirect('/shri')