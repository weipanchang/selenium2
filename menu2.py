from Tkinter import *


root = Tk()
root.title("Pack is BEST!!!")

l = Label(root, text="Pack is simply the best")
l.pack()


def forget():
     l.pack_forget()

def remember():
     l.pack()


b = Button(root, text="Forget about it", command=forget)
b.pack()
b = Button(root, text="Wait, I still need you", command=remember)
b.pack()


root.mainloop()
 