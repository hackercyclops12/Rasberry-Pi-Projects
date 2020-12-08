from random import *
import tkinter as tk

Answer = choice(["As i see it, yes.","Ask again later.","Better not tell you know.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","It is certain.","It is decidedly so.","Most Likely.","My reply is no.","My sources say no.","Outlook not so good.","Outlook good.","Reply hazy, try again.","Signs point to yes.","Very doubtful.","Without a doubt.","Yes.","Yes... definitely.","You may rely on it."])

root= tk.Tk()
root.title('Magic 8 Ball - Decision Maker')
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Magic 8 Ball - Decision Maker')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='What would you like to ask the magic 8 ball?')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def AnswerQuestion ():
    
    label3 = tk.Label(root, text= 'Answer to you question is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, text= Answer ,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Ask', command=AnswerQuestion, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
