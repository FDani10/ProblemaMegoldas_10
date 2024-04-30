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
