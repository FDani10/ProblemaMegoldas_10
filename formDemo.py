from tkinter import *
from PIL import Image,ImageTk
import ctypes

class board:
    def __init__(self, n11, n12, n13, n21, n22, n23, n31, n32, n33):
        self.r11 = n11
        self.r12 = n12
        self.r13 = n13
        self.r21 = n21
        self.r22 = n22
        self.r23 = n23
        self.r31 = n31
        self.r32 = n32
        self.r33 = n33

    def __str__(self):
        return f"{self.r11} | {self.r12} | {self.r13}\n{self.r21} | {self.r22} | {self.r23}\n{self.r31} | {self.r32} | {self.r33}\n"

def charOnLabel(char,om):
    text = Label(om,text=f"{variables[char].get()}",font=('Ariel',25),bg="#FFBCBC",justify="center")
    text.place(x=30,y=15,width=18,height=40)

def numOnLabel(char,om):
    text = Label(om,text=f"{variables[char].get()}",font=('Ariel',25),bg="#AEFFA7",justify="center")
    text.place(x=30,y=15,width=18,height=40)

def whiteOnLabel(char,om):
    text = Label(om,text=f"{variables[char].get()}",font=('Ariel',25),bg="#FFFFFF",justify="center")
    text.place(x=30,y=15,width=18,height=40)

boardsArray = []
root = Tk()

root.geometry("670x714")
root["bg"] = "#BBFBFF"

# Define options
chars = [' ','/', '*', '-', '+']
numbers = [' ',0,1,2,3,4,5,6,7,8,9]

image=Image.open(f'./pics/grayBlock.png')
grayBlock=ImageTk.PhotoImage(image)
image2=Image.open(f'./pics/pinkCircle.png')
pickCircle=ImageTk.PhotoImage(image2)
image3=Image.open(f'./pics/whiteBlock.png')
whiteBlock=ImageTk.PhotoImage(image3)
image4=Image.open(f'./pics/greenBlock.png')
greenBlock=ImageTk.PhotoImage(image4)

# ROW 1
variables = []
inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=20,y=10)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om1 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(0,om1))
om1.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om1.place(x=108,y=10)

inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=196,y=10)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om2 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(1,om2))
om2.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om2.place(x=284,y=10)

inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=372,y=10)

inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=460,y=10,width=50)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz1 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(2,sz1))
sz1.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz1.place(x=520,y=10)

# ROW 2
variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om3 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(3,om3))
om3.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om3.place(x=20,y=108)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om4 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(4,om4))
om4.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om4.place(x=196,y=108)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om5 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(5,om5))
om5.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om5.place(x=372,y=108)


# ROW 3
inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=20,y=196)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om6 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(6,om6))
om6.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om6.place(x=108,y=196)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
wb = OptionMenu(root, variable, *numbers, command= lambda e:whiteOnLabel(7,wb))
wb.config(image=whiteBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
wb.place(x=196,y=196)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om7 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(8,om7))
om7.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om7.place(x=284,y=196)

inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=372,y=196)

inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=460,y=196,width=50)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz2 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(9,sz2))
sz2.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz2.place(x=520,y=196)

# ROW 4
variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om8 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(10,om8))
om8.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om8.place(x=20,y=284)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om9 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(11,om9))
om9.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om9.place(x=196,y=284)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om10 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(12,om10))
om10.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om10.place(x=372,y=284)

# ROW 5
inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=20,y=372)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om11 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(13,om11))
om11.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om11.place(x=108,y=372)

inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=196,y=372)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om12 = OptionMenu(root, variable, *chars, command= lambda e:charOnLabel(14,om12))
om12.config(image=pickCircle,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
om12.place(x=284,y=372)

inputtxt = Label(root, image=grayBlock)
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=372,y=372)

inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=460,y=372,width=50)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz3 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(15,sz3))
sz3.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz3.place(x=520,y=372)


# ROW 6
inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=35,y=460,width=50,height=25)

inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=211,y=460,width=50,height=25)

inputtxt = Label(root, text="=",font=('Ariel',50),justify="center")
inputtxt["bg"] = "#BBFBFF"
inputtxt.place(x=387,y=460,width=50,height=25)
# ROW 7
variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz4 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(16,sz4))
sz4.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz4.place(x=20,y=500)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz5 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(17,sz5))
sz5.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz5.place(x=196,y=500)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
sz6 = OptionMenu(root, variable, *numbers, command= lambda e:numOnLabel(18,sz6))
sz6.config(image=greenBlock,border=0,indicatoron=False,font=('Ariel',20),bg="#BBFBFF",highlightthickness=0,activebackground="#BBFBFF")
sz6.place(x=372,y=500)


# Solver
def getSecondCalc(fc, sc, num1, num2, num3):
    try:
        firstCalculation = 0
        match fc:
            case "/":
                firstCalculation = num1 / num2
            case "*":
                firstCalculation = num1 * num2
            case "+":
                firstCalculation = num1 + num2
            case "-":
                firstCalculation = num1 - num2
        secondCalculation = 0
        match sc:
            case "/":
                secondCalculation = firstCalculation / num3
            case "*":
                secondCalculation = firstCalculation * num3
            case "+":
                secondCalculation = firstCalculation + num3
            case "-":
                secondCalculation = firstCalculation - num3
        return secondCalculation
    except ZeroDivisionError:
        return 69

def solveFirstRow(startBoard, firstC, secondC, answer):
    start1 = 0
    start2 = 0
    if firstC == "/": start1 = 1
    if secondC == "/": start2 = 1
    for i in range(start1,10):
        for j in range(start2,10):
            if getSecondCalc(firstC, secondC, i, startBoard.r22, j) == answer:
                b = board(startBoard.r11,startBoard.r12,startBoard.r13,i,startBoard.r22,j,startBoard.r31,startBoard.r32,startBoard.r33)
                boardsArray.append(b)

def solveColumn(boards, fc, sc, a, colNum):
    global boardsArray
    goodboards = []
    start1 = 0
    start2 = 0
    if fc == "/": start1 = 1
    if sc == "/": start2 = 1
    match colNum:
        case 1:
            for i in range(0,len(boards)):
                for j in range(start1,10):
                    for k in range(start2,10):
                        if getSecondCalc(fc, sc, j, boards[i].r21, k) == a:
                            b = board(j,boards[i].r12,boards[i].r13,boards[i].r21,boards[i].r22,boards[i].r23,k,boards[i].r32,boards[i].r33)
                            goodboards.append(b)
        case 2:
            for i in range(0,len(boards)):
                for j in range(start1,10):
                    for k in range(start2,10):
                        if getSecondCalc(fc, sc, j, boards[i].r22, k) == a:
                            b = board(boards[i].r11,j,boards[i].r13,boards[i].r21,boards[i].r22,boards[i].r23,boards[i].r31,k,boards[i].r33)
                            goodboards.append(b)
        case 3:
            for i in range(0,len(boards)):
                for j in range(start1,10):
                    for k in range(start2,10):
                        if getSecondCalc(fc, sc, j, boards[i].r23, k) == a:
                            b = board(boards[i].r11,boards[i].r12,j,boards[i].r21,boards[i].r22,boards[i].r23,boards[i].r31,boards[i].r32,k)
                            goodboards.append(b)
    unique = []
    for i in range(0,len(goodboards)):
        benne = False
        for j in range(0,len(unique)):
            if unique[j].__dict__ == goodboards[i].__dict__:
                benne = True
        if benne == False:
            unique.append(goodboards[i])
    boardsArray = unique

def delBadBoards(boards,c11,c12,c21,c22,c31,c32,a1,a2,a3):
    global boardsArray
    goodboards = []
    for i in range(len(boards)):
        if ((getSecondCalc(c11,c12,boards[i].r11,boards[i].r12,boards[i].r13) == a1) and
            (getSecondCalc(c21,c22,boards[i].r21,boards[i].r22,boards[i].r23) == a2) and
            (getSecondCalc(c31,c32,boards[i].r31,boards[i].r32,boards[i].r33) == a3)):
                goodboards.append(boards[i])
    unique = []
    for i in range(0,len(goodboards)):
        benne = False
        for j in range(0,len(unique)):
            if unique[j].__dict__ == goodboards[i].__dict__:
                benne = True
        if benne == False:
            unique.append(goodboards[i])
    boardsArray = unique

def szamolj():
    global boardsArray
    boardsArray = []
    megvan = True
    for i in range(len(variables)):
        if variables[i].get() == " ":
            megvan = False

    if megvan:
        sb = board(None, None, None, None, int(variables[7].get()), None, None, None, None)

        solveFirstRow(sb, variables[6].get(), variables[8].get(), int(variables[9].get()))

        solveColumn(boardsArray, variables[3].get(), variables[10].get(), int(variables[16].get()), 1)
        solveColumn(boardsArray, variables[4].get(), variables[11].get(), int(variables[17].get()), 2)
        solveColumn(boardsArray, variables[5].get(), variables[12].get(), int(variables[18].get()), 3)

        delBadBoards(boardsArray,variables[0].get(),variables[1].get(),variables[6].get(),variables[8].get(),variables[13].get(),variables[14].get(),int(variables[2].get()),int(variables[9].get()),int(variables[15].get()))

        print(f"Lehetséges jó válaszok: {len(boardsArray)}\n")
        for i in range(len(boardsArray)):
            print(f"{i+1}:")
            print(boardsArray[i])
    else:
        ctypes.windll.user32.MessageBoxW(0, "Töltsön ki minden mezőt!", "Hiba!", 0)

image_btn=Image.open(f'./pics/megoldasBtn.png')
solveBtn=ImageTk.PhotoImage(image_btn)
btn = Button(root, command=szamolj, image=solveBtn)
btn["bg"] = "#BBFBFF"
btn["activebackground"] = "#BBFBFF"
btn["border"] = "0"
btn.place(x=500,y=500)

root.mainloop()