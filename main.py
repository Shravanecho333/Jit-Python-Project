from datetime import datetime
from tkinter import *
from PIL import ImageTk,Image  
now = datetime.now()



def wishMe():
    root = Tk()
    canvas = Canvas(root, width = 680, height = 420) 
    canvas.pack() 
    hour = int(datetime.now().hour)

    if hour>=0 and hour<12:
        print("Good Morning!")
        img = ImageTk.PhotoImage(Image.open("Morning.jpg"))

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        img = ImageTk.PhotoImage(Image.open("Afternoon1.jpg"))

    elif hour>=18 and hour<20:
        print("Good Evening!")
        img = ImageTk.PhotoImage(Image.open("Evening.jpg"))

    else:
        print("Good Night!")
        img = ImageTk.PhotoImage(Image.open("Night.jpg"))

    canvas.create_image(20, 20, anchor=NW, image=img) 
    root.mainloop()
    


current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

wishMe()
print()



