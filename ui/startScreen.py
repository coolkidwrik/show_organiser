from tkinter import *

root = Tk()


# sets up all necessary details associated with the current frame
def set_frame():
    set_images()
    root.title("My Show List")
    root.config(background="#e7abf5")


# sets all images, including the icon, associated with the current frame
def set_images():
    icon = PhotoImage(file="../images/taiga_logo.png")
    root.iconphoto(True, icon)


set_frame()
root.mainloop()
