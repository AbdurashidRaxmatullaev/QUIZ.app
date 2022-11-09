from tkinter import *
def MATH():
    pass
def first_quiz():  
        first = Tk()
        first.geometry('600x400')
        first.title('Quiz app')
        first.resizable(width=False, height=False)
        def next1_func():
            global first_value
            first_value = var.get()
            first.destroy()
            second_quiz()



        def next1_func():
            global score
            score['1'] = var.get
            print (score)
            first.destroy()
            second_quiz()






        label_top = Label(first, bg='green', width=90, height=2, fg='white',
            text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        label_top.pack()
        var = StringVar()
        var.set(0)
        quiz1 = Label(first, text='2+2= nechchi?',
        font=('Arial', 15, 'bold'))
        quiz1.place(x=70, y=100)
        radio1 = Radiobutton(first, text='4', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radio1.place(x=70, y=140)
        radio2 = Radiobutton(first, text='5', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radio2.place(x=70, y=180)
        radio3 = Radiobutton(first, text='bilmiman', value="False", variable=var, font=('Arial', 15, 'normal'))
        radio3.place(x=70, y=220)
        radio4 = Radiobutton(first, text='1', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radio4.place(x=70, y=260)
        next = Button(first, text='Next', bg='blue', fg='white', width=13, height=2, command=next1_func)
        next.place(x=260, y=330)
        first.mainloop()

def second_quiz():
    def next2_func():
        global score
        score['2'] = var.get
        print (score)
        second_quiz.destroy()
        second_quiz()
        second = Tk()
        second.geometry('600x400')
        second.title('Quiz app')
        second.resizable(width=False, height=False)
        def next2_func():
            global second_value
            second_value = var.get()
            second.destroy()
            third_quiz()
        labell_top = Label(second, bg='green', width=90, height=2, fg='white',
            text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(second, text='4*4= nechchi?',
        font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(second, text='bilmiman', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(second, text='16', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(second, text='13', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(second, text='14', value="Tog'ri", variable=var, font=(
    'Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(second, text='Next', bg='blue', fg='white', width=13, height=2, command=next2_func)
        nextt.place(x=260, y=330)
        second.mainloop()
def third_quiz():
    def next3_func():
        global score
        score['3'] = var.get
        print (score)
        third_quiz.destroy()
        third_quiz()
        third = Tk()
        third.geometry('600x400')
        third.title('Quiz app')
        third.resizable(width=False, height=False)
        def next3_func():
            global third_value
            third_value = var.get()
            third.destroy()
            fourth_quiz()
        
        labell_top = Label(third, bg='green', width=90, height=2, fg='white',
            text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(third, text='p= formulasi',
        font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(third, text='(a+b)*2', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(third, text='4*4 , else , elif', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(third, text='2+2*2', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(third, text='bilmiman , elif, else', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(third, text='Next', bg='blue', fg='white', width=13, height=2, command=next3_func)
        nextt.place(x=260, y=330)
        third.mainloop()

def fourth_quiz():
    def next4_func():
        global score
        score['4'] = var.get
        print (score)
        fourth_quiz.destroy()
        fourth_quiz()
        fourth = Tk()
        fourth.geometry('600x400')
        fourth.title('Quiz app')
        fourth.resizable(width=False, height=False)
        def next4_func():
            global fourth_value
            fourth_value = var.get()
            fourth.destroy()
            fiveth_quiz()
        labell_top = Label(fourth, bg='green', width=90, height=2, fg='white',
            text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(fourth, text='10000+1=nechchi',
        font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(fourth, text='10001', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(fourth, text='10011', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(fourth, text='10010', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(fourth, text='bilmadim', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(fourth, text='Next', bg='blue', fg='white', width=13, height=2, command=next4_func)
        nextt.place(x=260, y=330)
        fourth.mainloop()
def fiveth_quiz():
    def next5_func():
        global score
        score['5'] = var.get
        print (score)
        fiveth_quiz.destroy()
        fiveth_quiz()
        fiveth = Tk()
        fiveth.geometry('600x400')
        fiveth.title('Quiz app')
        fiveth.resizable(width=False, height=False)
        def next5_func():
            global fiveth_value
            fiveth_value = var.get()
            fiveth.destroy()
            sixth_quiz()
        labell_top = Label(fiveth, bg='green', width=90, height=2, fg='white',
            text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(fiveth, text='0 sosnini oylab topgan',
        font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(fiveth, text='Alisher navoyi', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(fiveth, text='bobur', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(fiveth, text='beruniy', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(fiveth, text='bilmiman', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(fiveth, text='Next', bg='blue', fg='white', width=13, height=2, command=next5_func)
        nextt.place(x=260, y=330)
        fiveth.mainloop()
def sixth_quiz():
    def next6_func():
        global score
        score['6'] = var.get
        print (score)
        sixth_quiz.destroy()
        sixth_quiz()
        sixth = Tk()
        sixth.geometry('600x400')
        sixth.title('Quiz app')
        sixth.resizable(width=False, height=False)
        def next6_func():
            global sixth_value
            sixth_value = var.get()
            sixth.destroy()
            seventh_quiz()
        labell_top = Label(sixth, bg='green', width=90, height=2, fg='white',
            text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(sixth, text='manfiy nma bilan brlgilanadi',
        font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(sixth, text='+', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(sixth, text='-', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(sixth, text='bilmiman', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(sixth, text='hammasi togri',

        value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(sixth, text='Next', bg='blue', fg='white', width=13, height=2, command=next6_func)
        nextt.place(x=260, y=330)
        sixth.mainloop()

def seventh_quiz():
        def next7_func():
            global score
        score['7'] = var.get
        print (score)
        seventh_quiz.destroy()
        seventh_quiz()
        seventh = Tk()
        seventh.geometry('600x400')
        seventh.title('Quiz app')
        seventh.resizable(width=False, height=False)
        def next7_func():
            global seventh_value
            seventh_value = var.get()
            seventh.destroy()
            eightth_quiz()
        labell_top = Label(seventh, bg='green', width=90, height=2, fg='white',
            text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(seventh, text='kasr nima si bor',
        font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(seventh, text='-bor', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(seventh, text='ildiz', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(seventh, text='minus bor', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(seventh, text='endi bilib olaman', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(seventh, text='Next', bg='blue', fg='white', width=13, height=2, command=next7_func)
        nextt.place(x=260, y=330)
        seventh.mainloop() 
def eightth_quiz():
    def next8_func():
        global score
        score['8'] = var.get
        print (score)
        eightth_quiz.destroy()
        eightth_quiz()
        eightth = Tk()
        eightth.geometry('600x400')
        eightth.title('Quiz app')
        eightth.resizable(width=False, height=False)
        def next8_func():
            global eightth_value
            eightth_value = var.get()
            eightth.destroy()
            nineth_quiz()
        labell_top = Label(eightth, bg='green', width=90, height=2, fg='white',
            text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(eightth, text='990+90907nechchi',
        font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(eightth, text='191090', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(eightth, text='3129389', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(eightth, text='676575', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(eightth, text='bilmiman', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(eightth, text='Next', bg='blue', fg='white', width=13, height=2, command=next8_func)
        nextt.place(x=260, y=330)
        eightth.mainloop()

def nineth_quiz():
    def next9_func():
        global score
        score['9'] = var.get
        print (score)
        nineth_quiz.destroy()
        nineth_quiz()
        nineth = Tk()
        nineth.geometry('600x400')
        nineth.title('Quiz app')
        nineth.resizable(width=False, height=False)
        def next9_func():
            global nineth_value
            nineth_value = var.get()
            nineth.destroy()
            tenth_quiz()
        labell_top = Label(nineth, bg='green', width=90, height=2, fg='white',
            text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(nineth, text='Matematika 6 sinfdan keyin nma deb ataladi',
        font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(nineth, text='Algebra', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(nineth, text='Fizika', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(nineth, text='Kimyo', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(nineth, text='Zoologiya', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(nineth, text='Next', bg='blue', fg='white', width=13, height=2, command=next9_func)
        nextt.place(x=260, y=330)
        nineth.mainloop()
def tenth_quiz():
    def next10_func():
        global score
        score['10'] = var.get
        print (score)
        tenth_quiz.destroy()
        tenth_quiz()
        tenth = Tk()
        tenth.geometry('600x400')
        tenth.title('Quiz app')
        tenth.resizable(width=False, height=False)
        def next10_func():
            global tenth_value
            tenth_value = var.get()
            tenth.destroy()
            
        labell_top = Label(tenth, bg='green', width=90, height=2, fg='white',
            text='Quiz app by G11 group', font=('Arial', 15, 'normal'))
        labell_top.pack()
        var = StringVar()
        var.set(0)
        quizz1 = Label(tenth, text='8kvadrati nechchi',
        font=('Arial', 15, 'bold'))
        quizz1.place(x=70, y=100)
        radioo1 = Radiobutton(tenth, text='64', value="Tog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo1.place(x=70, y=140)
        radioo2 = Radiobutton(tenth, text='128', value="Notog'ri", variable=var, font=('Arial', 15, 'normal'))
        radioo2.place(x=70, y=180)
        radioo3 = Radiobutton(tenth, text='16', value="False", variable=var, font=('Arial', 15, 'normal'))
        radioo3.place(x=70, y=220)
        radioo4 = Radiobutton(tenth, text='869', value="Error", variable=var, font=('Arial', 15, 'normal'))
        radioo4.place(x=70, y=260)
        nextt = Button(tenth, text='Next', bg='blue', fg='white', width=13, height=2, command=next10_func)
        nextt.place(x=260, y=330)
        tenth.mainloop()


first_quiz()
