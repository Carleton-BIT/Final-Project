**Talking Dictionary**
Overview
Talking Dictionary is a graphical user interface (GUI) application that allows users to search for word meanings and listen to the pronunciations of both the word and its meaning. This project, created using Python and the Tkinter library, provides an intuitive way to interact with a dictionary, featuring text-to-speech functionality powered by the pyttsx3 library.

Features
Word Search: Retrieve meanings of words from a predefined JSON file (data.json).
Text-to-Speech:
Hear the pronunciation of the entered word.
Listen to the meaning of the word.
Interactive GUI: User-friendly interface built with Tkinter.
Keyboard Shortcut: Press the Enter key to initiate a word search.
Additional Functions:
Clear Fields: Quickly clear the input and output fields.
Exit Confirmation: Prompt the user to confirm before exiting the application.
Installation
Prerequisites:

Python 3.10 or later.
Required Python libraries: tkinter, pyttsx3.
Installation Steps:

Clone or download this repository to your local machine.
Ensure the following files are in the project directory:
main.py (this script).
data.json (dictionary data in JSON format).
Image assets:
bg.png
search.png
mic.png
clear.png
exit.png
Install the required libraries using pip:
bash
Copy code
pip install pyttsx3
How to Use
Start the Application:

Run main.py in your Python environment.
The application window will open.
Search for a Word:

Enter a word in the "Enter Word" text box.
Click the Search button (🔍) or press the Enter key.
Listen to Pronunciation:

Click the Mic icon near "Enter Word" to hear the pronunciation of the entered word.
Click the Mic icon near "Word Meaning" to hear the definition.
Clear Fields:

Click the Clear button (🧹) to clear both the input and output fields.
Exit the Application:

Click the Exit button (❌).
Confirm the exit prompt.
