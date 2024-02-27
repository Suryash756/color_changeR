from tkinter import*
import random

root = Tk()
root.title("Encapsulation")
root.geometry("500x500")
root.configure(background="cyan")

label_score = Label(root,text="score :0",font=("Arial",15,"bold"),bg="cyan")
label_score.place(relx=0.2,rely=0.2,anchor=CENTER)
inp= Entry(root)
inp.place(relx=0.5,rely=0.7,anchor=CENTER)
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
    def __update_score(self,inp):
        if (inp == self.color[self.random_color]):
            self.__score = self.__score + random.randint(0,10)
            label_score["text"]="Score:" + str(self.__score)
    def get_user_value(self,inp):
        self.__update_score(inp)
        
    
game_obj = game()
def get_inp():
    inp_val = inp.get()
    game_obj.get_user_value(inp_val)
    game_obj.update_game()
    inp.delete(0,END)
    
start = Button(root,text="start",command=game_obj.update_game,bg="orangered")
start.place(relx=0.7,rely=0.7,anchor=CENTER)
check = Button(root,text="check",command=get_inp,bg="orangered")
check.place(relx=0.9,rely=0.7,anchor=CENTER)
root.mainloop()
