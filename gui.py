from Tkinter import *
import Tkinter as ttk
from ttk import *

root = ttk.Tk()
S = ttk.Scrollbar(root)
T = ttk.Scrollbar(root)
Q = ttk.Scrollbar(root)

root.title("Automated Graded Essays")
canvas1 = ttk.Canvas(root, width = 50, height = 50)
canvas1.pack()
listbox = Listbox(root)
listbox.pack()

listbox.insert(END, "Essay Questions")

for item in ["Question 1", "Question 2", "Question 3", "Question 4","Question 5","Question 6", "Question 7","Question 8"]:
    listbox.insert(END, item)

choices = {}
s="All of us can think of a book that we hope none of our children or any other children have taken off the shelf." 
s+="But I have the right to remove that book from the shelf  that work I abhor  then you also have exactly the same right and so does everyone else." 
s+="And then we have no books left on the shelf for any of us. --Katherine Paterson, Author" 
s+="Write a persuasive essay to a newspaper reflecting your vies on censorship in libraries. Do you believe that certain materials, such as books,"
s+="music, movies, magazines, etc. should be removed from the shelves they are found offensive? Support your position with convincing arguments"
s+="from your own experience, observations, and/or reading."
choices["Question1"]=s


t="Write a persuasive essay to a newspaper reflecting your vies on censorship in libraries. Do you believe" 
t+="that certain materials, such as books, music, movies, magazines, etc., should be removed from the" 
t+="shelves if they are found offensive? Support your position with convincing arguments from your own" 
t+="experience, observations, and/or reading."
choices["Question2"]=t

t=""
t+="Write a response that explains how the features of the setting affect the cyclist. In your response,"
t+="include examples from the essay that support your conclusion."
choices["Question 3"]=t


l = "When they come back, Saeng vowed silently to herself, in the spring, when the snows melt and the" 
l+="geese return and this hibiscus is budding, then I will take that test again." 
l+="Write a response that explains why the author concludes the story with this paragraph. In your response, include details and examples from the story that support your ideas"
choices["Question 4"]=l


m="Describe the mood created by the author in the memoir. Support your answer with relevant and specific information from the memoir."
choices["Question 5"]=m

n="Based on the excerpt, describe the obstacles the builders of the Empire State Building faced in"
n+="attempting to allow dirigibles to dock there. Support your answer with relevant and specific information from the excerpt."
choices["Question 6"]=n


o="Write about patience. Being patient means that you are understanding and tolerant. A patient person"
o+="experience difficulties without complaining."
choices["Question 7"]=o


p="We all understand the benefits of laughter. For example, someone once said,Laughter is the shortest distance between two people." 
p+="Many other people believe that laughter is an important part of any relationship. Tell a true story in which laughter was one element or part"
choices["Question 8"]=p

root.title("Tk dropdown example")
text=Text(root, width = 110, height =10, fg = 'black',selectborderwidth =2, padx= 5, pady=5)
text.pack()
text.config(yscrollcommand=S.set)
text1=Text(root, width = 110, height =15)
text1.pack()
text1.config(yscrollcommand=S.set)
text2=Text(root, width = 20, height =2)
text2.pack()
text2.config(yscrollcommand=S.set)
button1 = ttk.Button(text='Submit Essay')
canvas1.create_window(20, 30, window=button1)

def change_dropdown(*args):
    question = choices[tkvar.get()]
    print(question)

def getSample(*args):
    choicesTemp = { }
    choicesTemp['1']="alpha"
    choicesTemp['2']="beta gamma delta as all"
    choicesTemp['3']="c"
    choicesTemp['4']="d"
    choicesTemp['5']="e"
    choicesTemp['6']="f"
    choicesTemp['7']="g"
    choicesTemp['8']="h"

root.mainloop()

