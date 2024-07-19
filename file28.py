from tkinter import *
from PIL import Image, ImageTk  
root = Tk()
root.title('open file')

image = Image.open("logo.jpg")
image = ImageTk.PhotoImage(image)

imageLable = Label(root, image=image)
imageLable.pack()

root.mainloop()

