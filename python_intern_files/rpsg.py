from tkinter import *
from PIL import Image,ImageTk
from random import randint
# main window
root = Tk()
root.title("Rock Paper Scissor ")
root.configure(background= "light blue")
# picture
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor.png"))
#insert picture
user_lable = Label(root, image=scissor_img, background="light blue")
comp_lable = Label(root, image=rock_img_comp, background="light blue")

user_lable.grid(row=1, column=0,)
comp_lable.grid(row=1, column=4)
#scores
userscores = Label(root, text=0, font=80, background="light blue", fg="black" )
computerscore = Label(root, text=0, font=80, background="light blue", fg="black")
computerscore.grid(row=1,column=1)
userscores.grid(row=1,column=3)
#indicator
user_indicator = Label(root, font=50, text="User",background="light blue")
comp_indicator = Label(root, font=50, text="Computer", background="light blue")
comp_indicator.grid(row=0,column=3)
user_indicator.grid(row=0,column=1)
# game completing mesg
mesg = Label(root, font=50, background="light blue", fg="black")
mesg.grid(row=3,column=2)
#update meassage
def updatemessage(x):
    mesg['text'] = x
#check win
def checkwin(user,computer):
      if user==computer :
        updatemessage("its a draw") 
      elif user=="rock":
           if computer=="paper":
               updatemessage("YOU LOOSE")
               updatecompscore()
           else:
                updatemessage("YOU WIN")
                updateuserscore()
      elif user=="paper":
          if computer=="scissor":
              updatemessage("YOU LOOSE")
              updatecompscore()
          else:
              updatemessage("YOU WIN")
              updateuserscore()           
      elif user=="scissor":
          if computer=="rock":
              updatemessage("YOU LOOSE")
              updatecompscore()
          else:
              updatemessage("YOU WIN")
              updateuserscore() 
      else:
          pass      
# update score
def updateuserscore():
       score = int(userscores["text"])
       score +=1
       userscores["text"] = str(score)
def updatecompscore():
    score = int(computerscore["text"])
    score +=1
    computerscore["text"] = str(score) 
#update choice
choices =["rock","paper","scissor"]
def updatechoice(x):
#for computer
    comp_choice = choices[randint(0,2)]
    if comp_choice == "rock":
        comp_lable.configure(image=rock_img)
    elif comp_choice == "paper":
        comp_lable.configure(image=paper_img)
    else:
        comp_lable.configure(image=scissor_img) 
#for user    
    if x=="rock":
        user_lable.configure(image=rock_img)
    elif x=="paper":
        user_lable.configure(image=paper_img)
    else:
        user_lable.configure(image=scissor_img) 

    checkwin(x,comp_choice)          
#button
rock_button= Button(root, width=20, height=2, text="Rock", pady=15, padx=4, background="red",fg="black", 
command=lambda:updatechoice("rock"))
rock_button.grid(row=2, column=1)
scissor_button= Button(root, width=20, height=2, text="Scissor", pady=15,padx=4,background="orange",fg="black", 
command=lambda:updatechoice("scissor"))
scissor_button.grid(row=2, column=2)
paper_button= Button(root, width=20, height=2, text="Paper",pady=15,padx=4,background="light green",fg="black", 
command=lambda:updatechoice("paper"))
paper_button.grid(row=2, column=3)

root.mainloop()