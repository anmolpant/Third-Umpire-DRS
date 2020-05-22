import tkinter
import cv2
from functools import partial
import PIL.Image, PIL.ImageTk

def play(speed):
    print(f"inshallah bois. speed is {speed} ")

#height and width of main screen
SET_WIDTH = 650
SET_HEIGHT = 350

#gui starts
window = tkinter.Tk()
window.title("Third Umpire DRS")
cv_img = cv2.cvtColor(cv2.imread("lords.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height = SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, anchor = tkinter.NW, image=photo )
canvas.pack()


#adding buttons
btn = tkinter.Button(window, text = "<< Previous (fast)", width = 50, command = partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text = "<< Previous (slow)", width = 50, command = partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text = " Next (slow) >>", width = 50, command = partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text = " Next (fast) >>", width = 50, command = partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text = " Give Out", width = 50)
btn.pack()

btn = tkinter.Button(window, text = " Give Not Out", width = 50)
btn.pack()
window.mainloop()