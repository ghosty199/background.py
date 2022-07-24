from tkinter import *
import random
root=Tk()
root.geometry("400x400")
root.title("")



dict={"colors":["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]
}


def randomcolors():
    bg=random.randint(0,7)
    root.configure(background = dict["colors"][bg])










button1=Button(root,text="click me",command=randomcolors)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)






























root.mainloop()
