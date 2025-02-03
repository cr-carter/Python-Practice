'''
The purpose of this project was to gain further experience with flask,
particularly with handling post requests to flask servers. This is an
update to the code from the Day 059 project.
'''
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

load_dotenv()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", method='get')
    else:
        send_email(name=request.form['name'], email=request.form['email'], phone=request.form['phone'], message=request.form['message'])
        return render_template("contact.html", method='post')


def send_email(name, email, phone, message):
    email_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_PASSWORD')
    with smtplib.SMTP(os.getenv('smtp.gmail.com')) as connection:
        connection.starttls()
        connection.login(email_address, email_password)
        connection.sendmail(
            from_addr=email_address,
            to_addrs=email_address,
            msg=f'Subject:Contact Request From Blog\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
        )


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
