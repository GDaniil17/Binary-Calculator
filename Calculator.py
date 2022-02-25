from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb

root = Tk()

def bin_(num):
    ans = ""
    if(not num):
        return "0"
    while(num):
        ans = str(num%2)+ans
        num //= 2
    return ans

def int_(num, base):
    ans = 0
    alp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    k = len(num)-1
    for i in num:
        ans += base**k*alp.index(i)
        k -= 1
    return ans

lab_1 = Label(root, text="a = ", font="Arial 18",justify=CENTER)
lab_1.config(font=("Courier", 20))
lab_1.pack(fill=tk.X)

ent_1_text = StringVar()
ent_1 = Entry(root,width=20, bd=5, textvariable = ent_1_text)
ent_1.config(font=("Courier", 20))
ent_1.pack(fill=tk.X)

var_a=IntVar()
var_a.set(1)
rad_a0 = Radiobutton(root,text="2-чная",
variable=var_a,value=0)
rad_a1 = Radiobutton(root,text="8-чная",
variable=var_a,value=1)
rad_a2 = Radiobutton(root,text="16-чная",
variable=var_a,value=2)
rad_a0.config(font=("Courier", 20))
rad_a1.config(font=("Courier", 20))
rad_a2.config(font=("Courier", 20))

rad_a0.pack()
rad_a1.pack()
rad_a2.pack()

choices = ['+', '-', '/', '*']
variable = StringVar(root)
variable.set('+')
w = OptionMenu(root, variable, *choices)
w.config(font="Arial 18")
w.pack()

lab = Label(root, text="b = ", font="Arial 18", justify=CENTER)
lab.config(font=("Courier", 20))
lab.pack(fill=tk.X)

ent_2_text = StringVar()
ent_2 = Entry(root,width=20, bd=5, textvariable=ent_2_text)
ent_2.config(font=("Courier", 20))
ent_2.pack(fill=tk.X)

var=IntVar()
var.set(1)
rad0 = Radiobutton(root,text="2-чная",
variable=var,value=0)
rad1 = Radiobutton(root,text="8-чная",
variable=var,value=1)
rad2 = Radiobutton(root,text="16-чная",
variable=var,value=2)

rad0.config(font=("Courier", 20))
rad1.config(font=("Courier", 20))
rad2.config(font=("Courier", 20))
rad0.pack()
rad1.pack()
rad2.pack()

lab_ans = Label(root, text="ans = ", font="Arial 18", justify=CENTER)
lab_ans.config(font=("Courier", 20))
lab_ans.pack(fill=tk.X)

var_ans=IntVar()
var_ans.set(1)
rad_ans0 = Radiobutton(root,text="2-чная",
variable=var_ans,value=0)
rad_ans1 = Radiobutton(root,text="8-чная",
variable=var_ans,value=1)
rad_ans2 = Radiobutton(root,text="16-чная",
variable=var_ans,value=2)

rad_ans0.config(font=("Courier", 20))
rad_ans1.config(font=("Courier", 20))
rad_ans2.config(font=("Courier", 20))
rad_ans0.pack()
rad_ans1.pack()
rad_ans2.pack()

lab_res = Label(root, text="", font="Arial 18", justify=CENTER)
lab_res.config(font=("Courier", 20))
lab_res.pack(fill=tk.X)

def submit_fun():
    global var_a
    global var
    global var_ans
    global ent_1_text
    global ent_2_text
    global lab_res
    global variable
    set_2 = {'0', '1'}
    set_8 = {'0', '1', '2', '3', '4', '5', '6', '7'}
    set_16 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'}

    if(var_a.get() == 0):
        if(ent_1_text.get() == "" or len(set(ent_1_text.get().upper()).difference(set_2)) != 0):
            mb.askyesno(title="!", message="Проверьте 2-чную запись числа")
            return
        else:
            first_10 = int_(ent_1_text.get(), 2)
            
    elif(var_a.get() == 1):
        if(ent_1_text.get() == "" or len(set(ent_1_text.get().upper()).difference(set_8)) != 0):
            mb.askyesno(title="!", message="Проверьте 8-чную запись числа")
            return
        else:
            first_10 = int_(ent_1_text.get(), 8)
            
    elif(var_a.get() == 2):
        if(ent_1_text.get() == "" or len(set(ent_1_text.get().upper()).difference(set_16)) != 0):
            mb.askyesno(title="!", message="Проверьте 16-чную запись числа")
            return
        else:
            first_10 = int_(ent_1_text.get(), 16)
            

    if(var.get() == 0):
        if(ent_2_text.get() == "" or len(set(ent_2_text.get().upper()).difference(set_2)) != 0):
            mb.askyesno(title="!", message="Проверьте 2-чную запись числа")
            return
        else:
            second_10 = int_(ent_2_text.get(), 2)
            
    elif(var.get() == 1):
        if(ent_2_text.get() == "" or len(set(ent_2_text.get().upper()).difference(set_8)) != 0):
            mb.askyesno(title="!", message="Проверьте 8-чную запись числа")
            return
        else:
            second_10 = int_(ent_2_text.get(), 8)
            
    elif(var.get() == 2):
        if(ent_2_text.get() == "" or len(set(ent_2_text.get().upper()).difference(set_16)) != 0):
            mb.askyesno(title="!", message="Проверьте 16-чную запись числа")
            return
        else:
            second_10 = int_(ent_2_text.get(), 16)
    ans = ""
    long = False
    integer = ""
    match variable.get():
        case '+':
            ans = (first_10+second_10)
            integer = bin_(ans)

        case '-':
            if(first_10 < second_10):
                mb.askyesno(title="!", message="Первое число должно быть больше второго!")
                return
            ans = (first_10-second_10)
            integer = bin_(ans)

        case '/':
            if(second_10 == 0):
                mb.askyesno(title="!", message="Второе число не должно быть 0!")
                return
            ans = (first_10/second_10)

            integer = bin_(int(ans//1))
            frac = ""
            if(ans%1 > 10**-6):
                long = True
                a = ans
                a %= 1
                while(a%1 > 10**-6):
                    a *= 2
                    frac += str(int(a // 1))
                    a %= 1

        case '*':
            ans = (first_10*second_10)
            integer = bin_(ans)
            
    set_2 = ['0', '1']
    set_8 = ['0', '1', '2', '3', '4', '5', '6', '7']
    set_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if(var_ans.get() == 0):
        if(long):
            ans = integer+"."+frac
        else:
            ans = integer
    elif(var_ans.get() == 1):
        need = len(integer)//3+bool(len(integer)%3)
        integer = (3*need - len(integer))*"0"+integer
        ans_8 = ""
        for i in range(0, need*3, 3):
            ans_8 += set_8[int_(integer[i:i+3], 2)]

        if(long):
            need = len(frac)//3+bool(len(frac)%3)
            integer = frac+(3*need - len(frac))*"0"
            ans_8 += "."
            for i in range(0, need*3, 3):
                ans_8 += set_8[int_(frac[i:i+3], 2)]
        ans = ans_8
            
    elif(var_ans.get() == 2):
        need = len(integer)//4+bool(len(integer)%4)
        integer = (4*need - len(integer))*"0"+integer
        ans_16 = ""
        for i in range(0, need*4, 4):
            ans_16 += set_16[int_(integer[i:i+4], 2)]
        if(long):
            need = len(frac)//4+bool(len(frac)%4)
            frac = frac+(4*need - len(frac))*"0"
            ans_16 += "."
            for i in range(0, need*4, 4):
                ans_16 += set_16[int_(frac[i:i+4], 2)]
        ans = ans_16
    lab_res.config(text = ans)
    
b1 = Button(text = "Submit", font=("Time New Roman", 40)) #width = len(rand)*10, height = 3)
b1.config(command = submit_fun,font=("Courier", 20))
b1.pack(fill=tk.X)

root.mainloop()


