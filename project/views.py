from flask import Flask, render_template

from app import app, pages

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/story/')
def story():
    return render_template('story.html')

@app.route('/team/')
def team():
    return render_template('team.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/blog/week_1')
def blog_week_1():
    return render_template('blog_entries/week_1.html')

@app.route('/blog/week_2')
def blog_week_2():
    return render_template('blog_entries/week_2.html')

@app.route('/blog/week_3')
def blog_week_3():
    return render_template('blog_entries/week_3.html')

@app.route('/blog/week_4')
def blog_week_4():
    return render_template('blog_entries/week_4.html')

if __name__ == '__main__':
    app.run(debug=True)
