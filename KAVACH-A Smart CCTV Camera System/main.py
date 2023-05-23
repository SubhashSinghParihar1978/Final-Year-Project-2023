# Tkinter module
import tkinter as tk
# from tkinter import filedialog
# Fonts available inside tkinter modules
import tkinter.font as font
# Importing Another files from this folder
from in_out import in_out
from motion import noise
# from rect_noise import rect_noise
from Fire_detection import find_fire
from record import record
from find_motion import find_motion
from identify import maincall
# PIL - Python Imaging library - adds features of image processing in python interpreter
from PIL import Image, ImageTk

# Displays the root window and manages all other components of tkinter application
window = tk.Tk()
window.configure(background="#cf9fff")
# Displays title at the left corner of the output window
window.title("Smart cctv")
# Applies a icon on the window , next to title
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
# Gives the window size
window.geometry('1920x1080')

# It is used to make main frame as container such that all other widgets inside the frame will be padded and centered automatcally
frame1 = tk.Frame(window)
frame1.configure(background="#cf9fff")
# Used to give title and some fonts to it
label_title = tk.Label(frame1, text="KAVACH")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
# Finally assigns the title in frame
# .grid() - is used to arrange all widgets in a tabular manner
label_title.grid(pady=(10,10), column=2)

# opens image
icon = Image.open('icons/spy.png')
# resize the img and antialias will remove the distortions and smoothens the img
icon = icon.resize((150,150), Image.ANTIALIAS)
# Displays img
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/fire.jpg')
btn2_image = btn2_image.resize((80,80), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn4_image = Image.open('icons/rec.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50,50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn7_image = Image.open('icons/recording.png')
btn7_image = btn7_image.resize((50,50), Image.ANTIALIAS)
btn7_image = ImageTk.PhotoImage(btn7_image)

# --------------- Button -------------------#
btn_font = font.Font(size=25)

# v = StringVar()

# Makes the widget as buttons which on click goes to the respected command call
btn1 = tk.Button(frame1, text='Theft Detector', height=90, width=400, fg='black',command = find_motion, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10))

btn2 = tk.Button(frame1, text='Fire', height=90, width=280, fg='black',command = find_fire, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))

btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, text='Noise', height=90, width=280, fg='black', command=noise, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=5, pady=(20,10))

btn4 = tk.Button(frame1, text='Record', height=90, width=350, fg='black', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=3)

btn5 = tk.Button(frame1, height=90, width=180, fg='black', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20,10), column=2)

# btn8 = tk.Button(frame1, text='Rectangle', height=90, width=350, fg='black', command=rect_noise, image=btn4_image, compound='left')
# btn8['font'] = btn_font
# btn8.grid(row=6, pady=(20,10), column=2,padx=(40,10))

btn6 = tk.Button(frame1, text='In Out', height=90, width=280, fg='black', command=in_out, image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=5, pady=(20,10), column=2)

btn7 = tk.Button(frame1, text="Identify", fg="black",command=maincall, compound='left', image=btn7_image, height=90, width=320)
btn7['font'] = btn_font
btn7.grid(row=3, column=2, pady=(20,10),padx=(40,10))

# Basically used to make our tkinter GUI responsive with features such as expand,fill etc.
frame1.pack()
# Without it , the frame will be closed within a second , basically used to hold the screen
window.mainloop()