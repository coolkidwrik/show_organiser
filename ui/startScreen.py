from tkinter import *

root = Tk()
bg = "#e7abf5"  # background color of the screen


# sets up all necessary details associated with the current frame
def set_frame():
    root.geometry("700x500")
    root.title("My Show List")
    root.config(background=bg)
    icon = PhotoImage(file="../images/taiga_logo.png")
    root.iconphoto(True, icon)
    root.resizable(False, False)
    # set_images()


# the following code does not work because python garbage collects the variables before they are
# put onto the screen.

# # sets all images, including the icon, associated with the current frame
# def set_images():
#     icon = PhotoImage(file="../images/taiga_logo.png")
#     # "../images/taiga_donut.png"
#     img1 = create_image_label("../images/taiga_donut.png")
#     img1.pack()
#     root.iconphoto(True, icon)
#
#
# # helper function to help create image labels
# def create_image_label(s: str):
#     img = PhotoImage(file=s)
#     label = Label(root, image=img)
#     return label


set_frame()
img = PhotoImage(file="../images/taiga_donut.png")
Label(root, image=img, bg=bg).place(x=320, y=220)
root.mainloop()
