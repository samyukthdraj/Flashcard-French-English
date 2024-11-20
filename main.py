BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel",40,"italic")
FONT_MEANING = ("Ariel", 60, "bold")

from tkinter import *
import pandas
import random

window = Tk()
window.title("Flashcard French to English")
window.minsize(width=900, height=400)
window.config(bg= BACKGROUND_COLOR, padx=50,pady=50)

#images
# canvas = Canvas(width=800, height=526)
# white_canvas = PhotoImage(file="./day 31 python/images/card_front.png")
# canvas.create_image(400, 263, image= white_canvas)
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row= 0, column= 0)


white_image = PhotoImage(file="./day 31 python/images/card_front.png")
green_image = PhotoImage(file="./day 31 python/images/card_back.png")
right_image = PhotoImage(file="./day 31 python/images/right.png")
wrong_image = PhotoImage(file="./day 31 python/images/wrong.png")

#taking datas from french_words.csv
try:
    data = pandas.read_csv("./day 31 python/data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./day 31 python/data/french_words.csv") # If not found, read original file
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")  # Use data from words_to_learn if it exists
current_card = {}


#==========================================FUNCTIONS==================================================================
#save progress function
def save_progress():
    remaining_words = pandas.DataFrame(word_dict)
    remaining_words.to_csv("./day 31 python/data/words_to_learn.csv", index=False)

# flip card function
current_card_face = white_image  # Initialize with the starting image
def flip_card():
    global current_card_face,current_card  # Necessary to modify the global variable
    current_card_face = green_image
    card_button.config(image=current_card_face, bg=BACKGROUND_COLOR)
    label_title.config(text="English", bg=BACKGROUND_COLOR, fg="white")
    label_meaning.config(text=current_card["English"], bg=BACKGROUND_COLOR, fg="white")

#the words we cant correctly guess will be in there in a new file, whereas the words we know wont repeat.

def is_known():
    global word_dict, current_card  # Add current_card here to remove the current card

    try:  # Handle potential empty list
        word_dict.remove(current_card)  # Remove current card from the list

    except ValueError:  # Catch ValueError if current_card is not in word_dict
        print("No more words to learn!")

    save_progress()  # Save updated list to words_to_learn.csv
    next_card()

#function for next words being added 
def next_card():
    global current_card, flip_timer, current_card_face
    window.after_cancel(flip_timer) #cancel the previous timer to avoid multiple timers stacking up
    current_card = random.choice(word_dict)
    current_card_face = white_image
    label_title.config(text="French", fg="black", bg="white")
    label_meaning.config(text=current_card["French"], fg="black", bg="white")
    card_button.config(image=current_card_face, bg="white")
    flip_timer = window.after(3000, func=flip_card)




#buttons
card_button = Button(window, image=white_image, highlightthickness=0,width=800,height=400,command=flip_card)
card_button.grid(row=0, column=0, columnspan=2, pady=(50,0))

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0, padx=50)

wrong_button = Button(image=wrong_image, highlightthickness=0, command= next_card)
wrong_button.grid(row=1, column=1, padx=50)

#label
label_title = Label(text="French", font=FONT_TITLE, bg="white")
label_title.place(x=300,y=150)

label_meaning = Label(text="Meaning", font=FONT_MEANING, bg="white")
label_meaning.place(x=290,y=260)

flip_timer = window.after(3000, func=flip_card) #call after 3 seconds
next_card()

window.mainloop()