from tkinter import *
from tkmacosx import Button


# creates a widget that acts as the starting screen for the GUI
class StartScreen:

    # initializes the screen
    def __init__(self):
        root = Tk()
        img1 = PhotoImage(file="../images/taiga_donut.png")
        img2 = PhotoImage(file="../images/sakura_background.png")
        set_frame(root, img1, img2)
        root.mainloop()


# sets up all necessary details associated with the current frame
def set_frame(root: Tk, img1: PhotoImage, img2: PhotoImage):
    set_frame_info(root)
    set_bg(root, img1, img2)
    set_buttons(root)


# sets all base info of the frame
def set_frame_info(root: Tk):
    root.geometry("700x500")
    root.title("My Show List")
    set_icon(root)
    root.resizable(False, False)


# sets the icon of the frame
def set_icon(root: Tk):
    icon = PhotoImage(file="../images/taiga_logo.png")
    root.iconphoto(True, icon)


# sets the necessary background of the frame
def set_bg(root: Tk, img1: PhotoImage, img2: PhotoImage):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    canvas = Canvas(root,
                    width=width,
                    height=height)
    canvas.create_image(0, 0, image=img2, anchor=NW)
    canvas.create_image(510, 355, image=img1)
    canvas.create_text(330, 150, text="My Show List", font=("Comic Sans", 60, "bold italic"), fill="#fa39b3")
    canvas.place(x=0, y=0)


# sets all the buttons on the frame
def set_buttons(root: Tk):
    button1 = create_button(root, text="Browse Lists", command=root.destroy)
    button2 = create_button(root, text="Create New Lists", command=root.destroy)
    button3 = create_button(root, text="Quit", command=root.destroy)
    button1.place(x=80, y=250)
    button2.place(x=80, y=300)
    button3.place(x=80, y=350)


def create_button(root: Tk, **kwargs):
    # for handling errors
    valid_indexes = {'text', 'command'}
    items = kwargs.items()
    assert items.__sizeof__() <= valid_indexes.__sizeof__(), "too many arguments"
    for key, value in items:
        assert key in valid_indexes, "not a valid index"

    # working function
    bg = "#e7abf5"  # background color of the button
    button = Button(root,
                    text=kwargs['text'],
                    bg=bg,
                    width=270,
                    height=40,
                    highlightbackground=bg,
                    fg="#fa39b3",
                    font=("Comic Sans", 30, "italic"),
                    command=kwargs['command'])
    return button
#
#
# set_frame()
# root.mainloop()


# testing
screen = StartScreen()

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
