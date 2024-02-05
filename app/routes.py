from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'adun'}
    posts = [
        {
            'author': {'username': 'jane'},
            'body': 'jane pets a cat!'
        },
        {
            'author': {'username': 'michael'},
            'body': 'michael the archangel'
        },
        {
            'author': {'username': 'jane'},
            'body': 'jane pets a cat!'
        },
        {
            'author': {'username': 'michael'},
            'body': 'michael the archangel'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)