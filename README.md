# Flashcard-French-English

This project is a simple flashcard application designed to help users learn French vocabulary. The application displays a French word, and after a few seconds, reveals its English translation. Users can mark words as known or indicate they need more practice, leading to a tailored learning experience.

## Features

- **Interactive Flashcards:** Users can view French words and reveal their English translations.
- **Learn at Your Own Pace:** A timer allows users time to think of the translation before it's displayed.
- **Progress Tracking:** The application remembers which words the user knows and focuses on the remaining ones.
- **User-Friendly Interface:** Simple buttons to navigate through the words and indicate progress.

## How to Use

1. **Run the Application:** Execute the Python script to launch the application.
2. **View French Word:** A French word will be displayed on the flashcard.
3. **Wait or Flip:** Either wait for the timer to automatically flip the card to show the English translation, or click the card to flip it manually.
4. **Mark as Known:** Click the "Right" button (checkmark) if you knew the translation.
5. **Practice Again:** Click the "Wrong" button (cross) if you didn't know the translation or want to practice it again.
6. **Continue Learning:** The application will continue presenting words until you've marked them all as known.


![image](https://github.com/user-attachments/assets/e073f687-abb1-47b6-a18f-ed8488c17020)
![image](https://github.com/user-attachments/assets/e5cfbaf4-8660-497b-9ae3-82561dce5e9b)



## Setup

1. **Clone the Repository:**
   ```bash
   git clone [repository_url]
Use code with caution.
Markdown
Install Dependencies: Ensure you have Python installed, along with the required libraries (tkinter and pandas).

pip install pandas
Use code with caution.
Bash
Run the Script: Navigate to the project directory and run the Python script.

python [your_script_name].py
Use code with caution.
Bash
File Structure
[your_script_name].py: The main Python script for the application.

./day 31 python/data/french_words.csv: CSV file containing the French and English word pairs.

./day 31 python/data/words_to_learn.csv: CSV file that stores the words the user still needs to learn.

./day 31 python/images/: Directory containing images for the flashcard design (card_front.png, card_back.png, right.png, wrong.png).

Data Files
french_words.csv: This file contains the initial list of French words and their English translations.

Columns: French, English

words_to_learn.csv: This file is generated and updated during the application's use. It keeps track of the words the user still needs to practice. If the user finishes all words, this file will eventually be empty.

Dependencies
Python 3.x

tkinter: For creating the graphical user interface. (Usually comes pre-installed with Python)

pandas: For reading and manipulating CSV files.

Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.
