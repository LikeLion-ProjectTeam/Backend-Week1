from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'secret key'

users = {
    "id": "pw1234"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        session['user'] = username
        flash('Login successful', 'info')
        return redirect(url_for('home'))
    else:
        flash('Invalid ID or PW', 'wrong')
        return redirect(url_for('home'))

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_post():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users:
        flash('already exists', 'wrong')
        return redirect(url_for('register'))

    users[username] = password
    flash('Registration successful.', 'info')
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged Out!', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)