# quiz_Spagnolo
🇪🇸 Spanish Vocab Trainer
A terminal-based flashcard and quiz application to learn Spanish vocabulary, built in Python.
Developed as a personal side project to support self-study of Spanish, with a focus on clean object-oriented design and local data persistence.

# Features:
- Add & remove words — build your own vocabulary with multiple accepted translations per word
- Category-based organisation — words are grouped into thematic categories (work, greetings, numbers, places, animals, IT terms, etc.)
- Two quiz modes:
    1) Open-answer quiz — type the translation freely
    2) Multiple-choice quiz - select an answer beetween the 4 response given (a, b, c, d)
- Persistent storage — vocabulary is saved locally in JSON files and survives between sessions
- General + specific quizzes — train on the full dictionary or drill a single category

# Project Structure:
- quiz_Spagnolo_Ing.py - main file
- file_json - general and specific vocabolary

# To use guide: 
- Requirements: Python 3.7+

- Copy the repository:
git clone https://github.com/francescomanzatoo/spanish-vocab-trainer.git
cd spanish-vocab-trainer

- Run the app:
python quiz_Spagnolo_Ing.py

# Example of usage: 
Read the instruction, then press the choosen command:
1) Add a new word into the dictionary
2) Remove a word from the dictionary
3) Start a general quiz
4) Start a specific quiz
5) Not finished yet...
6) Print all the words of the dictionary
7) Exit

3

Beginning of the quiz:

1) Translate: perro
Answer: cane
Correct!

3) Translate: gato
Answer: gatto
Correct!

Quiz completed! Score: 2/2
