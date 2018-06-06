from flask import Flask, render_template

from app import app, pages

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/route1/')
def project_1():
    return render_template('project1.html')
    
if __name__ == '__main__':
    app.run(debug=True)