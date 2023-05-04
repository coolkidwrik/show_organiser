from tkinter import *

root = Tk()
images = list()  # list of the images used for this frame

# sets up all necessary details associated with the current frame
def set_frame():
    root.geometry("700x500")
    root.title("My Show List")
    root.config(background="#e7abf5")
    set_images()


# sets all images, including the icon, associated with the current frame
def set_images():
    icon = PhotoImage(file="../images/taiga_logo.png")
    # "../images/taiga_donut.png"
    # create_image_label("../images/taiga_donut.png")
    root.iconphoto(True, icon)

# helper function to help create image labels
def create_image_label(s: str):
    img = PhotoImage(file=s)
    label = Label(root, image=img, text="hello world", compound="bottom")
    label.pack()


set_frame()
root.mainloop()
