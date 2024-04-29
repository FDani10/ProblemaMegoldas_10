from tkinter import *

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

boardsArray = []
root = Tk()

# Define options
chars = ['/', '*', '-', '+']  # Example values, replace with your options
numbers = [0,1,2,3,4,5,6,7,8,9]  # Example values, replace with your options

# ROW 1
variables = []
for i in range(2):
    inputtxt = Text(root, height=3, width=6, bg="lightgray", borderwidth=5, state=DISABLED)
    inputtxt.grid(column=i*2+1, row=1, padx=10, pady=10)

    variable = StringVar(root)
    variable.set(' ')
    variables.append(variable)
    om = OptionMenu(root, variable, *chars)
    om.config(width=6, height=3, bg="lightgray")
    om.grid(column=i*2+2, row=1, padx=10, pady=10)

inputtxt = Text(root, height=3, width=6, bg="lightgray", borderwidth=5, state=DISABLED)
inputtxt.grid(column=5, row=1, padx=10, pady=10)

inputtxt = Text(root, height=3, width=6, bg="lightgray", borderwidth=5)
inputtxt.tag_configure("center", justify=CENTER)
inputtxt.insert(INSERT, "=")
inputtxt.tag_add("center", "1.0", "end")
inputtxt.config(state=DISABLED)
inputtxt.grid(column=6, row=1, padx=10, pady=10)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om = OptionMenu(root, variable, *numbers)
om.config(width=6, height=3, bg="lightgray")
om.grid(column=7, row=1, padx=10, pady=10)



# ROW 2
for i in range(3):
    variable = StringVar(root)
    variable.set(' ')
    variables.append(variable)
    om = OptionMenu(root, variable, *chars)
    om.config(width=6, height=3, bg="lightgray")
    om.grid(column=i*2+1, row=2, padx=10, pady=10)


# ROW 3
for i in range(2):
    if i != 1:
        inputtxt = Text(root, height=3, width=6, bg="lightgray", borderwidth=5, state=DISABLED)
        inputtxt.grid(column=i*2+1, row=3, padx=10, pady=10)
    else:
        variable = StringVar(root)
        variable.set(' ')
        variables.append(variable)
        om = OptionMenu(root, variable, *numbers)
        om.config(width=6, height=3, bg="lightgray")
        om.grid(column=i*2+1, row=3, padx=10, pady=10)


    variable = StringVar(root)
    variable.set(' ')
    variables.append(variable)
    om = OptionMenu(root, variable, *chars)
    om.config(width=6, height=3, bg="lightgray")
    om.grid(column=i*2+2, row=3, padx=10, pady=10)

inputtxt = Text(root, height=3, width=6, bg="lightgray", borderwidth=5, state=DISABLED)
inputtxt.grid(column=5, row=3, padx=10, pady=10)

inputtxt = Text(root, height=3, width=6, bg="lightgray", borderwidth=5)
inputtxt.tag_configure("center", justify=CENTER)
inputtxt.insert(INSERT, "=")
inputtxt.tag_add("center", "1.0", "end")
inputtxt.config(state=DISABLED)
inputtxt.grid(column=6, row=3, padx=10, pady=10)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om = OptionMenu(root, variable, *numbers)
om.config(width=6, height=3, bg="lightgray")
om.grid(column=7, row=3, padx=10, pady=10)



# ROW 4
for i in range(3):
    variable = StringVar(root)
    variable.set(' ')
    variables.append(variable)
    om = OptionMenu(root, variable, *chars)
    om.config(width=6, height=3, bg="lightgray")
    om.grid(column=i*2+1, row=4, padx=10, pady=10)




# ROW 5
for i in range(2):
    inputtxt = Text(root, height=3, width=6, bg="lightgray", borderwidth=5, state=DISABLED)
    inputtxt.grid(column=i*2+1, row=5, padx=10, pady=10)

    variable = StringVar(root)
    variable.set(' ')
    variables.append(variable)
    om = OptionMenu(root, variable, *chars)
    om.config(width=6, height=3, bg="lightgray")
    om.grid(column=i*2+2, row=5, padx=10, pady=10)

inputtxt = Text(root, height=3, width=6, bg="lightgray", borderwidth=5, state=DISABLED)
inputtxt.grid(column=5, row=5, padx=10, pady=10)

inputtxt = Text(root, height=3, width=6, bg="lightgray", borderwidth=5)
inputtxt.tag_configure("center", justify=CENTER)
inputtxt.insert(INSERT, "=")
inputtxt.tag_add("center", "1.0", "end")
inputtxt.config(state=DISABLED)
inputtxt.grid(column=6, row=5, padx=10, pady=10)

variable = StringVar(root)
variable.set(' ')
variables.append(variable)
om = OptionMenu(root, variable, *numbers)
om.config(width=6, height=3, bg="lightgray")
om.grid(column=7, row=5, padx=10, pady=10)


# ROW 6
for i in range(3):
    inputtxt = Text(root, height=3, width=6, bg="lightgray", borderwidth=5)
    inputtxt.tag_configure("center", justify=CENTER)
    inputtxt.insert(INSERT, "=")
    inputtxt.tag_add("center", "1.0", "end")
    inputtxt.config(state=DISABLED)
    inputtxt.grid(column=i*2+1, row=6, padx=10, pady=10)

# ROW 7
for i in range(3):
    variable = StringVar(root)
    variable.set(' ')
    variables.append(variable)
    om = OptionMenu(root, variable, *numbers)
    om.config(width=6, height=3, bg="lightgray")
    om.grid(column=i*2+1, row=7, padx=10, pady=10)



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
        print(f"{i}: {variables[i].get()}")
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
        print("Tölts ki minden mezőt!")

btn = Button(root, text="Nyomod fasz xd", command=szamolj)
btn.grid(column=4,row=8,padx=10,pady=10)
root.mainloop()