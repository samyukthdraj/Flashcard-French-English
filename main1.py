from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_MEANING = ("Ariel", 60, "bold")

window = Tk()
window.title("Flashcard French to English")
window.minsize(width=900, height=700)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# ---------------------------- DATA SETUP ------------------------------- #
try:
    data = pd.read_csv("./day 31 python/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./day 31 python/data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")
current_card = {}

# ---------------------------- SAVE PROGRESS ---------------------------- #
def save_progress():
    remaining_words = pd.DataFrame(word_dict)
    remaining_words.to_csv("./day 31 python/data/words_to_learn.csv", index=False)

# ---------------------------- FLIP CARD ------------------------------- #
flip_timer = None

def flip_card():
    global current_card_face
    current_card_face = card_back_img
    canvas.itemconfig(card_image, image=current_card_face)
    canvas.config(bg=BACKGROUND_COLOR)
    label_title.config(text="English", bg=BACKGROUND_COLOR, fg="white")
    label_meaning.config(text=current_card["English"], bg=BACKGROUND_COLOR, fg="white")

def is_known():
    global word_dict, current_card
    try:
        word_dict.remove(current_card)
    except ValueError:
        print("No more words to learn!")
    save_progress()
    next_card()

def next_card():
    global current_card, flip_timer, current_card_face
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    current_card_face = card_front_img
    canvas.itemconfig(card_image, image=current_card_face)
    canvas.config(bg=BACKGROUND_COLOR)  # Set canvas background to white
    label_title.config(text="French", bg="white", fg="black")
    label_meaning.config(text=current_card["French"], bg="white", fg="black")
    flip_timer = window.after(5000, func=flip_card)

# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width=800, height=526, bg="white", highlightthickness=0)  # Initial bg = "white"
card_front_img = PhotoImage(file="./day 31 python/images/card_front.png")
card_back_img = PhotoImage(file="./day 31 python/images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

label_title = Label(text="French", font=FONT_TITLE, bg="white")
label_title.place(x=300, y=150)

label_meaning = Label(text="word", font=FONT_MEANING, bg="white")
label_meaning.place(x=300, y=263)

right_img = PhotoImage(file="./day 31 python/images/right.png")
wrong_img = PhotoImage(file="./day 31 python/images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()