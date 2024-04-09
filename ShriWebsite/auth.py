from flask import Blueprint, render_template, request, redirect, session

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
async def signup():
    return redirect('/login')
    
# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in') and session.get('username'):
        return redirect('/')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'test' and password == 'test':
            session['logged_in'] = True
            session['username'] = username
            return redirect('/')
    return render_template("login.html")

# Logout
@auth.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username')
    return redirect('/')