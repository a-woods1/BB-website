from flask import Flask, render_template

from app import app, pages

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/team/')
def team():
    return render_template('team.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)
