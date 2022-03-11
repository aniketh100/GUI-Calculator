# introduction
# importing the modules required
import tkinter as tk
import math


def plus():
    # addition

    x = int(n1.get())
    y = int(n2.get())
    # getting the two numbers required

    global a
    a = (str(x + y))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    fn.close()


def minus():
    # subtraction

    x = int(n1.get())
    y = int(n2.get())
    # getting the two numbers required

    global a
    a = (str(x - y))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def divide():
    # division

    x = int(n1.get())
    y = int(n2.get())
    # getting the two numbers required

    global a
    a = (str(x / y))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def multiply():
    # multiplication

    x = int(n1.get())
    y = int(n2.get())
    # getting the two numbers required

    global a
    a = (str(x * y))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def log():
    # log function

    x = int(n1.get())
    global a
    a = (math.log(x, 10))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def sin():
    # sine function

    x = math.radians(int(n1.get()))
    global a
    a = (math.sin(x))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def cosec():
    # cosec function

    x = math.radians(int(n1.get()))
    global a
    a = (1 / math.sin(x))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def cos():
    # cosine function

    x = math.radians(int(n1.get()))
    global a
    a = (math.cos(x))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def sec():
    # sec function

    x = math.radians(int(n1.get()))
    global a
    a = (1 / math.cos(x))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def tan():
    # tan function

    x = math.radians(int(n1.get()))
    global a
    a = (math.tan(x))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def cot():
    # cot function

    x = math.radians(int(n1.get()))
    global a
    a = (1 / math.tan(x))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def quad():
    # quadratic function

    a = int(n1.get())
    b = int(n2.get())
    c = int(n3.get())
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        global x
        x = ((-b + sqrt_val) / (2 * a))
        global y
        y = ((-b - sqrt_val) / (2 * a))

        l['text'] = [x, y]
        # storing the answer in a separate file
        fn = open('Calc_History.txt', 'a+')
        fn.writelines(x + '\n')
        print()
        fn.close()

        # storing the answer in a separate file
        fn = open('Calc_History.txt', 'a+')
        fn.writelines(y + '\n')
        print()
        fn.close()


    elif dis == 0:
        print(" real and same roots")

        global z
        z = (-b / (2 * a))

        l['text'] = z

        # storing the answer in a separate file
        fn = open('Calc_History.txt', 'a+')
        fn.writelines(z + '\n')
        print()
        fn.close()

    # when discriminant is less than 0
    else:
        print("Complex Roots")

        x = (- b / (2 * a), " + i", sqrt_val)

        y = (- b / (2 * a), " - i", sqrt_val)

        l['text'] = [x, y]

        # storing the answer in a separate file
        fn = open('Calc_History.txt', 'a+')
        fn.writelines(x + '\n')
        print()
        fn.close()

        # storing the answer in a separate file
        fn = open('Calc_History.txt', 'a+')
        fn.writelines(y + '\n')
        print()
        fn.close()


def sqrroot():
    # square root function

    x = int(n1.get())
    global a
    a = (math.sqrt(x))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def cuberoot():
    # cube root function

    x = int(n1.get())
    global a
    a = (math.ceil(x ** (1 / 3)))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def nthroot():
    # function to find the nth root of a given number

    x = int(n1.get())
    y = int(n2.get())
    global a
    a = (math.ceil(x ** (1 / y)))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def factorial():
    # factorial function

    a = int(n1.get())

    def fact(a):
        if a == 1:
            return a
        else:
            return a * fact(a - 1)

    global x
    x = (fact(a))
    l['text'] = x

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(x + '\n')
    print()
    fn.close()


def exp():
    # exponent function

    x = int(n1.get())
    y = int(n2.get())
    global a
    a = (x ** y)
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def pi():
    # pi function

    x = int(n1.get())
    global a
    a = str(x * 3.14)
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def invEXP():
    # Finds x^-1 for given input of x

    x = int(n1.get())
    global a
    a = (x ** -1)
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def ln():
    # Finds natural log (log base e) of given inputted number

    x = int(n1.get())
    global a
    a = str(math.log(x, 2.718))
    l['text'] = a

    # storing the answer in a separate file
    fn = open('Calc_History.txt', 'a+')
    fn.writelines(a + '\n')
    print()
    fn.close()


def clear_hist():
    # clears history

    fn = open('Calc_History.txt', 'w+')
    fn.writelines('')
    print()
    fn.close()


def hist():
    # shows the history

    print('History:')
    fn = open('Calc_History.txt', 'r+')
    print(fn.read())
    print()
    fn.close()


# create a GUI window
top = tk.Tk()

# create a Buttons and place at a particular
# location inside the root window .
# when user press the button, the command or
# function affiliated to that button is executed .


l1 = tk.Label(top, text="Entry #1")
l1.grid(row=0, column=0, pady=2)

l2 = tk.Label(top, text="Entry #2")
l2.grid(row=1, column=0, pady=2)

l3 = tk.Label(top, text="Entry #3")
l3.grid(row=2, column=0, pady=2)

res = tk.Label(top, text="Result")
res.grid(row=3, column=0, pady=2)

l = tk.Label(top, text="-/-/-")
l.grid(row=3, column=1, pady=2)

n1 = tk.Entry(top)
n1.grid(row=0, column=1, pady=2)

n2 = tk.Entry(top)
n2.grid(row=1, column=1, pady=2)

n3 = tk.Entry(top)
n3.grid(row=2, column=1, pady=2)

his = tk.Button(top, text='History', fg='white', bg='SpringGreen2', command=hist, height=1, width=7)
his.grid(row=0, column=3, pady=2, ipadx=35)

clear = tk.Button(top, text='Clear Hist', fg='white', bg='SpringGreen3', command=clear_hist, height=1, width=7)
clear.grid(row=1, column=3, pady=2, ipadx=35)

add = tk.Button(top, text='+', fg='white', bg='grey', command=plus, height=1, width=7)
add.grid(row=4, column=0, ipadx=35)

sub = tk.Button(top, text='-', fg='white', bg='grey', command=minus, height=1, width=7)
sub.grid(row=4, column=1, ipadx=35)

mult = tk.Button(top, text='*', fg='white', bg='grey', command=multiply, height=1, width=7)
mult.grid(row=4, column=2, ipadx=35)

div = tk.Button(top, text='/', fg='white', bg='grey', command=divide, height=1, width=7)
div.grid(row=4, column=3, ipadx=35)

ex = tk.Button(top, text='x^n', fg='white', bg='red', command=exp, height=1, width=7)
ex.grid(row=5, column=0, ipadx=35)

sn = tk.Button(top, text='sin(x)', fg='gold', bg='black', command=sin, height=1, width=7)
sn.grid(row=5, column=1, ipadx=35)

cs = tk.Button(top, text='cos(x)', fg='gold', bg='black', command=cos, height=1, width=7)
cs.grid(row=5, column=2, ipadx=35)

tn = tk.Button(top, text='tan(x)', fg='gold', bg='black', command=tan, height=1, width=7)
tn.grid(row=5, column=3, ipadx=35)

lg = tk.Button(top, text='log(n)', fg='white', bg='red', command=log, height=1, width=7)
lg.grid(row=6, column=0, ipadx=35)

cosc = tk.Button(top, text='cosec(x)', fg='gold', bg='black', command=cosec, height=1, width=7)
cosc.grid(row=6, column=1, ipadx=35)

sc = tk.Button(top, text='sec(x)', fg='gold', bg='black', command=sec, height=1, width=7)
sc.grid(row=6, column=2, ipadx=35)

ct = tk.Button(top, text='cot(x)', fg='gold', bg='black', command=cot, height=1, width=7)
ct.grid(row=6, column=3, ipadx=35)

inv = tk.Button(top, text='x^-1', fg='white', bg='red', command=invEXP, height=1, width=7)
inv.grid(row=7, column=0, ipadx=35)

sqrt = tk.Button(top, text='sqrt', fg='black', bg='cyan', command=sqrroot, height=1, width=7)
sqrt.grid(row=7, column=1, ipadx=35)

cubrt = tk.Button(top, text='cbrt', fg='black', bg='cyan', command=cuberoot, height=1, width=7)
cubrt.grid(row=7, column=2, ipadx=35)

nrt = tk.Button(top, text='nroot', fg='black', bg='cyan', command=nthroot, height=1, width=7)
nrt.grid(row=7, column=3, ipadx=35)

ln = tk.Button(top, text='ln(x)', fg='white', bg='red', command=ln, height=1, width=7)
ln.grid(row=8, column=0, ipadx=35)

pii = tk.Button(top, text='π', fg='black', bg='gold', command=pi, height=1, width=7)
pii.grid(row=8, column=1, ipadx=35)

fact = tk.Button(top, text='fact', fg='black', bg='gold', command=factorial, height=1, width=7)
fact.grid(row=8, column=2, ipadx=35)

quadra = tk.Button(top, text='quad', fg='black', bg='gold', command=quad, height=1, width=7)
quadra.grid(row=8, column=3, ipadx=35)

# start the GUI
top.mainloop()
