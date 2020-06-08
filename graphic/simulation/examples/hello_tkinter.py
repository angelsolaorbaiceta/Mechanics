from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

tk = Tk()
tk.title("Hello Tkinter")


def greet_user():
    messagebox.showinfo(
        'Greetings',
        f'Hello, {name.get()}'
    )


Label(tk, text='Enter your name:').grid(row=0, column=0)
name = StringVar()
Entry(tk, width=20, textvariable=name).grid(row=1, column=0)
Button(tk, text='Greet me', command=greet_user).grid(row=1, column=1)

tk.mainloop()
