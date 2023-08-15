from tkinter import *

def click_fun(event):
    global scrvari
    text = event.widget.cget('text')
    pass
    if text == '=':
        pass
    elif text == 'C':
        pass
    else:
        scrvari.set(scrvari.get() + text)
        screen.update()


root = Tk()

scrvari = StringVar()
scrvari.set("")

screen = Entry(root, textvar=scrvari, font= "lucida 20 bold")
screen.pack(fill=X, padx=10, pady=10)

the_frame = Frame(root, bg='gray')
the_frame.pack(padx=5, pady=5)

button = Button(the_frame, padx=13, pady=11, text='9', font='lucida 25 bold')
button.pack(side='left', padx=4, pady=4)
button.bind('<Button-1>', click_fun)

button = Button(the_frame, padx=13, pady=11, text='8', font='lucida 25 bold')
button.pack(side='left', padx=4, pady=4)
button.bind('<Button-1>', click_fun)

button = Button(the_frame, padx=13, pady=11, text='7', font='lucida 25 bold')
button.pack(side='left', padx=4, pady=4)
button.bind('<Button-1>', click_fun)

the_frame = Frame(root, bg='gray')
the_frame.pack(padx=5, pady=5)
button.bind('<Button-1>', click_fun)

button = Button(the_frame, padx=13, pady=11, text='6', font='lucida 25 bold')
button.pack(side='left', padx=4, pady=4)
button.bind('<Button-1>', click_fun)

button = Button(the_frame, padx=13, pady=11, text='5', font='lucida 25 bold')
button.pack(side='left', padx=4, pady=4)
button.bind('<Button-1>', click_fun)

button = Button(the_frame, padx=13, pady=11, text='4', font='lucida 25 bold')
button.pack(side='left', padx=4, pady=4)
button.bind('<Button-1>', click_fun)

the_frame = Frame(root, bg='gray')
the_frame.pack(padx=5, pady=5)

button = Button(the_frame, padx=13, pady=11, text='3', font='lucida 25 bold')
button.pack(side='left', padx=4, pady=4)
button.bind('<Button-1>', click_fun)

button = Button(the_frame, padx=13, pady=11, text='2', font='lucida 25 bold')
button.pack(side='left', padx=4, pady=4)
button.bind('<Button-1>', click_fun)

button = Button(the_frame, padx=13, pady=11, text='1', font='lucida 25 bold')
button.pack(side='left', padx=4, pady=4)
button.bind('<Button-1>', click_fun)

the_frame = Frame(root, bg='gray')
the_frame.pack(padx=5, pady=5)

button = Button(the_frame, padx=13, pady=11, text='0', font='lucida 25 bold')
button.pack(side='left', padx=4, pady=4)
button.bind('<Button-1>', click_fun)

root.geometry('300x500')
root.mainloop()
