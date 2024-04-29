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

def getSecondCalc(fc, sc, num1, num2, num3):
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



sb = board(None, None, None, None, 5, None, None, None, None)

boardsArray = []
solveFirstRow(sb, "+", "+", 6)

solveColumn(boardsArray, "-", "*", 8, 1)
solveColumn(boardsArray, "+", "-", 1, 2)
solveColumn(boardsArray, "*", "+", 5, 3)

delBadBoards(boardsArray,"-","+","+","+","+","-",4,6,6)

print(f"Lehetséges jó válaszok: {len(boardsArray)}\n")
for i in range(len(boardsArray)):
    print(f"{i+1}:")
    print(boardsArray[i])