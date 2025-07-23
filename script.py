from playsound import playsound
from tkinter import *

window = Tk()
window.geometry("800x600") ## change the resolution according to your image (if you even want a image)
window.title("placeholder") ## title

def play():
    playsound('file.mp3') ## any audio file can go here

button = Button(window, text='button', command=play) ## what name will be displayed on the button
button.pack()

icon = PhotoImage(file='icon.png') ## icon at the top
image = PhotoImage(file='image.png') ## image that should be displayed in the code

image_label = Label(window, image=image)
image_label.pack()

window.iconphoto(True,icon)

window.mainloop()

## also hello
