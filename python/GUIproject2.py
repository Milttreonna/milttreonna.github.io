import tkinter


def make_total(var, x, y):
    num_total = x.get() * 1.50 + y.get() * 2.00
    var.set('${:.2f}'.format(num_total))


def click():
    counter.set(counter.get() + 1)


def negclick():
    counter.set(counter.get() - 1)


def click2():
    counter2.set(counter2.get() + 1)


def negclick2():
    counter2.set(counter2.get() - 1)


if __name__ == '__main__':
    window = tkinter.Tk()
    # The model
    counter = tkinter.IntVar()
    counter.set(0)
    counter2 = tkinter.IntVar()
    counter2.set(0)
    total_sum = tkinter.StringVar()
    total_sum.set('')
    # The views.
    frame = tkinter.Frame(window)
    frame.grid()
    first = tkinter.Label(frame,
                          text='Item           Price            Quantity ',
                          fg="magenta3")
    first.grid()
    frame2 = tkinter.Frame(window, borderwidth=3, relief=tkinter.RAISED)
    frame2.grid()

    second = tkinter.Label(frame2,
                           text='Coke:        $1.50       ',
                           fg="deep pink")
    second.grid(row=2, column=10)
    button = tkinter.Button(frame2, text='+', command=click)
    button.grid(row=2, column=40)
    label = tkinter.Label(frame2, textvariable=counter)
    label.grid(row=2, column=30)
    button = tkinter.Button(frame2, text='-', command=negclick)
    button.grid(row=2, column=20)

    third = tkinter.Label(frame2,
                          text='Chips:        $2.00       ',
                          fg="hotpink1")
    third.grid(row=1, column=10)
    button = tkinter.Button(frame2, text='+', command=click2)
    button.grid(row=1, column=40)
    label = tkinter.Label(frame2, textvariable=counter2)
    label.grid(row=1, column=30)
    button = tkinter.Button(frame2, text='-', command=negclick2)
    button.grid(row=1, column=20)

    fourth = tkinter.Button(
        frame2,
        text='Total:',
        command=lambda: make_total(total_sum, counter, counter2))
    fourth.grid(row=3, column=10)
    total = tkinter.Label(frame2, textvariable=total_sum)
    total.grid(row=3, column=20)
    # Start the machinery
    window.mainloop()
