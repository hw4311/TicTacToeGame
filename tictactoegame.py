#TicTacToe by Hunter Williamson, Reda Masri, and Nathan Reyes Vergara

from tkinter import *
from tkinter import messagebox
import time

window = Tk() #Creating the window using Tkinter
window.title("TicTacToe") #Title of the window
window.geometry("220x250") #Setting the size of the window

Moves = 1 #Assigning 1 int to a variable called Moves

def TurnClicked(): #Creating a function that uses turns
    global Moves #Calling moves as a global variable
    if Moves == 1: #If statement that uses the base value of the moves variable and changes it to 2 int then writes an X in the box
        Moves = 2
        return "X"
    elif Moves == 2: #Elseif statement that takes the 2 int then sets it back to the 1 int and writes an O in the box.
        Moves = 1
        return "O" #This function then repeats because of the reassignment of the int values
        

def Button1Clicked():
    global Moves #Calling the global moves variable
    if Button1["text"] == "": #If button has no text in it then it is clickable
     Button1["text"] = TurnClicked() #Calling the TurnClicked function which puts an "X" or an "O" based on the function

def Button2Clicked(): #Repeats for all 9 ButtonClicked functions
    global Moves
    if Button2["text"] == "":
        Button2["text"] = TurnClicked()

def Button3Clicked():
    global Moves
    if Button3["text"] == "":
        Button3["text"] = TurnClicked()

def Button4Clicked():
    global Moves
    if Button4["text"] == "":
        Button4["text"] = TurnClicked()

def Button5Clicked():
    global Moves
    if Button5["text"] == "":
        Button5["text"] = TurnClicked()


def Button6Clicked():
    global Moves
    if Button6["text"] == "":
        Button6["text"] = TurnClicked()

def Button7Clicked():
    global Moves
    if Button7["text"] == "":
        Button7["text"] = TurnClicked()

def Button8Clicked():
    global Moves
    if Button8["text"] == "":
        Button8["text"] = TurnClicked()

def Button9Clicked():
    global Moves
    if Button9["text"] == "":
        Button9["text"] = TurnClicked()

def Vertical(): #Vertical check function
    if Button1["text"] == "X" and Button2["text"] == "X" and Button3["text"] == "X": #Checks vertically the buttons to see if they have an "X" text in them
        Button1.configure(bg="green") #Configures the buttons vertically down to change green one by one
        Button2.configure(bg="green")
        Button3.configure(bg="green")

        messagebox.showinfo("X wins!") #Messagebox displays showing that x wins
        window.destroy() #Terminates the tkinter program
        
        
                 
    elif Button4["text"] == "X" and Button5["text"] == "X" and Button6["text"] == "X": #Same thing as before but vertically down in the middle
        Button4.configure(bg="green")
        Button5.configure(bg="green")
        Button6.configure(bg="green")

        messagebox.showinfo("X wins!")
        window.destroy()
    
    if Button7["text"] == "X" and Button8["text"] == "X" and Button9["text"] == "X": #Same thing as before but vertically down at the end
        Button7.configure(bg="green")
        Button8.configure(bg="green")
        Button9.configure(bg="green")

        messagebox.showinfo("X wins!")
        window.destroy()

def Horizontal(): #Horizontal check function
    if Button1["text"] == "X" and Button4["text"] == "X" and Button7["text"] == "X": #Checks horizontally the buttons to see if they have an "X" text in them
        Button1.configure(bg="green") #Configures the buttons colors to green one by one
        Button4.configure(bg="green")
        Button7.configure(bg="green")

        messagebox.showinfo("X wins!")
        window.destroy()

    elif Button2["text"] == "X" and Button5["text"] == "X" and Button8["text"] == "X": #Same thing as before but horizontally in the middle
        Button2.configure(bg="green")
        Button5.configure(bg="green")
        Button8.configure(bg="green")

        messagebox.showinfo("X wins!")
        window.destroy()
    
    if Button3["text"] == "X" and Button6["text"] == "X" and Button9["text"] == "X": #Same thing as before but horizontally at the end
        Button3.configure(bg="green")
        Button6.configure(bg="green")
        Button9.configure(bg="green")

        messagebox.showinfo("X wins!")
        window.destroy()

def Diagonal(): #Diagonal check function
    if Button1["text"] == "X" and Button5["text"] == "X" and Button9["text"] == "X": #Checks diagonally the buttons to see if they have an "X" text in them
        Button1.configure(bg="green") #Changes the buttons colors to green one by one
        Button5.configure(bg="green")
        Button9.configure(bg="green")

        messagebox.showinfo("X wins!")
        window.destroy()
    
    elif Button7["text"] == "X" and Button5["text"] == "X" and Button3["text"] == "X": #Same thing as before but different locations
        Button7.configure(bg="green")
        Button5.configure(bg="green")
        Button3.configure(bg="green")

        messagebox.showinfo("X wins!")
        window.destroy()
    

def OVertical(): #O vertical check function
    if Button1["text"] == "O" and Button2["text"] == "O" and Button3["text"] == "O": #Checks vertically the buttons to see if they have an "O" text in them
        Button1.configure(bg="red") #Changes the buttons to red
        Button2.configure(bg="red")
        Button3.configure(bg="red")

        messagebox.showinfo("O wins!")
        window.destroy()
    
    elif Button4["text"] == "O" and Button5["text"] == "O" and Button6["text"] == "O": #Same thing as before but vertically down in the middle
        Button4.configure(bg="red")
        Button5.configure(bg="red")
        Button6.configure(bg="red")

        messagebox.showinfo("O wins!")
        window.destroy()
    
    if Button7["text"] == "O" and Button8["text"] == "O" and Button9["text"] == "O": #Same thing as before vertically down at the end
        Button7.configure(bg="red")
        Button8.configure(bg="red")
        Button9.configure(bg="red")

        messagebox.showinfo("O wins!")
        window.destroy()

def OHorizontal(): #O horizontal check function
    if Button1["text"] == "O" and Button4["text"] == "O" and Button7["text"] == "O": #Checks horizontally the buttons to see if they have an "O" text in them
        Button1.configure(bg="red")
        Button4.configure(bg="red")
        Button7.configure(bg="red")

        messagebox.showinfo("O wins!")
        window.destroy()

    elif Button2["text"] == "O" and Button5["text"] == "O" and Button8["text"] == "O": #Same thing as before horizontally in the middle
        Button2.configure(bg="red")
        Button5.configure(bg="red")
        Button8.configure(bg="red")

        messagebox.showinfo("O wins!")
        window.destroy()
    
    if Button3["text"] == "O" and Button6["text"] == "O" and Button9["text"] == "O": #Same thing as before horizontally at the end
        Button3.configure(bg="red")
        Button6.configure(bg="red")
        Button9.configure(bg="red")

        messagebox.showinfo("O wins!")
        window.destroy()

def ODiagonal(): #O diagonal check function
    if Button1["text"] == "O" and Button5["text"] == "O" and Button9["text"] == "O": #Checks diagonally the buttons to see if they have an "O" text in them
        Button1.configure(bg="red")
        Button5.configure(bg="red")
        Button9.configure(bg="red")

        messagebox.showinfo("O wins!")
        window.destroy()
    
    elif Button7["text"] == "O" and Button5["text"] == "O" and Button3["text"] == "O": #Same thing as before but different location
        Button7.configure(bg="red")
        Button5.configure(bg="red")
        Button3.configure(bg="red")

        messagebox.showinfo("O wins!")
        window.destroy()


Button1 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button1Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal(), ODiagonal()])
Button2 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button2Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal()])
Button3 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button3Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal(), ODiagonal()])

Button4 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button4Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal()])
Button5 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button5Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal(), ODiagonal()])
Button6 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button6Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal()])

Button7 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button7Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal(), ODiagonal()])
Button8 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button8Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal()])
Button9 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button9Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal(), ODiagonal()])

#Creating all of the buttons and binding the various functions to them via the use of the lambda command ^^

#Placing the buttons in their various x,y locations 

Button1.place(x=-1, y=0)
Button2.place(x=-1, y=86)
Button3.place(x=-1, y=172)

Button4.place(x=70, y=0)
Button5.place(x=70, y=86)
Button6.place(x=70, y=172)

Button7.place(x=144, y=0)
Button8.place(x=144, y=86)
Button9.place(x=144, y=172)


window.mainloop()