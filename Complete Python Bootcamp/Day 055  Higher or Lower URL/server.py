'''
The purpose of this project was to gain more experience using flask.
Attention was paid to working with url paths, using the flask debugger,
rendering html elements, using python decorators, and using *args and **kwargs.
'''

from flask import Flask
from random import randint

app = Flask(__name__)

number = randint(0,9)

@app.route("/")
def start():
    return ('<h1 style="text-align: center">Guess a number between 0 and 9. Enter your guess at the end of the URL.</h1>'
            '<p>Example: 127.0.0.1:5000/<b>5</b></p>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route("/<string:guess>")
def higher_lower(guess):
    try:
        guess = int(guess)
    except:
        return('<h1>Please use a number between 0 and 9.</h1>'
               '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExajhpdmpjMjNyc2dyc2M1ejU4dmRjbDR6NW05cGc4eTh6dG8zMnNxdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LPxe1MqUusuNG/giphy.gif">')
    else:
        if guess > number:
            return('<h1>Too high, try again!</h1>'
                   '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
        elif guess < number:
            return('<h1>Too low, try again!</h1>'
                   '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
        elif guess == number:
            return('<h1>You found me!</h1>'
                   '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)
