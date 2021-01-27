`========HOW TO RUN=======`

I developed this on python 3.4 and later on 3.8, so it is definitely compatible with these but should in theory run on any python 3 version. Simply download the dicegame.py file, put it into a separate folder and **open it in python IDLE to run it.** Note that python will *not* run tkinter interfaces from command line(double clicking on the file). It should also work with any screen resolution though I haven't extensively tested this.

`========DESCRIPTION========`

This is my coursework for the GCSE UK curriculum for ages 14-16. The objective is to write a dice game where 2 players can each roll a dice, and based on certain rules points will be added to their scores. The full specifiation for this can be found as Task 2 here: https://www.ocr.org.uk/Images/503195-programming-project-tasks-june-2019-and-june-2020.pdf. Is it allowed to publish coursework before it's submitted? I can't find anything at all saying that I can or can't, so I assume that it's fine.

`========PROGRAM========`

The program is about 1800 lines long and is written using just tkinter, math, random and time in-built libraries. It is class based, mostly using self and writing to external files for permanent storage. All code is written by myself except for the function to convert from RGB to hexadecimal. 

`========THIS IS HORRIBLE=======`
SonarCloud estimates the whole thing to take 3 days of solid work to fix - which is not happening. This is a monument to bad coding, but whatever; I was learning python when I wrote this. There are some particularly horrible examples on lines 1153, 1584, 1649, 172 if you really want to get into it, not to mention the entire structure. However, by some miracle, it works, and quite nicely at that - I'm proud of the UI, specifically the fade-in/fade out, loading screens and the entire dice-rollig scene. It's definitely useable if you don't look at the source code...
