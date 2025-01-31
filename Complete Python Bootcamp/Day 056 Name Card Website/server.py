'''
The purpose of this project was to continue gaining experience using Flask. This project focused on
using static pages with Flask, such as images and css files. HTML templates were also explored and used.
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def webpage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
