'''
This project was a capstone for the 'Intermediate' section of the course
100 Days of Code: The Complete Python Pro Bootcamp.
The purpose of this project was to utilize what I have learned about tkinter,
pandas, defining and using functions, and correct logic flow.
I also went a step further and researched how to perform actions when the user
closes the window, using the '.protocol' methods.
'''

from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = None

# Try to open a saved words_to_learn.csv file. If it does not exist, then open
# the french_words.csv. Whichever csv was opened, convert the data to a dictionary.
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
    print(type(data))
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    words_to_learn = data.to_dict(orient='records')


# --------------------- SAVE CARDS ---------------------#
# When the user clicks the exit button on the window, save
# remaining data in the dictionary to words_to_learn.csv
def on_closing():
    global words_to_learn
    new_data = pandas.DataFrame(words_to_learn)
    new_data.to_csv('./data/words_to_learn.csv', index=False)
    window.destroy()


# --------------------- KNOWN WORD ---------------------#
# When the user clicks the green check mark, remove the current
# word from the words_to_learn dictionary
def is_known():
    words_to_learn.remove(current_card)
    next_card()


# --------------------- NEXT CARD ---------------------#
# When the user clicks either the red x or the green check mark,
# randomly choose a new word from the words_to_learn dictionary.
# The displayed word will default to French. If no words are left,
# recreate the full dictionary from the french_words.csv file.
def next_card():
    global current_card
    global words_to_learn
    try:
        current_card = random.choice(words_to_learn)
    except IndexError:
        data = pandas.read_csv("./data/french_words.csv")
        words_to_learn = data.to_dict(orient='records')
        current_card = random.choice(words_to_learn)
    finally:
        flashcard_canvas.itemconfig('language', text="French")
        set_french_bg()


# --------------------- SET BG ---------------------#
# For convenience, I defined two functions that will change the
# color scheme when switching between English and French. One issue
# I could not solve is that the buttons display a green background
# behind the pictures of the x and check mark. This did not change 
# even when modifying the .config(bg= ) attribute. I was unable to
# find an answer on stackoverflow and similar websites.
def set_french_bg():
    flashcard_canvas.itemconfig('language', text="French", fill='black')
    flashcard_canvas.itemconfig('card_word', text=current_card['French'], fill='black')
    flashcard_canvas.itemconfig('canvas_image', image=card_front)
    flashcard_canvas.config(bg=BACKGROUND_COLOR)
    window.config(bg=BACKGROUND_COLOR)
    wrong_button.config(bg=BACKGROUND_COLOR)
    right_button.config(bg=BACKGROUND_COLOR)


def set_english_bg():
    flashcard_canvas.itemconfig('language', text="English", fill='white')
    flashcard_canvas.itemconfig('card_word', text=current_card['English'], fill='white')
    flashcard_canvas.itemconfig('canvas_image', image=card_back)
    flashcard_canvas.config(bg='white')
    window.config(bg='white')
    wrong_button.config(bg='white')
    right_button.config(bg='white')


# --------------------- CARD FLIP ---------------------#
# When the user clicks on the canvas, switch from French to
# English, and vice versa.
def flip_card():
    global current_card
    language = flashcard_canvas.itemcget('language', 'text')
    if language == 'French':
        set_english_bg()
    else:
        set_french_bg()


# --------------------- UI SETUP ---------------------#
window = Tk()

window.title("Flashy")
window.config(width=900, height=900, padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(width=None, height=None)

flashcard_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
flashcard_canvas.create_image(400, 263, image=card_front, tags='canvas_image')
flashcard_canvas.grid(row=0, column=0, columnspan=2)
flashcard_canvas.create_text(400, 150, font=("Ariel", 40, "italic"), tags="language")
flashcard_canvas.create_text(400, 263, font=("Ariel", 60, "bold"), tags="card_word")

flashcard_canvas.tag_bind('canvas_image', '<Button-1>', lambda e: flip_card())

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, border=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, border=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
