from tkinter import *
from tkinter import messagebox

root = Tk()

def button_click():
    messagebox.askyesno(title = 'Danger!', message = 'You will spend all your money! Are you sure?')
  

root['bg'] = '#fafafa'
root.title('Alex App')
root.geometry('480x375')

root.resizable(width=False, height=False)

canvas = Canvas(root,heigh=480, width= 405)
canvas.pack()

frame= Frame(root, bg='grey')
frame.place(rely = 0.03, relx = 0.025, relwidth = 0.95, relheight = 0.9)

title = Label (frame, text = 'Give some money for Anka', bg = '#FFE4B5', font = 45 )
title.pack()

button = Button(frame, text = 'Donate all', bg = 'yellow', width= 15, command= button_click) 
button.pack()

loginInput = Entry(frame, bg = '#fafafa')
loginInput.pack()



root.mainloop()


    





