import numpy as np
import cv2
from variables import *
from Functions import *
from UI import *

def remove_fours(arr):
    flag = False
    i = 0
    while i <= len(arr) - 4:
        count = 1
        while i + count < len(arr) and arr[i] == arr[i + count]:
            count += 1

        if count >= 4:
            flag = True
            del arr[i:i + 4]
        else:
            i += 1
    if flag:
        return remove_fours(arr)
    else:
        return arr


def simplify(arr):

    remove_fours(arr)

    final_list = []
    i = 0

    while i < len(arr):
        count = 1
        while i + count < len(arr) and arr[i] == arr[i + count]:
            count += 1

        if count == 1:
            final_list.append(arr[i])
        elif count == 2:
            final_list.append(arr[i] + '2')
        elif count == 3:
            final_list.append(arr[i] + '3')

        i += count

    return final_list


def get_colors(allbuttons):
    for k in range(6):
        for i in range(3):
            for j in range(3):
                bg_color = allbuttons[k][i][j].cget("bg")
                if bg_color == "white":
                    Cube[k][i][j] = 0
                elif bg_color == "blue":
                    Cube[k][i][j] = 1
                elif bg_color == "orange":
                    Cube[k][i][j] = 2
                elif bg_color == "green":
                    Cube[k][i][j] = 3
                elif bg_color == "red":
                    Cube[k][i][j] = 4
                elif bg_color == "yellow":
                    Cube[k][i][j] = 5
                else:
                    Cube[k][i][j] = -1


def solve():
    global Solved_Cube
    for i in range(4):
        U()
        if Cube == Solved_Cube:
            return 1
    for i in range(4):
        R()
        if Cube == Solved_Cube:
            return 2
    for i in range(4):
        D()
        if Cube == Solved_Cube:
            return 3
    for i in range(4):
        F()
        if Cube == Solved_Cube:
            return 4
    for i in range(4):
        B()
        if Cube == Solved_Cube:
            return 5
    for i in range(4):
        L()
        if Cube == Solved_Cube:
            return 6

    if not ((Cube[5][0][1] == 5 and Cube[5][1][2] == 5 and Cube[5][2][1] == 5 and Cube[5][1][0] == 5) and (
            Cube[1][2][1] == 1 and Cube[2][2][1] == 2 and Cube[3][2][1] == 3 and Cube[4][2][1] == 4 )):

        max2 = 100
        loop_count2 = 0
        while not (Cube[0][0][1] == 5 and Cube[0][1][2] == 5 and Cube[0][2][1] == 5 and Cube[0][1][0] == 5):

            loop_count2 += 1
            if loop_count2 > max2:
                return 7
            if Cube[1][1][0] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][1][2] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 8
                    U()
                RI()
            if Cube[1][1][2] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][1][0] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 9
                    U()
                L()
            if Cube[3][1][2] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][1][2] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 10
                    U()
                R()
            if Cube[3][1][0] == 5:
                max4 = 100

                loop_count4 = 0
                while Cube[0][1][0] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 11
                    U()
                LI()

            if Cube[2][1][2] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][2][1] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 12
                    U()
                F()
            if Cube[2][1][0] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][0][1] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 13
                    U()
                BI()
            if Cube[4][1][2] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][0][1] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 14
                    U()
                B()
            if Cube[4][1][0] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][2][1] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 15
                    U()
                FI()
            if Cube[5][0][1] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][2][1] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 16
                    U()
                F2()
            if Cube[5][1][2] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][1][2] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 17
                    U()
                R2()
            if Cube[5][2][1] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][0][1] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 18
                    U()
                B2()
            if Cube[5][1][0] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][1][0] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 19
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
                max4 = 100
                loop_count4 = 0
                while Cube[0][0][1] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 20
                    U()
                BI()
                UI()
                L()
            if Cube[2][2][1] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][1][0] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 21
                    U()
                LI()
                UI()
                F()
            if Cube[3][2][1] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][2][1] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 22
                    U()
                F()
                U()
                LI()
            if Cube[4][2][1] == 5:
                max4 = 100
                loop_count4 = 0
                while Cube[0][1][2] == 5:
                    loop_count4 += 1
                    if loop_count4 > max4:
                        return 23
                    U()
                R()
                U()
                FI()

        max2 = 100
        loop_count2 = 0
        while not (Cube[1][1][1] == Cube[1][0][1] and Cube[0][0][1] == 5):
            loop_count2 += 1
            if loop_count2 > max2:
                return 24
            U()
        B2()
        max2 = 100
        loop_count2 = 0
        while not (Cube[2][1][1] == Cube[2][0][1] and Cube[0][1][0] == 5):
            loop_count2 += 1
            if loop_count2 > max2:
                return 25
            U()
        L2()
        max2 = 100
        loop_count2 = 0
        while not (Cube[3][1][1] == Cube[3][0][1] and Cube[0][2][1] == 5):
            loop_count2 += 1
            if loop_count2 > max2:
                return 26
            U()
        F2()
        max2 = 100
        loop_count2 = 0
        while not (Cube[4][1][1] == Cube[4][0][1] and Cube[0][1][2] == 5):
            loop_count2 += 1
            if loop_count2 > max2:
                return 27
            U()
        R2()

    #corners
    max1 = 100

    loop_count1 = 0
    while not (Cube[5][0][0] == 5 and Cube[5][0][2] == 5 and Cube[5][2][0] == 5 and Cube[5][2][2] == 5 and Cube[1][2][
        2] == 1 and Cube[2][2][2] == 2 and Cube[3][2][2] == 3):
        loop_count1 += 1
        if loop_count1 > max1:
            return 28
        max2 = 100
        loop_count2 = 0
        while Cube[0][0][0] == 5 or Cube[0][0][2] == 5 or Cube[0][2][0] == 5 or Cube[0][2][2] == 5:
            loop_count2 += 1
            if loop_count2 > max2:
                return 29
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
        max2 = 100
        loop_count2 = 0
        while Cube[1][0][0] == 5 or Cube[2][0][0] == 5 or Cube[3][0][0] == 5 or Cube[4][0][0] == 5:
            loop_count2 += 1
            if loop_count2 > max2:
                return 30
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
        max2 = 100
        loop_count2 = 0
        while Cube[1][0][2] == 5 or Cube[2][0][2] == 5 or Cube[3][0][2] == 5 or Cube[4][0][2] == 5:
            loop_count2 += 1
            if loop_count2 > max2:
                return 31
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
    max1 = 100
    loop_count1 = 0
    while not (Cube[1][1][0] == 1 and Cube[1][1][2] == 1 and Cube[2][1][0] == 2 and Cube[2][1][2] == 2 and Cube[3][1][
        0] == 3 and Cube[3][1][2] == 3 and Cube[4][1][0] == 4 and Cube[4][1][2] == 4):
        loop_count1 += 1
        if loop_count1 > max1:
            return 32

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
            max3 = 100
            loop_count3 = 0
            while Cube[0][1][0] != 0:
                loop_count3 += 1
                if loop_count3 > max3:
                    return 33
                U()
            F()
            R()
            U()
            RI()
            UI()
            FI()
        else:
            max3 = 100
            loop_count3 = 0
            while not (Cube[0][1][0] == 0 and Cube[0][0][1] == 0):
                loop_count3 += 1
                if loop_count3 > max3:
                    return 34
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
        max2 = 100
        loop_count2 = 0
        while Cube[0][0][0] != 0:
            loop_count2 += 1
            if loop_count2 > max2:
                return 35
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
            max3 = 100
            loop_count3 = 0
            while Cube[3][0][0] != 0:
                loop_count3 += 1
                if loop_count3 > max3:
                    return 36
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
            max3 = 100
            loop_count3 = 0
            while not (Cube[0][0][0] == 0 and Cube[0][0][2] == 0):
                loop_count3 += 1
                if loop_count3 > max3:
                    return 37
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
        max2 = 100
        loop_count2 = 0
        while not (Cube[2][0][0] == 0 and Cube[2][0][2] == 0):
            loop_count2 += 1
            if loop_count2 > max2:
                return 38
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
        max2 = 100
        loop_count2 = 0
        while Cube[2][0][0] != Cube[2][0][2]:
            loop_count2 += 1
            if loop_count2 > max2:
                return 39
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
        max2 = 100
        loop_count2 = 0
        while Cube[1][0][0] != 1:
            loop_count2 += 1
            if loop_count2 > max2:
                return 40
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
        max2 = 100
        loop_count2 = 0
        while Cube[1][0][0] != Cube[1][0][1]:
            loop_count2 += 1
            if loop_count2 > max2:
                return 41
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
    max1 = 100
    loop_count1 = 0
    while Cube[1][0][0] != 1:
        loop_count1 += 1
        if loop_count1 > max1:
            return 42
        U()




def checkerror(allbuttons):

    global result
    global index
    get_colors(allbuttons)
    solution.clear()
    result.clear()
    index = -1

    pre_error = pre_error_handler()
    if pre_error == "success":
        Scrambled_Cube = [[[-1 for _ in range(3)] for _ in range(3)] for _ in range(6)]
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    Scrambled_Cube[i][j][k] = Cube[i][j][k]

        errcode = solve()
        print(errcode)

        x = simplify(solution)

        for i in x:
            result.append(i)

        post_error = post_error_handler()
        if post_error == "success":
            solvingUI()
        else:

            for i in range(6):
                for j in range(3):
                    for k in range(3):
                        Cube[i][j][k] = Scrambled_Cube[i][j][k]
            messagebox.showerror(title="Error", message= post_error)
    else:

        messagebox.showerror(title="Error",message = pre_error)


def start():
    mainwin = Tk()

    screen_height = mainwin.winfo_screenheight()
    screen_width = mainwin.winfo_screenwidth()

    mainwin.geometry(str(screen_width) + "x" + str(screen_height))
    mainwin.config(background="#1c1c1c")
    mainwin.title("Cube solver - 23EEB0B06")

    frame = Frame(mainwin, bg="#1c1c1c")
    frame.place(x=150, y=150)

    # creating buttons
    whitebuttons = [[Button(frame, padx=20, pady=15) for _ in range(3)] for _ in range(3)]
    bluebuttons = [[Button(frame, padx=20, pady=15) for _ in range(3)] for _ in range(3)]
    orangebuttons = [[Button(frame, padx=20, pady=15) for _ in range(3)] for _ in range(3)]
    greenbuttons = [[Button(frame, padx=20, pady=15) for _ in range(3)] for _ in range(3)]
    redbuttons = [[Button(frame, padx=20, pady=15) for _ in range(3)] for _ in range(3)]
    yellowbuttons = [[Button(frame, padx=20, pady=15) for _ in range(3)] for _ in range(3)]

    allbuttons = [whitebuttons, bluebuttons, orangebuttons, greenbuttons, redbuttons, yellowbuttons]

    start_button = Button(mainwin, bg="gray", text=" Start ",font=("helvetica", 12), command=lambda: checkerror(allbuttons))
    start_button.place(x="650", y="700")

    scan_button = Button(mainwin, bg="grey",text=" Scan ",font=("helvetica", 12),command=lambda: scan(allbuttons))
    scan_button.place(x="750", y="700")

    reset_button = Button(mainwin, bg="gray", text="Reset",font=("helvetica", 12), command=lambda: reset(allbuttons))
    reset_button.place(x="850", y="700")


    # button changer color wise

    for i in range(3):
        for j in range(3):
            whitebuttons[i][j].grid(row=i, column=j + 3)
    for i in range(3):
        for j in range(3):
            orangebuttons[i][j].grid(row=i + 3, column=j)
    for i in range(3):
        for j in range(3):
            greenbuttons[i][j].grid(row=i + 3, column=j + 3)
    for i in range(3):
        for j in range(3):
            redbuttons[i][j].grid(row=i + 3, column=j + 6)
    for i in range(3):
        for j in range(3):
            bluebuttons[i][j].grid(row=i + 3, column=j + 9)
    for i in range(3):
        for j in range(3):
            yellowbuttons[i][j].grid(row=i + 6, column=j + 3)

    # change all buttons here
    for i in range(6):
        for j in range(3):
            for k in range(3):
                allbuttons[i][j][k].config(bg="grey",
                                           command=lambda colour=i, row=j, col=k:
                                           color_chooser(allbuttons, colour, row, col))
    allbuttons[0][1][1].config(bg='white', state='disabled')
    allbuttons[1][1][1].config(bg='blue', state='disabled')
    allbuttons[2][1][1].config(bg='orange', state='disabled')
    allbuttons[3][1][1].config(bg='green', state='disabled')
    allbuttons[4][1][1].config(bg='red', state='disabled')
    allbuttons[5][1][1].config(bg='yellow', state='disabled')

    image = PhotoImage(file='pictures/pic1.png')
    instructions_label = Label(mainwin,image=image)
    instructions_label.place(x=850,y=200)

    mainwin.mainloop()



start()
