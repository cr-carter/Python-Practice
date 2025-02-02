'''
The purpose of this project was to continue with the use of flask and jinja,
while also incorporating the use of bootstrap in the html code.
'''
from flask import Flask, render_template
import requests
from post import Post

blog_posts = requests.get(url="https://api.npoint.io/76876931baa729e5bb68").json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<string:num>')
def requested_post(num):
    if num == 'index.html':
        return home()
    else:
        num = int(num)
        for post in blog_posts:
            if post["id"] == num:
                return_post = post
        return render_template("post.html", post=return_post)


if __name__ == "__main__":
    app.run(debug=True)
