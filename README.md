# What is this?
This is my coursework for the GCSE UK curriculum for ages 14-16. The objective is to write a dice game where 2 players can each roll a dice, and based on certain rules points will be added to their scores. The full specifiation for this can be found as Task 2 here: https://www.ocr.org.uk/Images/503195-programming-project-tasks-june-2019-and-june-2020.pdf.

# How to run
Should *probably* run on any Python 3 version. Simply download the dicegame.py file, put it into its own folder (it will generate some text files to store data), and run it.

# Why this project is terrible
The program is in one single file and is about 1800 lines long. It's written using just tkinter, math, random and time in-built libraries. The entire thing is inside a single class (which entirely defeats the point of object-oriented). There is a distinct lack of abstraction and meaningful comments, and there is absolutely no real structure to it. Some of the code is absoutely apalling (there are some particularly horrible examples on lines 1153, 1584, 1649, 172 if you really want to get into it). However, by some miracle, it works, and quite nicely at that - I'm proud of the UI, specifically the fade-in/fade out, loading screens and the entire dice-rollig scene. It's definitely useable if you don't look at the source code, and I'd ultimately consider this to be a fairly impressive project for GCSE level.
