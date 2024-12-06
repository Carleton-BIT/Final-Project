import json
from tkinter import *
import _json
from tkinter import messagebox
import pyttsx3

engine=pyttsx3.init()

voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

##############Functions section###########
def search():
   data= json.load(open('data.json'))
   word=enterwordEntry.get()
   if word in data:
       meaning=data[word]
       print(meaning)
       for item in meaning:
           textarea.insert(END,u'\u2022'+item+'\n\n')


####UI SECTION########
root=Tk()

root.geometry('555x260+100+30')

root.title('Talking Dictionary created by Setaish Qayomi')

root.resizable(False,False)

bgimage=PhotoImage(file='bg.png')
bgLabel=Label(root,image=bgimage)
bgLabel.place(x=0,y=0)


def clear():
    enterwordEntry.delete(0,END)
    textarea.delete(1.0,END)

def iexit():
    res=messagebox.askyesno('Confirm','Are you sure you want to exit??')
    if res==True:
        root.destroy()
    else:
        pass

def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()

def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()

enterwordlabel=Label(root,text='Enter Word',font=('Times',15,'bold'),foreground='green',bg='whitesmoke')
enterwordlabel.place(x=320,y=50)

enterwordEntry=Entry(root,font=('Times',8,'bold'),justify=CENTER,bd=6)
enterwordEntry.place(x=320,y=80)

searchimage=PhotoImage(file='search.png')
searchButton=Button(root,image=searchimage, cursor='hand2',activebackground='whitesmoke'
                    ,command=search)
searchButton.place(x=360,y=114)

micimage=PhotoImage(file='mic.png')
miciButton=Button(root,image=micimage, cursor='hand2'
                  ,command=wordaudio)
miciButton.place(x=390,y=114)

meaninglabel=Label(root,text='Word Meaning',font=('Times',15,'bold'),foreground='green',bg='whitesmoke')
meaninglabel.place(x=120,y=50)


textarea=Text(root,width=26,height=7,font=('Times',8,'bold'),bd=6)
textarea.place(x=103,y=85)

audioimage=PhotoImage(file='mic.png')
audioButton=Button(root,image=audioimage, cursor='hand2'
                   ,command=meaningaudio)
audioButton.place(x=275,y=160)

clearimage=PhotoImage(file='clear.png')
clearButton=Button(root,image=clearimage,
                   cursor='hand2', command=clear)
clearButton.place(x=275,y=130)

exitimage=PhotoImage(file='exit.png')
exitButton=Button(root,image=exitimage, cursor='hand2'
                  ,command=iexit)
exitButton.place(x=56,y=213)

def enter_function(event):
     searchButton.invoke()

root.bind('<Return>',enter_function)

root.mainloop()