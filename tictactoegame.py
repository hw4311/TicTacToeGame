from tkinter import *

window = Tk()
window.title("TicTacToe")
window.geometry("220x250")

Moves = 1

def TurnClicked():
    global Moves
    if Moves == 1:
        Moves = 2
        return "X"
    elif Moves == 2:
        Moves = 1
        return "O"
        

def Button1Clicked():
    global Moves
    if Button1["text"] == "": 
     Button1["text"] = TurnClicked()

def Button2Clicked():
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

def Vertical():
    if Button1["text"] == "X" and Button2["text"] == "X" and Button3["text"] == "X":
        Button1.configure(bg="green")
        Button2.configure(bg="green")
        Button3.configure(bg="green")
    
    elif Button4["text"] == "X" and Button5["text"] == "X" and Button6["text"] == "X":
        Button4.configure(bg="green")
        Button5.configure(bg="green")
        Button6.configure(bg="green")
    
    if Button7["text"] == "X" and Button8["text"] == "X" and Button9["text"] == "X":
        Button7.configure(bg="green")
        Button8.configure(bg="green")
        Button9.configure(bg="green")

def Horizontal():
    if Button1["text"] == "X" and Button4["text"] == "X" and Button7["text"] == "X":
        Button1.configure(bg="green")
        Button4.configure(bg="green")
        Button7.configure(bg="green")

    elif Button2["text"] == "X" and Button5["text"] == "X" and Button8["text"] == "X":
        Button2.configure(bg="green")
        Button5.configure(bg="green")
        Button8.configure(bg="green")
    
    if Button3["text"] == "X" and Button6["text"] == "X" and Button9["text"] == "X":
        Button3.configure(bg="green")
        Button6.configure(bg="green")
        Button9.configure(bg="green")

def Diagonal():
    if Button1["text"] == "X" and Button5["text"] == "X" and Button9["text"] == "X":
        Button1.configure(bg="green")
        Button5.configure(bg="green")
        Button9.configure(bg="green")
    
    elif Button7["text"] == "X" and Button5["text"] == "X" and Button3["text"] == "X":
        Button7.configure(bg="green")
        Button5.configure(bg="green")
        Button3.configure(bg="green")

def OVertical():
    if Button1["text"] == "O" and Button2["text"] == "O" and Button3["text"] == "O":
        Button1.configure(bg="red")
        Button2.configure(bg="red")
        Button3.configure(bg="red")
    
    elif Button4["text"] == "O" and Button5["text"] == "O" and Button6["text"] == "O":
        Button4.configure(bg="red")
        Button5.configure(bg="red")
        Button6.configure(bg="red")
    
    if Button7["text"] == "O" and Button8["text"] == "O" and Button9["text"] == "O":
        Button7.configure(bg="red")
        Button8.configure(bg="red")
        Button9.configure(bg="red")

def OHorizontal():
    if Button1["text"] == "O" and Button4["text"] == "O" and Button7["text"] == "O":
        Button1.configure(bg="red")
        Button4.configure(bg="red")
        Button7.configure(bg="red")

    elif Button2["text"] == "O" and Button5["text"] == "O" and Button8["text"] == "O":
        Button2.configure(bg="red")
        Button5.configure(bg="red")
        Button8.configure(bg="red")
    
    if Button3["text"] == "O" and Button6["text"] == "O" and Button9["text"] == "O":
        Button3.configure(bg="red")
        Button6.configure(bg="red")
        Button9.configure(bg="red")

def ODiagonal():
    if Button1["text"] == "O" and Button5["text"] == "O" and Button9["text"] == "O":
        Button1.configure(bg="red")
        Button5.configure(bg="red")
        Button9.configure(bg="red")
    
    elif Button7["text"] == "O" and Button5["text"] == "O" and Button3["text"] == "O":
        Button7.configure(bg="red")
        Button5.configure(bg="red")
        Button3.configure(bg="red")

Button1 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button1Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal(), ODiagonal()])
Button2 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button2Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal()])
Button3 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button3Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal(), ODiagonal()])

Button4 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button4Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal()])
Button5 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button5Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal(), ODiagonal()])
Button6 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button6Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal()])

Button7 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button7Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal(), ODiagonal()])
Button8 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button8Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal()])
Button9 = Button(window, text= "", font=("Arial", 15), height=3, width=6, bg="white", command=lambda:[Button9Clicked(), Vertical(), Horizontal(), OVertical(), OHorizontal(), Diagonal(), ODiagonal()])

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