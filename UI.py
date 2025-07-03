import numpy as np
import cv2
from variables import *
from tkinter import *
from tkinter import messagebox
from Functions import *
from tkinter import ttk

def update_progress_bar():
    progress['value'] = (index / len(result)) * 100
def wchosen(allbuttons,colour,row,col,color_window=None):
    allbuttons[colour][row][col].config(bg="white")
    Cube[colour][row][col] = 0
    if color_window != None:
        color_window.destroy()
def bchosen(allbuttons,colour,row,col,color_window=None):
    allbuttons[colour][row][col].config(bg="blue")
    Cube[colour][row][col] = 1
    if color_window != None:
        color_window.destroy()
def ochosen(allbuttons,colour,row,col,color_window=None):
    allbuttons[colour][row][col].config(bg="orange")
    Cube[colour][row][col] = 2
    if color_window != None:
        color_window.destroy()
def gchosen(allbuttons,colour,row,col,color_window=None):
    allbuttons[colour][row][col].config(bg="green")
    Cube[colour][row][col] = 3
    if color_window != None:
        color_window.destroy()
def rchosen(allbuttons,colour,row,col,color_window=None):
    allbuttons[colour][row][col].config(bg="red")
    Cube[colour][row][col] = 4
    if color_window != None:
        color_window.destroy()
def ychosen(allbuttons,colour,row,col,color_window=None):
    allbuttons[colour][row][col].config(bg="yellow")
    Cube[colour][row][col] = 5
    if color_window != None:
        color_window.destroy()

chosen_array = [wchosen,bchosen,ochosen,gchosen,rchosen,ychosen]
def apply_scan(side_colors_int,allbuttons):

    for l in range(6):
        if side_colors_int[1][1] == l:
            for i in range(3):
                for j in range(3):
                    if i == j == 1:
                        continue
                    for k in range(6):
                        if side_colors_int[i][j]==k:
                            chosen_array[k](allbuttons, l, i, j)

def scan(allbuttons):
    def detect_color(square):

        hsv_square = cv2.cvtColor(square, cv2.COLOR_BGR2HSV)


        color_ranges = {
            'red1': [(0, 180, 67), (1, 255, 255)],
            'red2': [(173, 180, 67), (180, 255, 255)],
            'green': [(43, 140, 67), (73, 255, 255)],
            'blue': [(100, 140, 45), (130, 255, 255)],
            'yellow': [(20, 101, 67), (40, 255, 255)],
            'orange': [(1, 100, 67), (20, 255, 255)],
            'white': [(0, 0, 146), (180, 70, 255)]
        }

        for color, (lower, upper) in color_ranges.items():
            lower_bound = np.array(lower)
            upper_bound = np.array(upper)

            mask = cv2.inRange(hsv_square, lower_bound, upper_bound)


            if color.startswith('red'):

                lower_bound2 = np.array(color_ranges['red2'][0])
                upper_bound2 = np.array(color_ranges['red2'][1])
                mask2 = cv2.inRange(hsv_square, lower_bound2, upper_bound2)
                mask = cv2.bitwise_or(mask, mask2)


            color_percentage = (np.count_nonzero(mask) / mask.size) * 100


            if color_percentage > 50:
                return 'red' if color.startswith('red') else color

        return 'unknown'

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    crop_size = 600

    while True:
        ret, frame = cap.read()
        flipped_frame = cv2.flip(frame, 1)
        if not ret:
            break

        height, width, _ = flipped_frame.shape
        if width >= crop_size and height >= crop_size:
            center_x, center_y = width // 2, height // 2
            x_start = center_x - crop_size // 2
            y_start = center_y - crop_size // 2
            cropped_frame = flipped_frame[y_start:y_start + crop_size, x_start:x_start + crop_size]
        else:
            cropped_frame = flipped_frame

        img = cropped_frame.copy()

        img = cv2.line(img, (200, 0), (200, 600), (0, 0, 0), 3)
        img = cv2.line(img, (400, 0), (400, 600), (0, 0, 0), 3)
        img = cv2.line(img, (0, 200), (600, 200), (0, 0, 0), 3)
        img = cv2.line(img, (0, 400), (600, 400), (0, 0, 0), 3)

        detected_colors = [['unknown'] * 3 for _ in range(3)]
        cv2.putText(img, 'Press Q to exit', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        for row in range(3):
            for col in range(3):
                square = cropped_frame[row * 200:(row + 1) * 200, col * 200:(col + 1) * 200]
                color = detect_color(square)

                text_x = col * 200 + 100
                text_y = row * 200 + 100


                cv2.putText(img, color, (text_x - 50, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                detected_colors[row][col] = color

        if all(color != 'unknown' for row in detected_colors for color in row):
            side_colors = [row[::-1] for row in detected_colors]
            color_map = {
                "white": 0,
                "blue": 1,
                "orange": 2,
                "green": 3,
                "red": 4,
                "yellow": 5
            }
            side_colors_int = [[color_map[color] for color in row] for row in side_colors]
            apply_scan(side_colors_int,allbuttons)
            cv2.destroyAllWindows()
            break



        cv2.imshow('Cropped Camera', img)

        if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == ord('Q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def color_chooser(allbuttons,colour, row, col):
    color_window = Toplevel()
    color_window.config(bg= "black")

    color_frame = Frame(color_window, bg="gray")
    color_frame.pack()

    chose_white = Button(color_frame, padx=20, pady=15, bg="white",command= lambda : wchosen(allbuttons,colour, row,col, color_window)).grid(row=0,column=0, padx=15, pady=15)
    chose_blue = Button(color_frame, padx=20, pady=15,bg="blue",command= lambda: bchosen(allbuttons,colour, row, col, color_window)).grid(row=0,column=1, padx=15, pady=15)
    chose_orange = Button(color_frame, padx=20, pady=15,bg="orange",command= lambda:  ochosen(allbuttons,colour, row, col, color_window)).grid(row=0,column=2, padx=15, pady=15)
    chose_green = Button(color_frame, padx=20, pady=15, bg="green",command= lambda: gchosen(allbuttons,colour, row, col, color_window)).grid(row=1,column=0, padx=15, pady=15)
    chose_red = Button(color_frame, padx=20, pady=15, bg="red",command= lambda: rchosen(allbuttons,colour, row, col, color_window)).grid(row=1,column=1, padx=15, pady=15)
    chose_yellow = Button(color_frame, padx=20, pady=15, bg="yellow",command= lambda: ychosen(allbuttons,colour, row,col, color_window)).grid(row=1,column=2, padx=15, pady=15)

def reset(allbuttons):
    for k in range(6):
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    continue
                allbuttons[k][i][j].config(bg="gray")
                Cube[k][i][j] = -1


def next(window2,  moves, event=None):


    global index
    index += 1
    update_progress_bar()

    for widget in window2.winfo_children():
        if isinstance(widget, Label):
            widget.destroy()
    moves_label = Label(window2, text=str(index+1) + "/" + str(moves))
    moves_label.place(x=1000, y=320)

    if len(result) > index >= 0:

        update_progress_bar()

        if result[index] == 'U':
            photo = PhotoImage(file='pictures/U.png')
            text = ''
        elif result[index] == 'U2':
            photo = PhotoImage(file='pictures/U.png')
            text = 'x2'
        elif result[index] == 'U3':
            photo = PhotoImage(file='pictures/UI.png')
            text = ''
        elif result[index] == 'R':
            photo = PhotoImage(file='pictures/R.png')
            text = ''
        elif result[index] == 'R2':
            photo = PhotoImage(file='pictures/R.png')
            text = 'x2'
        elif result[index] == 'R3':
            photo = PhotoImage(file='pictures/RI.png')
            text = ''
        elif result[index] == 'L':
            photo = PhotoImage(file='pictures/L.png')
            text = ''
        elif result[index] == 'L2':
            photo = PhotoImage(file='pictures/L.png')
            text = 'x2'
        elif result[index] == 'L3':
            photo = PhotoImage(file='pictures/LI.png')
            text = ''
        elif result[index] == 'D':
            photo = PhotoImage(file='pictures/D.png')
            text = ''
        elif result[index] == 'D2':
            photo = PhotoImage(file='pictures/D.png')
            text = 'x2'
        elif result[index] == 'D3':
            photo = PhotoImage(file='pictures/DI.png')
            text = ''
        elif result[index] == 'F':
            photo = PhotoImage(file='pictures/F.png')
            text = ''
        elif result[index] == 'F2':
            photo = PhotoImage(file='pictures/F.png')
            text = 'x2'
        elif result[index] == 'F3':
            photo = PhotoImage(file='pictures/FI.png')
            text = ''
        elif result[index] == 'B':
            photo = PhotoImage(file='pictures/B.png')
            text = ''
        elif result[index] == 'B2':
            photo = PhotoImage(file='pictures/B.png')
            text = 'x2'
        elif result[index] == 'B3':
            photo = PhotoImage(file='pictures/BI.png')
            text = ''
        else:
            photo = None
            text = "Some error occurred. Please try again"

        # Create and place labels
        image_label = Label(window2, image=photo)
        image_label.image = photo
        image_label.place(x=100, y=100)

        if text != '':
            text_label = Label(window2, text=text, font=("calibri", 80))
            text_label.place(x=100, y=600)

    elif index == len(result):

        image = PhotoImage(file='pictures/done_message.png')
        done_label = Label(window2, image=image)
        done_label.place(x=100, y=100)
        done_label.image = image

    elif index > len(result):
        window2.destroy()
def prev(window2,moves,event=None):
    global index



    if 0 < index < len(result):
        index -= 1
        update_progress_bar()

        for widget in window2.winfo_children():
            if isinstance(widget, Label):
                widget.destroy()
        moves_label = Label(window2, text=str(index+1) + "/" + str(moves))
        moves_label.place(x=1000, y=320)
        if result[index] == 'U':
            photo = PhotoImage(file='pictures/U.png')
            text = ''
        elif result[index] == 'U2':
            photo = PhotoImage(file='pictures/U.png')
            text = 'x2'
        elif result[index] == 'U3':
            photo = PhotoImage(file='pictures/UI.png')
            text = ''
        elif result[index] == 'R':
            photo = PhotoImage(file='pictures/R.png')
            text = ''
        elif result[index] == 'R2':
            photo = PhotoImage(file='pictures/R.png')
            text = 'x2'
        elif result[index] == 'R3':
            photo = PhotoImage(file='pictures/RI.png')
            text = ''
        elif result[index] == 'L':
            photo = PhotoImage(file='pictures/L.png')
            text = ''
        elif result[index] == 'L2':
            photo = PhotoImage(file='pictures/L.png')
            text = 'x2'
        elif result[index] == 'L3':
            photo = PhotoImage(file='pictures/LI.png')
            text = ''
        elif result[index] == 'D':
            photo = PhotoImage(file='pictures/D.png')
            text = ''
        elif result[index] == 'D2':
            photo = PhotoImage(file='pictures/D.png')
            text = 'x2'
        elif result[index] == 'D3':
            photo = PhotoImage(file='pictures/DI.png')
            text = ''
        elif result[index] == 'F':
            photo = PhotoImage(file='pictures/F.png')
            text = ''
        elif result[index] == 'F2':
            photo = PhotoImage(file='pictures/F.png')
            text = 'x2'
        elif result[index] == 'F3':
            photo = PhotoImage(file='pictures/FI.png')
            text = ''
        elif result[index] == 'B':
            photo = PhotoImage(file='pictures/B.png')
            text = ''
        elif result[index] == 'B2':
            photo = PhotoImage(file='pictures/B.png')
            text = 'x2'
        elif result[index] == 'B3':
            photo = PhotoImage(file='pictures/BI.png')
            text = ''
        else:
            photo = None
            text = "Some error occurred. Please try again"

        # Create and place labels
        image_label = Label(window2, image=photo)
        image_label.image = photo
        image_label.place(x=100, y=100)

        if text != '':
            text_label = Label(window2, text=text, font=("calibri", 80))
            text_label.place(x=100, y=600)


def solvingUI():
    print(result)
    global index
    global progress
    index = -1
    moves = len(result)
    window2 = Toplevel()

    window2.bind('<Right>', lambda event: next(window2, moves))
    window2.bind('<Left>', lambda event: prev(window2, moves))

    screen_height = window2.winfo_screenheight()
    screen_width = window2.winfo_screenwidth()
    window2.geometry(str(screen_width)+"x"+str(screen_height))
    window2.config(bg="#1c1c1c")

    progress = ttk.Progressbar(window2, orient='horizontal', length=300, mode='determinate')
    progress.place(x=1000, y=350)


    prev_button = Button(window2, text='Prev', command=lambda: prev(window2,moves))
    prev_button.place(x=750, y=700)


    next_button = Button(window2, text='Next', command=lambda: next(window2,moves))
    next_button.place(x=850, y=700)

    image = PhotoImage(file='pictures/pic2.png')
    instruction_label = Label(window2,image=image)

    instruction_label.place(x=150,y=150)
    instruction_label.image = image

    moves_label = Label(window2, text=str(index+1)+"/"+str(moves), font=("Helvetica", 14))
    moves_label.place(x=1000, y=320)
