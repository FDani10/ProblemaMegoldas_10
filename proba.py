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

boards = []

for i in range(0,10):
    for j in range(1,10):
        if(((i + 9) / j) == 2):
            b = board(None,None,None,i,9,j,None,None,None)
            if b not in boards:
                boards.append(b)

for i in range(0,len(boards)):
    for j in range(0,10):
        for k in range(1,10):
            if(((j + boards[i].r21) / k) == 2):
                b = board(j,None,None,boards[i].r21,boards[i].r22,boards[i].r23,k,None,None)
                if b not in boards:
                    boards.append(b)

for i in range(len(boards)-1,-1,-1):
    if boards[i].r11 == None:
        boards.pop(i)   

for i in range(0,len(boards)):
    for j in range(1,10):
        for k in range(1,10):
            if(((boards[i].r31) / j) * k == 2):
                b = board(boards[i].r11,None,None,boards[i].r21,boards[i].r22,boards[i].r23,boards[i].r31,j,k)
                if b not in boards:
                    boards.append(b)

for i in range(len(boards)-1,-1,-1):
    if boards[i].r32 == None:
        boards.pop(i)

for i in range(0,len(boards)):
    for j in range(0,10):
        for k in range(0,10):
            if(((j * (boards[i].r22)) + boards[i].r32) == 2):
                b = board(boards[i].r11,j,None,boards[i].r21,boards[i].r22,boards[i].r23,boards[i].r31,boards[i].r32,boards[i].r33)
                if b not in boards:
                    boards.append(b)

for i in range(len(boards)-1,-1,-1):
    if boards[i].r12 == None:
        boards.pop(i)

for i in range(0,len(boards)):
    for j in range(0,10):
        if(((j / boards[i].r23) + boards[i].r33) == 2):
            b = board(boards[i].r11,boards[i].r12,j,boards[i].r21,boards[i].r22,boards[i].r23,boards[i].r31,boards[i].r32,boards[i].r33)
            if b not in boards:
                boards.append(b)

for i in range(len(boards)-1,-1,-1):
    if boards[i].r13 == None:
        boards.pop(i)

# A nagy befejezés #
for i in range(len(boards)-1,-1,-1):
    if((((boards[i].r11 - boards[i].r12) - boards[i].r13) != 2) or
       (((boards[i].r21 + boards[i].r22) / boards[i].r23) != 2) or
       (((boards[i].r31 / boards[i].r32) * boards[i].r33) != 2) or
       (((boards[i].r11 + boards[i].r21) / boards[i].r31) != 2) or
       (((boards[i].r12 * boards[i].r22) + boards[i].r32) != 2) or
       (((boards[i].r13 / boards[i].r23) + boards[i].r33) != 2)):
        boards.pop(i)

unique = []
for i in range(0,len(boards)):
    benne = False
    for j in range(0,len(unique)):
        if unique[j].__dict__ == boards[i].__dict__:
            benne = True
    if benne == False:
        unique.append(boards[i])

print(f"Lehetséges jó válaszok: {len(unique)}\n")
for i in range(len(unique)):
    print(f"{i+1}:")
    print(unique[i])