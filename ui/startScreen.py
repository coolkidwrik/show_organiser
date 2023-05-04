from tkinter import *

root = Tk()
bg = "#e7abf5"  # background color of the screen
img1 = PhotoImage(file="../images/taiga_donut.png")
img2 = PhotoImage(file="../images/sakura_background.png")


# sets up all necessary details associated with the current frame
def set_frame():
    set_frame_info()
    set_bg()
    set_buttons()


# sets all base info of the frame
def set_frame_info():
    root.geometry("700x500")
    root.title("My Show List")
    set_icon()
    root.resizable(False, False)


# sets the icon of the frame
def set_icon():
    icon = PhotoImage(file="../images/taiga_logo.png")
    root.iconphoto(True, icon)


# sets the necessary background of the frame
def set_bg():
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    canvas = Canvas(root,
                    width=width,
                    height=height)
    canvas.create_image(0, 0, image=img2, anchor=NW)
    canvas.create_image(510, 355, image=img1)
    canvas.create_text(330, 100, text="My Show List", font=("Calibre", 60, "bold italic"), fill="#fa39b3")
    canvas.place(x=0, y=0)
    canvas.configure(bg=bg)


# sets all the buttons on the frame
def set_buttons():
    pass


set_frame()
root.mainloop()


# the following code is for a label. Since labels don't support transparent backgrounds, it is not used

# img = PhotoImage(file="../images/taiga_donut.png")
# Label(root, image=img, bg=bg).place(x=320, y=220)


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
