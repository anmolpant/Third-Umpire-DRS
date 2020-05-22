import tkinter
import cv2
import PIL.Image, PIL.ImageTk

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
window.mainloop()