from Tkinter import *
from Tkinter import Text
import Tkinter
    
master=Tkinter.Tk()

def message():
#
    compose_button.destroy()
    send_message_button=Tkinter.Button(master, text="Submit Message")
    send_message_button.pack()
      
    compose_text=Tkinter.Text(master)
    compose_text.pack()
    compose_text.after(5, master.quit())

    #


compose_button=Tkinter.Button(master, text="Compose Message", command = message)
compose_button.pack()
#compose_button.config(command = message)
#compose_button.after(5, master.quit())


master.mainloop()