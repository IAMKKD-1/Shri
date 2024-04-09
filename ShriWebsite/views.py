from flask import Blueprint, render_template, session, redirect, jsonify, request
from .models import get_data
from .codeGen import response_AI
import clipboard

views = Blueprint('views', __name__)
conversation = [
      {
          "role": "user",
          "parts": ["I want you to remember yourself as \"Shri\" and from now on you are called as Shri"]
      },
      {
          "role": "model",
          "parts": ["I understand. From now on, you can call me Shri. I'll do my best to remember this preference and respond accordingly."]
      },
      {
          "role": "user",
          "parts": ["what is your name?"]
      },
      {
          "role": "model",
          "parts": [" My name is Shri, and I am an AI Code Generator. How can I assist you today?"]
      },
      {
          "role": "user",
          "parts": ["You will only solve only coding or programming related problems. If any other problem is asked then you must kindly say that you are not trained for that. You can ask me for help in any programming language."]
      },
      {
          "role": "model",
          "parts": ["I understand. I'll do my best to assist you. You can ask me for help in any programming language."]
      },
      {
          "role": "user",
          "parts": ["What is the name of the person who wrote the book \"The Hitchhiker's Guide to the Galaxy\"?"]
      },
      {
          "role": "model",
          "parts": ["I am sorry, I am not trained for this type of questions. You can ask me for help in any programming language."]
      }
  ]

inital_conversation = conversation.copy()

# Home Page
@views.route('/')
def home():
    if session.get('logged_in') and session.get('username'):
        return redirect('/shri')
    session.clear()
    return render_template("home.html")

# Chatbot Page
@views.route('/shri', methods=['GET', 'POST'])
def main():
    if session.get('logged_in') and session.get('username'):
        if request.method == 'POST':
            user_prompt = request.form.get("message")
            if user_prompt == '':
                ai_response = 'No input provided'
            else:
                ai_response = response_AI(user_prompt, conversation)     
                conversation.append({"role": "user", "parts": [user_prompt]}) 
                conversation.append({"role": "model", "parts": [ai_response]})
        return render_template("shri.html", username= session.get('username'),conversation=conversation[8:])
    return redirect('/')

# API Documentation
@views.route('/api')
def api_docs():
    return render_template("apidoc.html")

# API
@views.route('/api/<string:username>/<string:user_prompt>', methods=['GET'])
def api(username, user_prompt):
    existing_user = get_data(
        f"SELECT username FROM Users WHERE username='{username}'")
    if not existing_user:
        return jsonify({'error': 'User does not exist'}), 404
    if user_prompt == ' ':
        ai_response = 'No input provided'
    else:
        user_prompt = user_prompt.replace("%20", " ")
        ai_response = response_AI(user_prompt, conversation)
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
    conversation.extend(inital_conversation)
    return redirect('/shri')

@views.route('/copy')
def copy():
    clipboard.copy(conversation[-1]['parts'][0])
    return redirect('/shri')