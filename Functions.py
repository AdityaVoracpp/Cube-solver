from variables import *

saved_scramble = [[[]]]
def U():
    solution.append('U')
    k = 0
    temp = Cube[k][0][2]
    Cube[k][0][2] = Cube[k][0][0]
    Cube[k][0][0] = Cube[k][2][0]
    Cube[k][2][0] = Cube[k][2][2]
    Cube[k][2][2] = temp
    temp = Cube[k][0][1]
    Cube[k][0][1] = Cube[k][1][0]
    Cube[k][1][0] = Cube[k][2][1]
    Cube[k][2][1] = Cube[k][1][2]
    Cube[k][1][2] = temp
    temp = Cube[1][0][0]
    Cube[1][0][0] = Cube[2][0][0]
    Cube[2][0][0] = Cube[3][0][0]
    Cube[3][0][0] = Cube[4][0][0]
    Cube[4][0][0] = temp
    temp = Cube[1][0][2]
    Cube[1][0][2] = Cube[2][0][2]
    Cube[2][0][2] = Cube[3][0][2]
    Cube[3][0][2] = Cube[4][0][2]
    Cube[4][0][2] = temp
    temp = Cube[1][0][1]
    Cube[1][0][1] = Cube[2][0][1]
    Cube[2][0][1] = Cube[3][0][1]
    Cube[3][0][1] = Cube[4][0][1]
    Cube[4][0][1] = temp
def U2():
    U()
    U()
def UI():
    U()
    U()
    U()
def R():
    solution.append('R')
    k = 4
    temp = Cube[k][0][2]
    Cube[k][0][2] = Cube[k][0][0]
    Cube[k][0][0] = Cube[k][2][0]
    Cube[k][2][0] = Cube[k][2][2]
    Cube[k][2][2] = temp
    temp = Cube[k][0][1]
    Cube[k][0][1] = Cube[k][1][0]
    Cube[k][1][0] = Cube[k][2][1]
    Cube[k][2][1] = Cube[k][1][2]
    Cube[k][1][2] = temp
    temp = Cube[3][0][2]
    Cube[3][0][2] = Cube[5][0][2]
    Cube[5][0][2] = Cube[1][2][0]
    Cube[1][2][0] = Cube[0][0][2]
    Cube[0][0][2] = temp
    temp = Cube[3][2][2]
    Cube[3][2][2] = Cube[5][2][2]
    Cube[5][2][2] = Cube[1][0][0]
    Cube[1][0][0] = Cube[0][2][2]
    Cube[0][2][2] = temp
    temp = Cube[3][1][2]
    Cube[3][1][2] = Cube[5][1][2]
    Cube[5][1][2] = Cube[1][1][0]
    Cube[1][1][0] = Cube[0][1][2]
    Cube[0][1][2] = temp
def R2():
    R()
    R()
def RI():
    R()
    R()
    R()
def F():
    solution.append('F')
    k = 3
    temp = Cube[k][0][2]
    Cube[k][0][2] = Cube[k][0][0]
    Cube[k][0][0] = Cube[k][2][0]
    Cube[k][2][0] = Cube[k][2][2]
    Cube[k][2][2] = temp
    temp = Cube[k][0][1]
    Cube[k][0][1] = Cube[k][1][0]
    Cube[k][1][0] = Cube[k][2][1]
    Cube[k][2][1] = Cube[k][1][2]
    Cube[k][1][2] = temp
    temp = Cube[2][0][2]
    Cube[2][0][2] = Cube[5][0][0]
    Cube[5][0][0] = Cube[4][2][0]
    Cube[4][2][0] = Cube[0][2][2]
    Cube[0][2][2] = temp
    temp = Cube[2][2][2]
    Cube[2][2][2] = Cube[5][0][2]
    Cube[5][0][2] = Cube[4][0][0]
    Cube[4][0][0] = Cube[0][2][0]
    Cube[0][2][0] = temp
    temp = Cube[2][1][2]
    Cube[2][1][2] = Cube[5][0][1]
    Cube[5][0][1] = Cube[4][1][0]
    Cube[4][1][0] = Cube[0][2][1]
    Cube[0][2][1] = temp
def F2():
    F()
    F()
def FI():
    F()
    F()
    F()
def D():
    solution.append('D')
    k = 5
    temp = Cube[k][0][2]
    Cube[k][0][2] = Cube[k][0][0]
    Cube[k][0][0] = Cube[k][2][0]
    Cube[k][2][0] = Cube[k][2][2]
    Cube[k][2][2] = temp
    temp = Cube[k][0][1]
    Cube[k][0][1] = Cube[k][1][0]
    Cube[k][1][0] = Cube[k][2][1]
    Cube[k][2][1] = Cube[k][1][2]
    Cube[k][1][2] = temp
    temp = Cube[3][2][0]
    Cube[3][2][0] = Cube[2][2][0]
    Cube[2][2][0] = Cube[1][2][0]
    Cube[1][2][0] = Cube[4][2][0]
    Cube[4][2][0] = temp
    temp = Cube[3][2][2]
    Cube[3][2][2] = Cube[2][2][2]
    Cube[2][2][2] = Cube[1][2][2]
    Cube[1][2][2] = Cube[4][2][2]
    Cube[4][2][2] = temp
    temp = Cube[3][2][1]
    Cube[3][2][1] = Cube[2][2][1]
    Cube[2][2][1] = Cube[1][2][1]
    Cube[1][2][1] = Cube[4][2][1]
    Cube[4][2][1] = temp
def DI():
    D()
    D()
    D()
def D2():
    D()
    D()
def L():
    solution.append('L')
    k = 2
    temp = Cube[k][0][2]
    Cube[k][0][2] = Cube[k][0][0]
    Cube[k][0][0] = Cube[k][2][0]
    Cube[k][2][0] = Cube[k][2][2]
    Cube[k][2][2] = temp
    temp = Cube[k][0][1]
    Cube[k][0][1] = Cube[k][1][0]
    Cube[k][1][0] = Cube[k][2][1]
    Cube[k][2][1] = Cube[k][1][2]
    Cube[k][1][2] = temp
    temp = Cube[3][0][0]
    Cube[3][0][0] = Cube[0][0][0]
    Cube[0][0][0] = Cube[1][2][2]
    Cube[1][2][2] = Cube[5][0][0]
    Cube[5][0][0] = temp
    temp = Cube[3][2][0]
    Cube[3][2][0] = Cube[0][2][0]
    Cube[0][2][0] = Cube[1][0][2]
    Cube[1][0][2] = Cube[5][2][0]
    Cube[5][2][0] = temp
    temp = Cube[3][1][0]
    Cube[3][1][0] = Cube[0][1][0]
    Cube[0][1][0] = Cube[1][1][2]
    Cube[1][1][2] = Cube[5][1][0]
    Cube[5][1][0] = temp
def L2():
    L()
    L()
def LI():
    L()
    L()
    L()
def B():
    solution.append('B')
    k = 1
    temp = Cube[k][0][2]
    Cube[k][0][2] = Cube[k][0][0]
    Cube[k][0][0] = Cube[k][2][0]
    Cube[k][2][0] = Cube[k][2][2]
    Cube[k][2][2] = temp
    temp = Cube[k][0][1]
    Cube[k][0][1] = Cube[k][1][0]
    Cube[k][1][0] = Cube[k][2][1]
    Cube[k][2][1] = Cube[k][1][2]
    Cube[k][1][2] = temp
    temp = Cube[2][0][0]
    Cube[2][0][0] = Cube[0][0][2]
    Cube[0][0][2] = Cube[4][2][2]
    Cube[4][2][2] = Cube[5][2][0]
    Cube[5][2][0] = temp
    temp = Cube[2][2][0]
    Cube[2][2][0] = Cube[0][0][0]
    Cube[0][0][0] = Cube[4][0][2]
    Cube[4][0][2] = Cube[5][2][2]
    Cube[5][2][2] = temp
    temp = Cube[2][1][0]
    Cube[2][1][0] = Cube[0][0][1]
    Cube[0][0][1] = Cube[4][1][2]
    Cube[4][1][2] = Cube[5][2][1]
    Cube[5][2][1] = temp
def B2():
    B()
    B()
def BI():
    B()
    B()
    B()


def FRcorner():
    while not (Cube[5][0][2] == 5 and Cube[3][2][2] == 3):
        R()
        U()
        RI()
        UI()
def FLcorner():
    while not (Cube[5][0][0] == 5 and Cube[3][2][0] == 3):
        LI()
        UI()
        L()
        U()
def BRcorner():
    while not (Cube[5][2][2] == 5 and Cube[1][2][0] == 1):
        RI()
        UI()
        R()
        U()
def BLcorner():
    while not (Cube[5][2][0] == 5 and Cube[1][2][2] == 1):
        L()
        U()
        LI()
        UI()

def pre_error_handler():

    for k in range(6):
        for i in range(3):
            for j in range(3):
                if Cube[k][i][j] == -1:
                    return "There are some unfilled tiles!"
    return "success"

def post_error_handler():
    if Cube != Solved_Cube:
        return "This combination is Unsolvable, Please check for mistakes and try again!"
    else:
        return "success"


