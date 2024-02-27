from tkinter import*
import random

root = Tk()
root.title("Encapsulation")
root.geometry("500x500")
root.configure(background="cyan")

name = Label(root,font=("Arial",40),bg="cyan")
name.place(relx=0.5,rely=0.5,anchor=CENTER)

class game:
    def __init__(self):
        self.__score=0
    def update_game(self):
        self.text=["red","green","blue","black","yellow"]
        self.random_text = random.randint(0,4)
        self.color=["red","green","blue","black","yellow"]
        self.random_color=random.randint(0,4)
        name["text"] = self.text[self.random_text]
        name["fg"]=self.color[self.random_color]
    
game_obj = game()
start = Button(root,text="start",command=game_obj.update_game,bg="orangered")
start.place(relx=0.5,rely=0.8,anchor=CENTER)
root.mainloop()
