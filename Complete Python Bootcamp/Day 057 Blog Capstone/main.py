'''
The purpose of this project was to act as a capstone for the "Intermediate+" section
of the Udemy Course "100 Days of Code: The Complete Python Pro Bootcamp".
This project focused on using flask and jinja to produce dynamic html pages.
The use of jinja templating, apis, and url building in flask were highlights of this project.
'''

from flask import Flask, render_template
import requests
from post import Post

blog = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()
posts = []
for entry in blog:
    post = Post(entry['id'], entry['title'], entry['subtitle'], entry['body'])
    posts.append(post)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/<int:num>')
def get_blog(num):
    for entry in posts:
        if entry.id == num:
            blog_post = entry
    return render_template("post.html", blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
