#this code is form github.com/prateek269/GitHub-action-practice/blob/main/app.py
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
