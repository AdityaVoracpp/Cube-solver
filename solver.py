from tkinter import *

Cube = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]], [[4, 4, 4], [4, 4, 4], [4, 4, 4]], [[5, 5, 5], [5, 5, 5], [5, 5, 5]]]

# def wchosen():
# def wchosen():
# def wchosen():
# def wchosen():
# def wchosen():
# def wchosen():

def color_chooser():
    color_window = Toplevel()
    color_window.config(bg= "black")

    color_frame = Frame(color_window, bg="#5476b8")
    color_frame.pack()

    chose_white = Button(color_frame, padx=20, pady=15, bg="white",command = wchosen).grid(row=0,column=0, padx=15, pady=15)
    chose_blue = Button(color_frame, padx=20, pady=15,bg="blue",command = bchosen).grid(row=0,column=1, padx=15, pady=15)
    chose_orange = Button(color_frame, padx=20, pady=15,bg="orange",command = ochosen).grid(row=0,column=2, padx=15, pady=15)
    chose_green = Button(color_frame, padx=20, pady=15, bg="green",command = gchosen).grid(row=1,column=0, padx=15, pady=15)
    chose_red = Button(color_frame, padx=20, pady=15, bg="red",command = rchosen).grid(row=1,column=1, padx=15, pady=15)
    chose_yellow = Button(color_frame, padx=20, pady=15, bg="yellow",command = ychosen).grid(row=1,column=2, padx=15, pady=15)




mainwin = Tk()

screen_height = mainwin.winfo_screenheight()
screen_width = mainwin.winfo_screenwidth()

mainwin.geometry(str(screen_width)+"x"+str(screen_width))
mainwin.config(background="black")

frame = Frame(mainwin,bg="black")
frame.place(x=150, y=150)

#creating buttons
wr1buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
wr2buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
wr3buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]

whitebuttons = [wr1buttons, wr2buttons, wr3buttons]

br1buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
br2buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
br3buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]

bluebuttons = [br1buttons, br2buttons, br3buttons]

or1buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
or2buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
or3buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]

orangebuttons = [or1buttons, or2buttons, or3buttons]

gr1buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
gr2buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
gr3buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]

greenbuttons = [gr1buttons, gr2buttons, gr3buttons]

rr1buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
rr2buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
rr3buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]

redbuttons = [rr1buttons, rr2buttons, rr3buttons]

yr1buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
yr2buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]
yr3buttons = [Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15), Button(frame,padx=20,pady=15)]

yellowbuttons = [yr1buttons, yr2buttons, yr3buttons]

allbuttons = [whitebuttons, bluebuttons, orangebuttons, greenbuttons, redbuttons, yellowbuttons]

#buttons created


#button changer color wisee
for i in range(3):
    for j in range(3):
        whitebuttons[i][j].grid(row=i,column=j+3)
for i in range(3):
    for j in range(3):
        orangebuttons[i][j].grid(row=i+3,column=j)
for i in range(3):
    for j in range(3):
        greenbuttons[i][j].grid(row=i+3,column=j+3)
for i in range(3):
    for j in range(3):
        redbuttons[i][j].grid(row=i+3,column=j+6)
for i in range(3):
    for j in range(3):
        bluebuttons[i][j].grid(row=i+3,column=j+9)
for i in range(3):
    for j in range(3):
        yellowbuttons[i][j].grid(row=i+6,column=j+3)

#change all buttons here
for i in range(6):
    for j in range(3):
        for k in range(3):
            allbuttons[i][j][k].config(command=color_chooser)








mainwin.mainloop()














def U():

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

def Solve():
    #cross
    while not (Cube[0][0][1] == 5 and Cube[0][1][2] == 5 and Cube[0][2][1] == 5 and Cube[0][1][0] == 5):
        if Cube[1][1][0] == 5:
            while Cube[0][1][2] == 5:
                U()
            RI()
        if Cube[1][1][2] == 5:
            while Cube[0][1][0] == 5:
                U()
            L()
        if Cube[3][1][2] == 5:
            while Cube[0][1][2] == 5:
                U()
            R()
        if Cube[3][1][0] == 5:
            while Cube[0][1][0] == 5:
                U()
            LI()
        if Cube[2][1][2] == 5:
            while Cube[0][2][1] == 5:
                U()
            F()
        if Cube[2][1][0] == 5:
            while Cube[0][0][1] == 5:
                U()
            BI()
        if Cube[4][1][2] == 5:
            while Cube[0][0][1] == 5:
                U()
            B()
        if Cube[4][1][0] == 5:
            while Cube[0][2][1] == 5:
                U()
            FI()
        if Cube[5][0][1] == 5:
            while Cube[0][2][1] == 5:
                U()
            F2()
        if Cube[5][1][2] == 5:
            while Cube[0][1][2] == 5:
                U()
            R2()
        if Cube[5][2][1] == 5:
            while Cube[0][0][1] == 5:
                U()
            B2()
        if Cube[5][1][0] == 5:
            while Cube[0][1][0] == 5:
                U()
            L2()
        if Cube[1][0][1] == 5:
            BI()
            U()
            RI()
        if Cube[2][0][1] == 5:
            L()
            UI()
            F()
        if Cube[3][0][1] == 5:
            F()
            UI()
            R()
        if Cube[4][0][1] == 5:
            RI()
            U()
            FI()
        if Cube[1][2][1] == 5:
            while Cube[0][0][1] == 5:
                U()
            BI()
            UI()
            L()
        if Cube[2][2][1] == 5:
            while Cube[0][1][0] == 5:
                U()
            LI()
            UI()
            F()
        if Cube[3][2][1] == 5:
            while Cube[0][2][1] == 5:
                U()
            F()
            U()
            LI()
        if Cube[4][2][1] == 5:
            while Cube[0][1][2] == 5:
                U()
            R()
            U()
            FI()
    while not (Cube[1][1][1] == Cube[1][0][1] and Cube[0][0][1] == 5):
        U()
    B2()
    while not (Cube[2][1][1] == Cube[2][0][1] and Cube[0][1][0] == 5):
        U()
    L2()
    while not (Cube[3][1][1] == Cube[3][0][1] and Cube[0][2][1] == 5):
        U()
    F2()
    while not (Cube[4][1][1] == Cube[4][0][1] and Cube[0][1][2] == 5):
        U()
    R2()

#corners

    while not (Cube[5][0][0] == 5 and Cube[5][0][2] == 5 and Cube[5][2][0] == 5 and Cube[5][2][2] == 5 and Cube[1][2][
        2] == 1 and Cube[2][2][2] == 2 and Cube[3][2][2] == 3):
        while Cube[0][0][0] == 5 or Cube[0][0][2] == 5 or Cube[0][2][0] == 5 or Cube[0][2][2] == 5:
            if Cube[0][0][2] == 5:
                UI()
            elif Cube[0][2][0] == 5:
                U()
            elif Cube[0][2][2] == 5:
                U2()
            flag = 1
            for k in range(1, 4):
                if Cube[k][0][2] == k + 1:
                    break
                UI()
                flag += 1
            if flag == 1:
                BLcorner()
            elif flag == 2:
                FLcorner()
            elif flag == 3:
                FRcorner()
            else:
                BRcorner()
        while Cube[1][0][0] == 5 or Cube[2][0][0] == 5 or Cube[3][0][0] == 5 or Cube[4][0][0] == 5:
            if Cube[1][0][0] == 5:
                UI()
            elif Cube[3][0][0] == 5:
                U()
            elif Cube[4][0][0] == 5:
                U2()
            flag = 1
            for k in range(1, 4):
                if Cube[k][0][2] == k:
                    break
                UI()
                flag += 1
            if flag == 1:
                BLcorner()
            elif flag == 2:
                FLcorner()
            elif flag == 3:
                FRcorner()
            else:
                BRcorner()
        while Cube[1][0][2] == 5 or Cube[2][0][2] == 5 or Cube[3][0][2] == 5 or Cube[4][0][2] == 5:
            if Cube[1][0][2] == 5:
                U()
            elif Cube[2][0][2] == 5:
                U2()
            elif Cube[3][0][2] == 5:
                UI()
            flag = 1
            for k in range(1, 4):
                if Cube[k][0][0] == k:
                    break
                UI()
                flag += 1
            if flag == 1:
                BRcorner()
            elif flag == 2:
                BLcorner()
            elif flag == 3:
                FLcorner()
            else:
                FRcorner()
        if not (Cube[5][0][0] == 5 and Cube[3][2][0] == 3):
            LI()
            UI()
            L()
        if not (Cube[5][0][2] == 5 and Cube[3][2][2] == 3):
            R()
            U()
            RI()
        if not (Cube[5][2][0] == 5 and Cube[1][2][2] == 1):
            L()
            U()
            LI()
        if not (Cube[5][2][2] == 5 and Cube[1][2][0] == 1):
            RI()
            UI()
            R()

   #F2L

    while not (Cube[1][1][0] == 1 and Cube[1][1][2] == 1 and Cube[2][1][0] == 2 and Cube[2][1][2] == 2 and Cube[3][1][
        0] == 3 and Cube[3][1][2] == 3 and Cube[4][1][0] == 4 and Cube[4][1][2] == 4):
        if Cube[1][0][1] == 1 and Cube[0][0][1] == 2:
            U()
            L()
            U()
            LI()
            UI()
            BI()
            UI()
            B()
        if Cube[1][0][1] == 1 and Cube[0][0][1] == 4:
            UI()
            RI()
            UI()
            R()
            U()
            B()
            U()
            BI()
        if Cube[2][0][1] == 2 and Cube[0][1][0] == 1:
            UI()
            BI()
            UI()
            B()
            U()
            L()
            U()
            LI()
        if Cube[2][0][1] == 2 and Cube[0][1][0] == 3:
            U()
            F()
            U()
            FI()
            UI()
            LI()
            UI()
            L()
        if Cube[3][0][1] == 3 and Cube[0][2][1] == 2:
            UI()
            LI()
            UI()
            L()
            U()
            F()
            U()
            FI()
        if Cube[3][0][1] == 3 and Cube[0][2][1] == 4:
            U()
            R()
            U()
            RI()
            UI()
            FI()
            UI()
            F()
        if Cube[4][0][1] == 4 and Cube[0][1][2] == 3:
            UI()
            FI()
            UI()
            F()
            U()
            R()
            U()
            RI()
        if Cube[4][0][1] == 4 and Cube[0][1][2] == 1:
            U()
            B()
            U()
            BI()
            UI()
            RI()
            UI()
            R()
        UI()
        if ((Cube[0][0][1] == 0 or Cube[1][0][1] == 0) and (Cube[0][1][2] == 0 or Cube[4][0][1] == 0) and (
                Cube[0][2][1] == 0 or Cube[3][0][1] == 0) and (Cube[0][1][0] == 0 or Cube[2][0][1] == 0)):
            if not (Cube[2][1][2] == 2 and Cube[3][1][0] == 3):
                UI()
                LI()
                UI()
                L()
                U()
                F()
                U()
                FI()
            elif not (Cube[4][1][0] == 4 and Cube[3][1][2] == 3):
                U()
                R()
                U()
                RI()
                UI()
                FI()
                UI()
                F()
            elif not (Cube[4][1][2] == 4 and Cube[1][1][0] == 1):
                UI()
                RI()
                UI()
                R()
                U()
                B()
                U()
                BI()
            elif not (Cube[2][1][0] == 2 and Cube[1][1][2] == 1):
                U()
                L()
                U()
                LI()
                UI()
                BI()
                UI()
                B()

   #oll

    edge_count = 0
    edge_pos = 0
    for i in range(1, 5):
        if Cube[i][0][1] != 0:
            edge_count += 1
            edge_pos += i
    if edge_count == 0:
        R()
        U2()
        R2()
        F()
        R()
        FI()
        U2()
        RI()
        F()
        R()
        FI()
    elif edge_count == 2:
        if edge_pos % 2 == 0:
            while Cube[0][1][0] != 0:
                U()
            F()
            R()
            U()
            RI()
            UI()
            FI()
        else:
            while Cube[0][1][0] != 0 and Cube[0][0][1] == 0:
                U()
            F()
            R()
            U()
            RI()
            UI()
            R()
            U()
            RI()
            UI()
            FI()
    corner_count = 0
    for i in range(2):
        for j in range(2):
            if Cube[0][i * 2][j * 2] == 0:
                corner_count += 1
    if corner_count == 1:
        while Cube[0][0][0] != 0:
            U()
        if Cube[3][0][2] == 0:
            UI()
            R()
            U()
            RI()
            U()
            R()
            U2()
            RI()
        else:
            RI()
            UI()
            R()
            UI()
            RI()
            U2()
            R()
    if corner_count == 2:
        if (Cube[0][0][0] == 0 and Cube[0][2][2] == 0) or (Cube[0][0][2] == 0 and Cube[0][2][0] == 0):
            while Cube[3][0][0] != 0:
                U()
            F()
            RI()
            FI()
            L()
            F()
            R()
            FI()
            LI()
        else:
            while not (Cube[0][0][0] == 0 and Cube[0][0][2] == 0):
                U()
            if Cube[3][0][0] == 0:
                R2()
                D()
                RI()
                U2()
                R()
                DI()
                RI()
                U2()
                RI()
            else:
                U2()
                R()
                U()
                R()
                D()
                RI()
                UI()
                R()
                DI()
                R2()
    if corner_count == 0:
        while not (Cube[2][0][0] == 0 and Cube[2][0][2] == 0):
            U()
        if Cube[3][0][2] == 0:
            R()
            U2()
            R2()
            UI()
            R2()
            UI()
            R2()
            U2()
            R()
        else:
            R()
            U()
            RI()
            U()
            R()
            UI()
            RI()
            U()
            R()
            U2()
            RI()

    #PLL

    headlight = 0
    for i in range(1, 5):
        if Cube[i][0][0] == Cube[i][0][2]:
            headlight += 1
    if headlight == 0:
        RI()
        U()
        RI()
        UI()
        R()
        DI()
        RI()
        D()
        RI()
        U()
        DI()
        R2()
        UI()
        R2()
        D()
        R2()
    elif headlight == 1:
        while Cube[2][0][0] != Cube[2][0][2]:
            U()
        R()
        U()
        RI()
        UI()
        RI()
        F()
        R2()
        UI()
        RI()
        UI()
        R()
        U()
        RI()
        FI()
    bar = 0
    for i in range(1, 5):
        if Cube[i][0][0] == Cube[i][0][1]:
            bar += 1
    if bar == 0:
        while Cube[1][0][0] != 1:
            U()
        if Cube[1][0][1] - Cube[1][0][0] == 2:
            R2()
            U2()
            R()
            U2()
            R2()
            U2()
            R2()
            U2()
            R()
            U2()
            R2()
        elif Cube[3][0][0] == Cube[2][0][1]:
            UI()
            R()
            U()
            RI()
            U()
            RI()
            UI()
            RI()
            U()
            R()
            UI()
            RI()
            UI()
            R2()
            U()
            R()
        else:
            R()
            U()
            RI()
            U()
            RI()
            UI()
            RI()
            U()
            R()
            UI()
            RI()
            UI()
            R2()
            U()
            R()
    if bar == 1:
        while Cube[1][0][0] != Cube[1][0][1]:
            U()
        if Cube[2][0][0] - Cube[4][0][1] == 0:
            R()
            UI()
            R()
            U()
            R()
            U()
            R()
            UI()
            RI()
            UI()
            R2()
        else:
            LI()
            U()
            LI()
            UI()
            LI()
            UI()
            LI()
            U()
            L()
            U()
            L2()
    while Cube[1][0][0] != 1:
        U()
