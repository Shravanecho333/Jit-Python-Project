from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 680, height = 420)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("Afternoon1.jpg"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
root.mainloop()