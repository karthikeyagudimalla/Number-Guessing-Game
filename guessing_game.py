from tkinter import *
from tkinter import PhotoImage
import random
global count
count=1
def onplay():
    def levels(n,level,num):
        print(num)
        def onenter():
            global count
            userinput=int(input.get())
            if userinput==num:
                heading2.destroy()
                input.destroy()
                enter.destroy()
                output.config(text=f"Your choice: {userinput}\nActual Number: {num}\n{userinput} = {num}\nYou Won!!\nNo.of Tries: {count}\n\n"+"Thank You for Playing!!")
                outputframe.pack()
            elif userinput>num:
                input.delete(0,'end')
                output.config(text=f"{userinput} is greater than actual number\nTry Again!!")
                outputframe.pack()
                count+=1
            elif userinput<num:
                input.delete(0,'end')
                output.config(text=f"{userinput} is smaller than actual number\nTry Again!!")
                outputframe.pack()
                count+=1

        heading.destroy()
        one.destroy()
        two.destroy()
        three.destroy()
        heading1=Label(root,text=f"LEVEL-{level}",font=("Georigia",30),bg="Gold",fg="Black")
        heading1.pack(pady=20)
        heading2=Label(root,text=f"Select the number between 1 to {n}",font=("Georgia",23),bg="Pink")
        heading2.pack(pady=20)
        input=Entry(root,font=("Georgia",27))
        input.pack(pady=20)
        enter=Button(root,text="enter",command=onenter,font=("Georgia",25),bg="Dark Blue",fg="red")
        enter.pack(pady=20)
    def onone():
        levels(n=10,level=1,num=random.randint(1,10))
    def ontwo():
        levels(n=100,level=2,num=random.randint(1,100))
    def onthree():
        levels(n=1000,level=3,num=random.randint(1,1000))

    play.destroy()
    heading=Label(root,text="Select the level",font=("Georgia",28),bg="Silver",fg="Black")
    heading.pack(pady=20)
    one=Button(root,text="Level 1",command=onone,font=("Georgia",25),bg="Dark Blue",fg="pink")
    one.pack(pady=20)
    two=Button(root,text="Level 2",command=ontwo,font=("Georgia",25),bg="Dark Blue",fg="pink")
    two.pack(pady=20)
    three=Button(root,text="Level 3",command=onthree,font=("Georgia",25),bg="Dark Blue",fg="pink")
    three.pack(pady=20)

root=Tk()
root.title("The Guessing Game")
root.geometry("950x700")
header=Label(root,text="The Number Guessing Game",font=("Georgia",30),bg="Black",fg="Red")
header.pack(pady=50)
play=Button(root,text="Click to Play!",font=("Georgia",27),fg="Pink",bg="Dark Blue",command=onplay)
play.pack(pady=70)
outputframe=Frame(root,highlightbackground="Yellow",highlightthickness=7,background="Dark Blue")
output=Label(outputframe,text="",font=("Georgia",20),fg="Red",bg="Black")
output.pack(pady=20)
root.mainloop()
