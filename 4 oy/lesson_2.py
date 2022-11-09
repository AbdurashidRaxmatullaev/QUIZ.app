from tkinter import *
from PIL import Image, ImageTk
import json
root = Tk()
root.geometry('600x400')
frame = Frame()


frame1 = Frame(root, width =300, height=500, bg='red')
frame1.place(x=0,y=0)    

frame2 = Frame(root, width =300, height=500, bg='yellow')
frame2.place(x=300,y=0)   

rasm = Image.open('ok.jpg').resize((200,200))
image =ImageTk.PhotoImage(rasm)
label =Label(frame1, image=image)
label.place(x=40, y=90)


with open('quiz_app.json','r') as a:
    w = json.load(a)


# for k,v in w.items():
#     label = Label(frame2, text=k, bg='green', fg='white')    
#     label.place(x=25, y=r)
#     r+=30























root.mainloop()