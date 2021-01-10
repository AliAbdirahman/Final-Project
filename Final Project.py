select_typeof_Calculator= input ("Can you please type of calculator you want to use. The differents of calculators are: Scientific Calculator, Quadratic Calculator, Add 2*2 Matrix, Subtract 2*2 Matrix, Multiply 2*2 Matrix, Divide 2*2 Matrix, Inverse 2*2 Matrix, Discriminant 2*2 Matrix, Product 2*2 Matrix, Add 3*3 Matrix, Subtract 3*3 Matrix, Multiply 3*3 Matrix, Divide 3*3 Matrix, Discriminant 3*3 Matrix, Product 3*3 Matrix?")
#================================Scientific Calculator========================================
if select_typeof_Calculator=="Scientific Calculator":
    from tkinter import *
    import math as m
    root= Tk()
    root.title("Scientific Calculator")
    entry= Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")#This entry is to display the numbers pressed and the result of the entered exponentression
    entry.grid(row=0, column=0, columnspan=5, padx=10, pady=15)
    def press(to_print):#This function is called whenever any average number is pressed and BODMAS like 1,2,+,- and *
        old=entry.get()#set variable old to the whatever is in the entry e
        entry.delete(0, END)# Delete everything previously in the entry
        entry.insert(0, old+to_print)#insert everything originally in the entry with the currently pressed button into the entry
        return
    def complex_operation(event):#Event catches whatever your action needs to perform
        key=event.widget #store the event in the variable key
        text=key['text'] # convert from event to string and store in the variable text
        input_number=entry.get() # store the given entry in the variable no
        result=''#variable result is used to store the result of if conditions
        if text=='deg':# if the given event is deg preform the action below
            result=str(m.degrees(float(input_number)))# we find the degree of a function using the degree method in the math library
        if text=='sin':#The rest of the if statement similiar as the first, check if a specific even is called on and then preofrm that event using the math library
            result=str(m.sin(float(input_number)))
        if text=='cos':
            result=str(m.cos(float(input_number)))
        if text=='tan':
            result=str(m.tan(float(input_number)))
        if text=='lg':
            result=str(m.log10(float(input_number)))
        if text=='ln':
            result=str(m.log(float(input_number)))
        if text=='Sqrt':
            result=str(m.sqrt(float(input_number)))
        if text=='x!':
            result=str(m.factorialorial(float(input_number)))
        if text=='1/x':
            result=str(1/(float(input_number)))
        if text=='pi':
            if no=="":#The extra if statement is used incase the user wants to find out what value corrospondes with pi
                result=str(m.pi)
            else:
                result=str(float(input_number) * m.pi)
        if text=='e':
            if no=="":#The extra if statement is used incase the user wants to find out what value corrospondes with e
                result=str(m.e)
            else:
                result=str(m.e**float(input_number))
        entry.delete(0, END)# Delet everything in entry
        entry.insert(0, result)# Display the Answer

    def clear():
        entry.delete(0, END)# delete everything from start of entry to end
        return
    def delete_last():
        current_position=entry.get()# store everything in the entry tab in the variable current
        length_of_entry=len(current_position)-1 # get the length of entry minus 1
        entry.delete(length_of_entry, END)#you delete everything between length and the end of entry, meaning that you will be deleteing the last entry
    def evaluate():
        answer=entry.get()# store everything in the entry tab in the variable ans
        answer=eval(answer)# eval takes the string and evaluates that string, the evaluated string is the answer or the solution of the given string, so you set ans as the evaluate string or the ans of string
        entry.delete(0, END)# Delete everything in entry
        entry.insert(0, answer)#Display the Ans
        
    #==========================The section below ia about making the button and defining the size, the color and what function is called when this button is pressed===========================#

        
    lg = Button(root, text="lg", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
    lg.bind("<Button-1>", complex_operation)
    ln = Button(root, text="ln", padx=26, pady=10, relief=RAISED, bg="Black", fg="White")
    ln.bind("<Button-1>", complex_operation)
    lg = Button(root, text="lg", padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
    lg.bind("<Button-1>", complex_operation)
    degb = Button(root, text="deg", padx=24, pady=10, relief=RAISED, bg="Black", fg="White")
    degb.bind("<Button-1>", complex_operation)
    sinb = Button(root, text="sin", padx=25, pady=10, relief=RAISED, bg="Black", fg="White")
    sinb.bind("<Button-1>", complex_operation)
    cosb = Button(root, text="cos", padx=25, pady=10, relief=RAISED, bg="Black", fg="White")
    cosb.bind("<Button-1>", complex_operation)
    tanb = Button(root, text="tan", padx=25, pady=10, relief=RAISED, bg="Black", fg="White")
    tanb.bind("<Button-1>", complex_operation)

    squareroot = Button(root, text="Sqrt", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
    squareroot.bind("<Button-1>", complex_operation)
    factorial = Button(root, text="x!", padx=29, pady=10, relief=RAISED, bg="Black", fg="White")
    factorial.bind("<Button-1>", complex_operation)
    inverse = Button(root, text="1/x", padx=25, pady=10, relief=RAISED, bg="Black", fg="White")
    inverse.bind("<Button-1>", complex_operation)
    pib = Button(root, text="pi", padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
    pib.bind("<Button-1>", complex_operation)
    e_b = Button(root, text="e", padx=27, pady=10, relief=RAISED, bg="#003366", fg="White")
    e_b.bind("<Button-1>", complex_operation)
    ac= Button(root, text="C", padx=26, pady=10, relief=RAISED, bg="red", fg="White", command=lambda:clear())
    backspace = Button(root, text="backspace", padx=7, pady=10, relief=RAISED, bg="#003366", fg="White", command=lambda:delete_last())
    equal = Button(root, text="=", padx=25, pady=10, relief=RAISED, bg="green", fg="White", command=lambda: evaluate())
    mod = Button(root, text="mod", padx=18, pady=10, relief=RAISED, bg="#003366", fg="White", command=lambda: press("%"))
    zero = Button(root, text="0", padx=26.5, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: press("0"))
    par1st=  Button(root, text="(", padx=28, pady=10, relief=RAISED, bg="#003366", fg="White", command=lambda: press("("))
    par2nd=  Button(root, text=")", padx=28, pady=10, relief=RAISED, bg="#003366", fg="White", command=lambda: press(")"))
    dot =  Button(root, text=".", padx=27.5, pady=10, relief=RAISED, bg="#003366", fg="White", command=lambda: press("."))
    exponent = Button(root, text="^", padx=26, pady=10, relief=RAISED, bg="#003366", fg="White", command=lambda: press("**"))
    divide =  Button(root, text="/", padx=27, pady=10, relief=RAISED, bg="#003366", fg="White", command=lambda: press("/"))
    one = Button(root, text="1", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: press("1"))
    two = Button(root, text="2", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: press("2"))
    three = Button(root, text="3", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: press("3"))
    four = Button(root, text="4", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: press("4"))
    five = Button(root, text="5", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: press("5"))
    six = Button(root, text="6", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: press("6"))
    seven = Button(root, text="7", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: press("7"))
    eight = Button(root, text="8", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: press("8"))
    nine = Button(root, text="9", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: press("9"))
    multiplication= Button(root, text="*", padx=27, pady=10, relief=RAISED, bg="#003366", fg="White", command=lambda: press("*"))
    plus = Button(root, text="+", padx=26, pady=10, relief=RAISED, bg="#003366", fg="White", command=lambda: press("+"))
    minus = Button(root, text="-", padx=27, pady=10, relief=RAISED, bg="#003366", fg="White", command=lambda: press("-"))

    #============================= The section below is about defining the position of different button===============================#

    lg.grid(row=1, column=0)
    ln.grid(row=1, column=1)
    sinb.grid(row=1, column=2)
    cosb.grid(row=1, column=3)
    tanb.grid(row=1, column=4)
    degb.grid(row=2, column=0)
    exponent.grid(row=2, column=1)
    par1st.grid(row=2, column=2)
    par2nd.grid(row=2, column=3)
    dot.grid(row=2, column=4)
    squareroot.grid(row=3, column=0)
    ac.grid(row=3, column=1)
    backspace.grid(row=3, column=2)
    mod.grid(row=3, column=3)
    divide.grid(row=3, column=4)
    factorial.grid(row=4, column=0)
    seven.grid(row=4, column=1)
    eight.grid(row=4, column=2)
    nine.grid(row=4, column=3)
    multiplication.grid(row=4, column=4)
    inverse.grid(row=5, column=0)
    four.grid(row=5, column=1)
    five.grid(row=5, column=2)
    six.grid(row=5, column=3)
    minus.grid(row=5, column=4)
    pib.grid(row=6, column=0)
    one.grid(row=6, column=1)
    two.grid(row=6, column=2)
    three.grid(row=6, column=3)
    plus.grid(row=6, column=4)
    e_b.grid(row=7, column=1)
    zero.grid(row=7, column=2)
    equal.grid(row=7, column=3)
#============================================Quadratic Calculator=====================================================================================
if select_typeof_Calculator=="Quadratic Calculator":
    from tkinter import *
    from math import sqrt

    def calculator_Function(a,b,c):# This function is how we calculate the x-value in a quaratic equation, the a,b,c are the variable coefficient in the quaratic equation
        Discriminant = b*b - 4*a*c
        if Discriminant >= 0:#Thsi if function checks if the discriminant is negative and if it is the quadratic equation has imaginary solution        
            x1 = (-b + sqrt(Discriminant)) / (2*a)#Quadratic formula
            x2 = (-b - sqrt(Discriminant)) / (2*a)#Quadratic formula
            if x1==x2:#This if function check if there are 2 or 1 solution if 1 just display 1 solution for x
                text= "The discriminant is: %s \n The X-value = %s" % (Discriminant,x1)
            else:
                text = "The discriminant is: %s \n X1 is: %s \n X2 is: %s \n" % (Discriminant, x1, x2)        
        else:#Below is what is displayed if the quaratic equation has no real solutions
            text = "The discriminant is: %s \nThis quadratic equation has no real solutions" % (Discriminant)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)    

    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator to be solved
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient))
    root = Tk()
    root.title("Quadratic calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)
    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    #Creating labels
    a_input = Label(frame, text="x^2+")
    b_input = Label(frame, text="x+")
    c_input = Label(frame, text="= 0")
    Solve_button = Button(frame, text="Solve", command=variable_input_function)

    output = Text(frame, bg="light green", font="Arial 12", width=35, height=10)#background color, size and etc.
    #Location of everything
    output.grid(row=2, columnspan=8)
    a.grid(row=1,column=1,padx=(10,0))
    b.grid(row=1,column=3)
    c.grid(row=1, column=5)
    a_input.grid(row=1,column=2)
    b_input.grid(row=1, column=4)
    c_input.grid(row=1, column=6)
    Solve_button.grid(row=1, column=7, padx=(10,0))
    root.mainloop()

#============================================2x2 Inverse Matrix Calculator=========================
if select_typeof_Calculator=="Inverse 2*2 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d):
        A = np.array([[a, b],
                      [c, d]])
        text= np.linalg.inv(A)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient))
    root = Tk()
    root.title("2x2-Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=5)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=5)
    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=5)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=5)
    d.bind("<FocusIn>", clear)

    #Creating labels and buttons

    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=10, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light green", font="Arial 12", width=35, height=10)#background color, size and etc.

    #Location of everything

    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1,column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    closing_parenthesis.grid(row=1,column=4)
    opening_parenthesis2.grid(row=2,column=0)
    c.grid(row=2, column=1)
    comma2.grid(row=2,column=2)
    d.grid(row=2, column=3)
    closing_parenthesis2.grid(row=2,column=4)
    Solve_button.grid(row=1, column=5, padx=(0,0))
    output.grid(row=3, columnspan=8)
    root.mainloop()
#=================================2x2 Multiplying Matrices Calculator=======================-------==========-=-==================-=-==========
if select_typeof_Calculator=="Multiply 2*2 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d,e,f,g,h):
        x = np.array([[a, b],
                      [c, d]])
        y = np.array([[e, f],
                      [g, h]])
        text= np.multiply(x,y)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        e_coefficient = float(e.get())
        f_coefficient = float(f.get())
        g_coefficient = float(g.get())
        h_coefficient = float(h.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient, e_coefficient, f_coefficient, g_coefficient, h_coefficient))
    root = Tk()
    root.title("2x2-Multiply Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)

    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=3)
    d.bind("<FocusIn>", clear)
    e = Entry(frame, width=3)
    e.bind("<FocusIn>", clear)
    f = Entry(frame, width=3)
    f.bind("<FocusIn>", clear)
    g = Entry(frame, width=3)
    g.bind("<FocusIn>", clear)

    h = Entry(frame, width=3)
    h.bind("<FocusIn>", clear)
    #Creating labels and buttons

    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    add_symbol= Label(frame, text="*")
    add_symbol.config(font=("Courier", 20))
    opening_parenthesis3 = Label(frame, text="[")
    opening_parenthesis3.config(font=("Courier", 20))
    comma3 = Label(frame, text=",")
    comma3.config(font=("Courier", 20))
    closing_parenthesis3 = Label(frame, text="]")
    closing_parenthesis3.config(font=("Courier", 20))
    opening_parenthesis4 = Label(frame, text="[")
    opening_parenthesis4.config(font=("Courier", 20))
    comma4 = Label(frame, text=",")
    comma4.config(font=("Courier", 20))
    closing_parenthesis4 = Label(frame, text="]")
    closing_parenthesis4.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=7, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light grey", font="Arial 12", width=30, height=10)#background color, size and etc.

    #Location of everything

    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1,column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    closing_parenthesis.grid(row=1,column=4)
    add_symbol.grid(row=1, column=5)
    opening_parenthesis3.grid(row=1,column=6)
    e.grid(row=1,column=7)
    comma3.grid(row=1,column=8)
    f.grid(row=1,column=9)
    closing_parenthesis3.grid(row=1,column=10)
    opening_parenthesis2.grid(row=2,column=0)
    c.grid(row=2, column=1)
    comma2.grid(row=2,column=2)
    d.grid(row=2, column=3)
    closing_parenthesis2.grid(row=2,column=4)
    opening_parenthesis4.grid(row=2,column=6)
    g.grid(row=2,column=7)
    comma4.grid(row=2,column=8)
    h.grid(row=2,column=9)
    closing_parenthesis4.grid(row=2,column=10)
    Solve_button.grid(row=1, column=11, padx=(0,0))
    output.grid(row=3, columnspan=8)
    root.mainloop()
#================================2x2 Adding Matrices=============================++++++++++========================================
if select_typeof_Calculator=="Add 2*2 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d,e,f,g,h):
        x = np.array([[a, b],
                      [c, d]])
        y = np.array([[e, f],
                      [g, h]])
        text= np.multiply(x,y)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        e_coefficient = float(e.get())
        f_coefficient = float(f.get())
        g_coefficient = float(g.get())
        h_coefficient = float(h.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient, e_coefficient, f_coefficient, g_coefficient, h_coefficient))
    root = Tk()
    root.title("2x2-Multiply Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)

    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=3)
    d.bind("<FocusIn>", clear)
    e = Entry(frame, width=3)
    e.bind("<FocusIn>", clear)
    f = Entry(frame, width=3)
    f.bind("<FocusIn>", clear)
    g = Entry(frame, width=3)
    g.bind("<FocusIn>", clear)

    h = Entry(frame, width=3)
    h.bind("<FocusIn>", clear)
    #Creating labels and buttons

    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    add_symbol= Label(frame, text="*")
    add_symbol.config(font=("Courier", 20))
    opening_parenthesis3 = Label(frame, text="[")
    opening_parenthesis3.config(font=("Courier", 20))
    comma3 = Label(frame, text=",")
    comma3.config(font=("Courier", 20))
    closing_parenthesis3 = Label(frame, text="]")
    closing_parenthesis3.config(font=("Courier", 20))
    opening_parenthesis4 = Label(frame, text="[")
    opening_parenthesis4.config(font=("Courier", 20))
    comma4 = Label(frame, text=",")
    comma4.config(font=("Courier", 20))
    closing_parenthesis4 = Label(frame, text="]")
    closing_parenthesis4.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=7, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light grey", font="Arial 12", width=30, height=10)#background color, size and etc.

    #Location of everything

    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1,column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    closing_parenthesis.grid(row=1,column=4)
    add_symbol.grid(row=1, column=5)
    opening_parenthesis3.grid(row=1,column=6)
    e.grid(row=1,column=7)
    comma3.grid(row=1,column=8)
    f.grid(row=1,column=9)
    closing_parenthesis3.grid(row=1,column=10)
    opening_parenthesis2.grid(row=2,column=0)
    c.grid(row=2, column=1)
    comma2.grid(row=2,column=2)
    d.grid(row=2, column=3)
    closing_parenthesis2.grid(row=2,column=4)
    opening_parenthesis4.grid(row=2,column=6)
    g.grid(row=2,column=7)
    comma4.grid(row=2,column=8)
    h.grid(row=2,column=9)
    closing_parenthesis4.grid(row=2,column=10)
    Solve_button.grid(row=1, column=11, padx=(0,0))
    output.grid(row=3, columnspan=8)
    root.mainloop()
#=================================2x2 Product matrix calculator==================+++===========================================
if select_typeof_Calculator=="Product 2*2 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d,e,f,g,h):
        x = np.array([[a, b],
                      [c, d]])
        y = np.array([[e, f],
                      [g, h]])
        text= np.dot(x,y)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        e_coefficient = float(e.get())
        f_coefficient = float(f.get())
        g_coefficient = float(g.get())
        h_coefficient = float(h.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient, e_coefficient, f_coefficient, g_coefficient, h_coefficient))
    root = Tk()
    root.title("2x2-Product Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)

    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=3)
    d.bind("<FocusIn>", clear)
    e = Entry(frame, width=3)
    e.bind("<FocusIn>", clear)
    f = Entry(frame, width=3)
    f.bind("<FocusIn>", clear)
    g = Entry(frame, width=3)
    g.bind("<FocusIn>", clear)

    h = Entry(frame, width=3)
    h.bind("<FocusIn>", clear)
    #Creating labels and buttons

    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    add_symbol= Label(frame, text=".")
    add_symbol.config(font=("Courier", 20))
    opening_parenthesis3 = Label(frame, text="[")
    opening_parenthesis3.config(font=("Courier", 20))
    comma3 = Label(frame, text=",")
    comma3.config(font=("Courier", 20))
    closing_parenthesis3 = Label(frame, text="]")
    closing_parenthesis3.config(font=("Courier", 20))
    opening_parenthesis4 = Label(frame, text="[")
    opening_parenthesis4.config(font=("Courier", 20))
    comma4 = Label(frame, text=",")
    comma4.config(font=("Courier", 20))
    closing_parenthesis4 = Label(frame, text="]")
    closing_parenthesis4.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=7, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light grey", font="Arial 12", width=30, height=10)#background color, size and etc.

    #Location of everything

    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1,column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    closing_parenthesis.grid(row=1,column=4)
    add_symbol.grid(row=1, column=5)
    opening_parenthesis3.grid(row=1,column=6)
    e.grid(row=1,column=7)
    comma3.grid(row=1,column=8)
    f.grid(row=1,column=9)
    closing_parenthesis3.grid(row=1,column=10)
    opening_parenthesis2.grid(row=2,column=0)
    c.grid(row=2, column=1)
    comma2.grid(row=2,column=2)
    d.grid(row=2, column=3)
    closing_parenthesis2.grid(row=2,column=4)
    opening_parenthesis4.grid(row=2,column=6)
    g.grid(row=2,column=7)
    comma4.grid(row=2,column=8)
    h.grid(row=2,column=9)
    closing_parenthesis4.grid(row=2,column=10)
    Solve_button.grid(row=1, column=11, padx=(0,0))
    output.grid(row=3, columnspan=8)
    root.mainloop()
#=================================2x2 Dividing Matrices======================================================================================
if select_typeof_Calculator=="Divide 2*2 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d,e,f,g,h):
        x = np.array([[a, b],
                      [c, d]])
        y = np.array([[e, f],
                      [g, h]])
        text= np.divide(x,y)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        e_coefficient = float(e.get())
        f_coefficient = float(f.get())
        g_coefficient = float(g.get())
        h_coefficient = float(h.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient, e_coefficient, f_coefficient, g_coefficient, h_coefficient))
    root = Tk()
    root.title("2x2-Divide Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)

    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=3)
    d.bind("<FocusIn>", clear)
    e = Entry(frame, width=3)
    e.bind("<FocusIn>", clear)
    f = Entry(frame, width=3)
    f.bind("<FocusIn>", clear)
    g = Entry(frame, width=3)
    g.bind("<FocusIn>", clear)

    h = Entry(frame, width=3)
    h.bind("<FocusIn>", clear)
    #Creating labels and buttons

    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    add_symbol= Label(frame, text="/")
    add_symbol.config(font=("Courier", 20))
    opening_parenthesis3 = Label(frame, text="[")
    opening_parenthesis3.config(font=("Courier", 20))
    comma3 = Label(frame, text=",")
    comma3.config(font=("Courier", 20))
    closing_parenthesis3 = Label(frame, text="]")
    closing_parenthesis3.config(font=("Courier", 20))
    opening_parenthesis4 = Label(frame, text="[")
    opening_parenthesis4.config(font=("Courier", 20))
    comma4 = Label(frame, text=",")
    comma4.config(font=("Courier", 20))
    closing_parenthesis4 = Label(frame, text="]")
    closing_parenthesis4.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=7, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light grey", font="Arial 12", width=30, height=10)#background color, size and etc.

    #Location of everything

    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1,column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    closing_parenthesis.grid(row=1,column=4)
    add_symbol.grid(row=1, column=5)
    opening_parenthesis3.grid(row=1,column=6)
    e.grid(row=1,column=7)
    comma3.grid(row=1,column=8)
    f.grid(row=1,column=9)
    closing_parenthesis3.grid(row=1,column=10)
    opening_parenthesis2.grid(row=2,column=0)
    c.grid(row=2, column=1)
    comma2.grid(row=2,column=2)
    d.grid(row=2, column=3)
    closing_parenthesis2.grid(row=2,column=4)
    opening_parenthesis4.grid(row=2,column=6)
    g.grid(row=2,column=7)
    comma4.grid(row=2,column=8)
    h.grid(row=2,column=9)
    closing_parenthesis4.grid(row=2,column=10)
    Solve_button.grid(row=1, column=11, padx=(0,0))
    output.grid(row=3, columnspan=8)
    root.mainloop()


#=================================2x2 Subtracting Matrices=============================================================================================
if select_typeof_Calculator=="Subtract 2*2 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d,e,f,g,h):
        x = np.array([[a, b],
                      [c, d]])
        y = np.array([[e, f],
                      [g, h]])
        text= np.subtract(x,y)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget


    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        e_coefficient = float(e.get())
        f_coefficient = float(f.get())
        g_coefficient = float(g.get())
        h_coefficient = float(h.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient, e_coefficient, f_coefficient, g_coefficient, h_coefficient))
    root = Tk()
    root.title("2x2-Add Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)

    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=3)
    d.bind("<FocusIn>", clear)
    e = Entry(frame, width=3)
    e.bind("<FocusIn>", clear)
    f = Entry(frame, width=3)
    f.bind("<FocusIn>", clear)
    g = Entry(frame, width=3)
    g.bind("<FocusIn>", clear)

    h = Entry(frame, width=3)
    h.bind("<FocusIn>", clear)
    #Creating labels and buttons

    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    add_symbol= Label(frame, text="-")
    add_symbol.config(font=("Courier", 20))
    opening_parenthesis3 = Label(frame, text="[")
    opening_parenthesis3.config(font=("Courier", 20))
    comma3 = Label(frame, text=",")
    comma3.config(font=("Courier", 20))
    closing_parenthesis3 = Label(frame, text="]")
    closing_parenthesis3.config(font=("Courier", 20))
    opening_parenthesis4 = Label(frame, text="[")
    opening_parenthesis4.config(font=("Courier", 20))
    comma4 = Label(frame, text=",")
    comma4.config(font=("Courier", 20))
    closing_parenthesis4 = Label(frame, text="]")
    closing_parenthesis4.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=7, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light grey", font="Arial 12", width=30, height=10)#background color, size and etc.

    #Location of everything

    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1,column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    closing_parenthesis.grid(row=1,column=4)
    add_symbol.grid(row=1, column=5)
    opening_parenthesis3.grid(row=1,column=6)
    e.grid(row=1,column=7)
    comma3.grid(row=1,column=8)
    f.grid(row=1,column=9)
    closing_parenthesis3.grid(row=1,column=10)
    opening_parenthesis2.grid(row=2,column=0)
    c.grid(row=2, column=1)
    comma2.grid(row=2,column=2)
    d.grid(row=2, column=3)
    closing_parenthesis2.grid(row=2,column=4)
    opening_parenthesis4.grid(row=2,column=6)
    g.grid(row=2,column=7)
    comma4.grid(row=2,column=8)
    h.grid(row=2,column=9)
    closing_parenthesis4.grid(row=2,column=10)
    Solve_button.grid(row=1, column=11, padx=(0,0))
    output.grid(row=3, columnspan=8)
    root.mainloop()

#========================================2x2 Detriminant Calculator======================================================================================
if select_typeof_Calculator=="Discriminant 2*2 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d):
        A = np.array([[a, b],
                      [c, d]])
        determinant = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
        return determinant

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient))
    root = Tk()
    root.title("2x2-Determinant Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=5)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=5)
    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=5)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=5)
    d.bind("<FocusIn>", clear)

    #Creating labels and buttons

    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=10, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light green", font="Arial 12", width=35, height=10)#background color, size and etc.

    #Location of everything

    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1,column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    closing_parenthesis.grid(row=1,column=4)
    opening_parenthesis2.grid(row=2,column=0)
    c.grid(row=2, column=1)
    comma2.grid(row=2,column=2)
    d.grid(row=2, column=3)
    closing_parenthesis2.grid(row=2,column=4)
    Solve_button.grid(row=1, column=5, padx=(0,0))
    output.grid(row=3, columnspan=8)
    root.mainloop()
#===================================3x3 Multiply Matrix Calculator===================================================================
if select_typeof_Calculator=="Multiply 3*3 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
        x = np.array([[a, b, c],
                      [d, e, f],
                      [g, h, i]])
        y= np.array([[j, k, l],
                     [m, n, o],
                     [p, q, r]])
        text= np.multiply(x,y)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        e_coefficient = float(e.get())
        f_coefficient = float(f.get())
        g_coefficient = float(g.get())
        h_coefficient = float(h.get())
        i_coefficient = float(i.get())
        j_coefficient = float(j.get())
        k_coefficient = float(k.get())
        l_coefficient = float(l.get())
        m_coefficient = float(m.get())
        n_coefficient = float(n.get())
        o_coefficient = float(o.get())
        p_coefficient = float(p.get())
        q_coefficient = float(q.get())
        r_coefficient = float(r.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient, e_coefficient, f_coefficient, g_coefficient, h_coefficient, i_coefficient, j_coefficient, k_coefficient, l_coefficient, m_coefficient, n_coefficient, o_coefficient, p_coefficient, q_coefficient, r_coefficient))
    root = Tk()
    root.title("3x3-multiply Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)
    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=3)
    d.bind("<FocusIn>", clear)
    e = Entry(frame, width=3)
    e.bind("<FocusIn>", clear)
    f = Entry(frame, width=3)
    f.bind("<FocusIn>", clear)
    g = Entry(frame, width=3)
    g.bind("<FocusIn>", clear)
    h = Entry(frame, width=3)
    h.bind("<FocusIn>", clear)
    i = Entry(frame, width=3)
    i.bind("<FocusIn>", clear)
    j = Entry(frame, width=3)
    j.bind("<FocusIn>", clear)
    k = Entry(frame, width=3)
    k.bind("<FocusIn>", clear)
    l = Entry(frame, width=3)
    l.bind("<FocusIn>", clear)
    m = Entry(frame, width=3)
    m.bind("<FocusIn>", clear)
    n = Entry(frame, width=3)
    n.bind("<FocusIn>", clear)
    o = Entry(frame, width=3)
    o.bind("<FocusIn>", clear)
    p = Entry(frame, width=3)
    p.bind("<FocusIn>", clear)
    q = Entry(frame, width=3)
    q.bind("<FocusIn>", clear)
    r = Entry(frame, width=3)
    r.bind("<FocusIn>", clear)
    #Creating labels and buttons
    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    opening_parenthesis3 = Label(frame, text="[")
    opening_parenthesis3.config(font=("Courier", 20))
    opening_parenthesis4 = Label(frame, text="[")
    opening_parenthesis4.config(font=("Courier", 20))
    opening_parenthesis5 = Label(frame, text="[")
    opening_parenthesis5.config(font=("Courier", 20))
    opening_parenthesis6 = Label(frame, text="[")
    opening_parenthesis6.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    closing_parenthesis3 = Label(frame, text="]")
    closing_parenthesis3.config(font=("Courier", 20))
    closing_parenthesis4 = Label(frame, text="]")
    closing_parenthesis4.config(font=("Courier", 20))
    closing_parenthesis5 = Label(frame, text="]")
    closing_parenthesis5.config(font=("Courier", 20))
    closing_parenthesis6 = Label(frame, text="]")
    closing_parenthesis6.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    comma3 = Label(frame, text=",")
    comma3.config(font=("Courier", 20))
    comma4 = Label(frame, text=",")
    comma4.config(font=("Courier", 20))
    comma5 = Label(frame, text=",")
    comma5.config(font=("Courier", 20))
    comma6 = Label(frame, text=",")
    comma6.config(font=("Courier", 20))
    comma7 = Label(frame, text=",")
    comma7.config(font=("Courier", 20))
    comma8 = Label(frame, text=",")
    comma8.config(font=("Courier", 20))
    comma9 = Label(frame, text=",")
    comma9.config(font=("Courier", 20))
    comma10 = Label(frame, text=",")
    comma10.config(font=("Courier", 20))
    comma11 = Label(frame, text=",")
    comma11.config(font=("Courier", 20))
    comma12 = Label(frame, text=",")
    comma12.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=7, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light grey", font="Arial 12", width=30, height=10)#background color, size and etc.
    multiply_symbol= Label(frame, text="*")
    multiply_symbol.config(font=("Courier", 20))
    #Location of everything
    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1, column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    comma2.grid(row=1,column=4)
    c.grid(row=1,column=5)
    closing_parenthesis.grid(row=1,column=6)
    multiply_symbol.grid(row=1, column=7)
    opening_parenthesis2.grid(row=1,column=8)
    j.grid(row=1, column=9)
    comma3.grid(row=1,column=10)
    k.grid(row=1,column=11)
    comma4.grid(row=1,column=12)
    l.grid(row=1,column=13)
    closing_parenthesis2.grid(row=1,column=14)
    opening_parenthesis3.grid(row=2,column=0)
    d.grid(row=2, column=1)
    comma5.grid(row=2,column=2)
    e.grid(row=2,column=3)
    comma6.grid(row=2,column=4)
    f.grid(row=2,column=5)
    closing_parenthesis3.grid(row=2,column=6)
    opening_parenthesis4.grid(row=2,column=8)
    m.grid(row=2, column=9)
    comma7.grid(row=2,column=10)
    n.grid(row=2,column=11)
    comma8.grid(row=2,column=12)
    o.grid(row=2,column=13)
    closing_parenthesis4.grid(row=2,column=14)
    opening_parenthesis5.grid(row=3,column=0)
    g.grid(row=3, column=1)
    comma9.grid(row=3,column=2)
    h.grid(row=3,column=3)
    comma10.grid(row=3,column=4)
    i.grid(row=3,column=5)
    closing_parenthesis5.grid(row=3,column=6)
    opening_parenthesis6.grid(row=3,column=8)
    p.grid(row=3, column=9)
    comma11.grid(row=3,column=10)
    q.grid(row=3,column=11)
    comma12.grid(row=3,column=12)
    r.grid(row=3,column=13)
    closing_parenthesis6.grid(row=3,column=14)
    Solve_button.grid(row=1, column=15, padx=(0,0))
    output.grid(row=4, columnspan=14)
    root.mainloop()
#=================================3x3 Add Matrix Calculator=======================
if select_typeof_Calculator=="Add 3*3 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
        x = np.array([[a, b, c],
                      [d, e, f],
                      [g, h, i]])
        y= np.array([[j, k, l],
                     [m, n, o],
                     [p, q, r]])
        text= np.add(x,y)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        e_coefficient = float(e.get())
        f_coefficient = float(f.get())
        g_coefficient = float(g.get())
        h_coefficient = float(h.get())
        i_coefficient = float(i.get())
        j_coefficient = float(j.get())
        k_coefficient = float(k.get())
        l_coefficient = float(l.get())
        m_coefficient = float(m.get())
        n_coefficient = float(n.get())
        o_coefficient = float(o.get())
        p_coefficient = float(p.get())
        q_coefficient = float(q.get())
        r_coefficient = float(r.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient, e_coefficient, f_coefficient, g_coefficient, h_coefficient, i_coefficient, j_coefficient, k_coefficient, l_coefficient, m_coefficient, n_coefficient, o_coefficient, p_coefficient, q_coefficient, r_coefficient))
    root = Tk()
    root.title("3x3-Add Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)
    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=3)
    d.bind("<FocusIn>", clear)
    e = Entry(frame, width=3)
    e.bind("<FocusIn>", clear)
    f = Entry(frame, width=3)
    f.bind("<FocusIn>", clear)
    g = Entry(frame, width=3)
    g.bind("<FocusIn>", clear)
    h = Entry(frame, width=3)
    h.bind("<FocusIn>", clear)
    i = Entry(frame, width=3)
    i.bind("<FocusIn>", clear)
    j = Entry(frame, width=3)
    j.bind("<FocusIn>", clear)
    k = Entry(frame, width=3)
    k.bind("<FocusIn>", clear)
    l = Entry(frame, width=3)
    l.bind("<FocusIn>", clear)
    m = Entry(frame, width=3)
    m.bind("<FocusIn>", clear)
    n = Entry(frame, width=3)
    n.bind("<FocusIn>", clear)
    o = Entry(frame, width=3)
    o.bind("<FocusIn>", clear)
    p = Entry(frame, width=3)
    p.bind("<FocusIn>", clear)
    q = Entry(frame, width=3)
    q.bind("<FocusIn>", clear)
    r = Entry(frame, width=3)
    r.bind("<FocusIn>", clear)
    #Creating labels and buttons
    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    opening_parenthesis3 = Label(frame, text="[")
    opening_parenthesis3.config(font=("Courier", 20))
    opening_parenthesis4 = Label(frame, text="[")
    opening_parenthesis4.config(font=("Courier", 20))
    opening_parenthesis5 = Label(frame, text="[")
    opening_parenthesis5.config(font=("Courier", 20))
    opening_parenthesis6 = Label(frame, text="[")
    opening_parenthesis6.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    closing_parenthesis3 = Label(frame, text="]")
    closing_parenthesis3.config(font=("Courier", 20))
    closing_parenthesis4 = Label(frame, text="]")
    closing_parenthesis4.config(font=("Courier", 20))
    closing_parenthesis5 = Label(frame, text="]")
    closing_parenthesis5.config(font=("Courier", 20))
    closing_parenthesis6 = Label(frame, text="]")
    closing_parenthesis6.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    comma3 = Label(frame, text=",")
    comma3.config(font=("Courier", 20))
    comma4 = Label(frame, text=",")
    comma4.config(font=("Courier", 20))
    comma5 = Label(frame, text=",")
    comma5.config(font=("Courier", 20))
    comma6 = Label(frame, text=",")
    comma6.config(font=("Courier", 20))
    comma7 = Label(frame, text=",")
    comma7.config(font=("Courier", 20))
    comma8 = Label(frame, text=",")
    comma8.config(font=("Courier", 20))
    comma9 = Label(frame, text=",")
    comma9.config(font=("Courier", 20))
    comma10 = Label(frame, text=",")
    comma10.config(font=("Courier", 20))
    comma11 = Label(frame, text=",")
    comma11.config(font=("Courier", 20))
    comma12 = Label(frame, text=",")
    comma12.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=7, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light grey", font="Arial 12", width=30, height=10)#background color, size and etc.
    add_symbol= Label(frame, text="+")
    add_symbol.config(font=("Courier", 20))
    #Location of everything
    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1, column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    comma2.grid(row=1,column=4)
    c.grid(row=1,column=5)
    closing_parenthesis.grid(row=1,column=6)
    add_symbol.grid(row=1, column=7)
    opening_parenthesis2.grid(row=1,column=8)
    j.grid(row=1, column=9)
    comma3.grid(row=1,column=10)
    k.grid(row=1,column=11)
    comma4.grid(row=1,column=12)
    l.grid(row=1,column=13)
    closing_parenthesis2.grid(row=1,column=14)
    opening_parenthesis3.grid(row=2,column=0)
    d.grid(row=2, column=1)
    comma5.grid(row=2,column=2)
    e.grid(row=2,column=3)
    comma6.grid(row=2,column=4)
    f.grid(row=2,column=5)
    closing_parenthesis3.grid(row=2,column=6)
    opening_parenthesis4.grid(row=2,column=8)
    m.grid(row=2, column=9)
    comma7.grid(row=2,column=10)
    n.grid(row=2,column=11)
    comma8.grid(row=2,column=12)
    o.grid(row=2,column=13)
    closing_parenthesis4.grid(row=2,column=14)
    opening_parenthesis5.grid(row=3,column=0)
    g.grid(row=3, column=1)
    comma9.grid(row=3,column=2)
    h.grid(row=3,column=3)
    comma10.grid(row=3,column=4)
    i.grid(row=3,column=5)
    closing_parenthesis5.grid(row=3,column=6)
    opening_parenthesis6.grid(row=3,column=8)
    p.grid(row=3, column=9)
    comma11.grid(row=3,column=10)
    q.grid(row=3,column=11)
    comma12.grid(row=3,column=12)
    r.grid(row=3,column=13)
    closing_parenthesis6.grid(row=3,column=14)
    Solve_button.grid(row=1, column=15, padx=(0,0))
    output.grid(row=4, columnspan=14)
    root.mainloop()


#==================================3x3 Subtract Matrix Calculator===================
if select_typeof_Calculator=="Subtract 3*3 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
        x = np.array([[a, b, c],
                      [d, e, f],
                      [g, h, i]])
        y= np.array([[j, k, l],
                     [m, n, o],
                     [p, q, r]])
        text= np.subtract(x,y)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        e_coefficient = float(e.get())
        f_coefficient = float(f.get())
        g_coefficient = float(g.get())
        h_coefficient = float(h.get())
        i_coefficient = float(i.get())
        j_coefficient = float(j.get())
        k_coefficient = float(k.get())
        l_coefficient = float(l.get())
        m_coefficient = float(m.get())
        n_coefficient = float(n.get())
        o_coefficient = float(o.get())
        p_coefficient = float(p.get())
        q_coefficient = float(q.get())
        r_coefficient = float(r.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient, e_coefficient, f_coefficient, g_coefficient, h_coefficient, i_coefficient, j_coefficient, k_coefficient, l_coefficient, m_coefficient, n_coefficient, o_coefficient, p_coefficient, q_coefficient, r_coefficient))
    root = Tk()
    root.title("3x3-Subtract Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)
    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=3)
    d.bind("<FocusIn>", clear)
    e = Entry(frame, width=3)
    e.bind("<FocusIn>", clear)
    f = Entry(frame, width=3)
    f.bind("<FocusIn>", clear)
    g = Entry(frame, width=3)
    g.bind("<FocusIn>", clear)
    h = Entry(frame, width=3)
    h.bind("<FocusIn>", clear)
    i = Entry(frame, width=3)
    i.bind("<FocusIn>", clear)
    j = Entry(frame, width=3)
    j.bind("<FocusIn>", clear)
    k = Entry(frame, width=3)
    k.bind("<FocusIn>", clear)
    l = Entry(frame, width=3)
    l.bind("<FocusIn>", clear)
    m = Entry(frame, width=3)
    m.bind("<FocusIn>", clear)
    n = Entry(frame, width=3)
    n.bind("<FocusIn>", clear)
    o = Entry(frame, width=3)
    o.bind("<FocusIn>", clear)
    p = Entry(frame, width=3)
    p.bind("<FocusIn>", clear)
    q = Entry(frame, width=3)
    q.bind("<FocusIn>", clear)
    r = Entry(frame, width=3)
    r.bind("<FocusIn>", clear)
    #Creating labels and buttons
    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    opening_parenthesis3 = Label(frame, text="[")
    opening_parenthesis3.config(font=("Courier", 20))
    opening_parenthesis4 = Label(frame, text="[")
    opening_parenthesis4.config(font=("Courier", 20))
    opening_parenthesis5 = Label(frame, text="[")
    opening_parenthesis5.config(font=("Courier", 20))
    opening_parenthesis6 = Label(frame, text="[")
    opening_parenthesis6.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    closing_parenthesis3 = Label(frame, text="]")
    closing_parenthesis3.config(font=("Courier", 20))
    closing_parenthesis4 = Label(frame, text="]")
    closing_parenthesis4.config(font=("Courier", 20))
    closing_parenthesis5 = Label(frame, text="]")
    closing_parenthesis5.config(font=("Courier", 20))
    closing_parenthesis6 = Label(frame, text="]")
    closing_parenthesis6.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    comma3 = Label(frame, text=",")
    comma3.config(font=("Courier", 20))
    comma4 = Label(frame, text=",")
    comma4.config(font=("Courier", 20))
    comma5 = Label(frame, text=",")
    comma5.config(font=("Courier", 20))
    comma6 = Label(frame, text=",")
    comma6.config(font=("Courier", 20))
    comma7 = Label(frame, text=",")
    comma7.config(font=("Courier", 20))
    comma8 = Label(frame, text=",")
    comma8.config(font=("Courier", 20))
    comma9 = Label(frame, text=",")
    comma9.config(font=("Courier", 20))
    comma10 = Label(frame, text=",")
    comma10.config(font=("Courier", 20))
    comma11 = Label(frame, text=",")
    comma11.config(font=("Courier", 20))
    comma12 = Label(frame, text=",")
    comma12.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=7, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light grey", font="Arial 12", width=30, height=10)#background color, size and etc.
    subtract_symbol= Label(frame, text="-")
    subtract_symbol.config(font=("Courier", 20))
    #Location of everything
    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1, column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    comma2.grid(row=1,column=4)
    c.grid(row=1,column=5)
    closing_parenthesis.grid(row=1,column=6)
    subtract_symbol.grid(row=1, column=7)
    opening_parenthesis2.grid(row=1,column=8)
    j.grid(row=1, column=9)
    comma3.grid(row=1,column=10)
    k.grid(row=1,column=11)
    comma4.grid(row=1,column=12)
    l.grid(row=1,column=13)
    closing_parenthesis2.grid(row=1,column=14)
    opening_parenthesis3.grid(row=2,column=0)
    d.grid(row=2, column=1)
    comma5.grid(row=2,column=2)
    e.grid(row=2,column=3)
    comma6.grid(row=2,column=4)
    f.grid(row=2,column=5)
    closing_parenthesis3.grid(row=2,column=6)
    opening_parenthesis4.grid(row=2,column=8)
    m.grid(row=2, column=9)
    comma7.grid(row=2,column=10)
    n.grid(row=2,column=11)
    comma8.grid(row=2,column=12)
    o.grid(row=2,column=13)
    closing_parenthesis4.grid(row=2,column=14)
    opening_parenthesis5.grid(row=3,column=0)
    g.grid(row=3, column=1)
    comma9.grid(row=3,column=2)
    h.grid(row=3,column=3)
    comma10.grid(row=3,column=4)
    i.grid(row=3,column=5)
    closing_parenthesis5.grid(row=3,column=6)
    opening_parenthesis6.grid(row=3,column=8)
    p.grid(row=3, column=9)
    comma11.grid(row=3,column=10)
    q.grid(row=3,column=11)
    comma12.grid(row=3,column=12)
    r.grid(row=3,column=13)
    closing_parenthesis6.grid(row=3,column=14)
    Solve_button.grid(row=1, column=15, padx=(0,0))
    output.grid(row=4, columnspan=14)
    root.mainloop()
#==============================3x3 Discriminant Matrix Calculator==================
if select_typeof_Calculator=="Discriminant 3*3 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d,e,f,g,h,i):
        x = np.array([[a, b, c],
                      [d, e, f],
                      [g, h, i]])
        
        text= x[0][0]*((x[1][1] * x[2][2]) - (x[1][2] * x[2][1]))-x[0][1]*((x[1][0]*x[2][2])-(x[1][2]*x[2][0]))+x[0][2]*((x[1][0]*x[2][1])-(x[1][1]*x[2][0]))
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        e_coefficient = float(e.get())
        f_coefficient = float(f.get())
        g_coefficient = float(g.get())
        h_coefficient = float(h.get())
        i_coefficient = float(i.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient,
                                     d_coefficient, e_coefficient, f_coefficient,
                                     g_coefficient, h_coefficient, i_coefficient))
    root = Tk()
    root.title("3x3-Discriminant Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)
    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=3)
    d.bind("<FocusIn>", clear)
    e = Entry(frame, width=3)
    e.bind("<FocusIn>", clear)
    f = Entry(frame, width=3)
    f.bind("<FocusIn>", clear)
    g = Entry(frame, width=3)
    g.bind("<FocusIn>", clear)
    h = Entry(frame, width=3)
    h.bind("<FocusIn>", clear)
    i = Entry(frame, width=3)
    i.bind("<FocusIn>", clear)

    #Creating labels and buttons
    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    opening_parenthesis3 = Label(frame, text="[")
    opening_parenthesis3.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    closing_parenthesis3 = Label(frame, text="]")
    closing_parenthesis3.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    comma3 = Label(frame, text=",")
    comma3.config(font=("Courier", 20))
    comma4 = Label(frame, text=",")
    comma4.config(font=("Courier", 20))
    comma5 = Label(frame, text=",")
    comma5.config(font=("Courier", 20))
    comma6 = Label(frame, text=",")
    comma6.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=7, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light grey", font="Arial 12", width=30, height=10)#background color, size and etc.
    product_symbol= Label(frame, text=".")
    product_symbol.config(font=("Courier", 20))
    #Location of everything
    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1, column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    comma2.grid(row=1,column=4)
    c.grid(row=1,column=5)
    closing_parenthesis.grid(row=1,column=6)
    opening_parenthesis2.grid(row=2,column=0)
    d.grid(row=2, column=1)
    comma3.grid(row=2,column=2)
    e.grid(row=2,column=3)
    comma4.grid(row=2,column=4)
    f.grid(row=2,column=5)
    closing_parenthesis2.grid(row=2,column=6)
    opening_parenthesis3.grid(row=3,column=0)
    g.grid(row=3, column=1)
    comma5.grid(row=3,column=2)
    h.grid(row=3,column=3)
    comma6.grid(row=3,column=4)
    i.grid(row=3,column=5)
    closing_parenthesis3.grid(row=3,column=6)
    Solve_button.grid(row=1, column=15, padx=(0,0))
    output.grid(row=4, columnspan=14)
    root.mainloop()
#===================================3x3 Product matrices calculator========================================================
if select_typeof_Calculator=="Product 3*3 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
        x = np.array([[a, b, c],
                      [d, e, f],
                      [g, h, i]])
        y= np.array([[j, k, l],
                     [m, n, o],
                     [p, q, r]])
        text= np.product(x,y)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        e_coefficient = float(e.get())
        f_coefficient = float(f.get())

        g_coefficient = float(g.get())
        h_coefficient = float(h.get())
        i_coefficient = float(i.get())
        j_coefficient = float(j.get())
        k_coefficient = float(k.get())
        l_coefficient = float(l.get())
        m_coefficient = float(m.get())
        n_coefficient = float(n.get())
        o_coefficient = float(o.get())
        p_coefficient = float(p.get())
        q_coefficient = float(q.get())
        r_coefficient = float(r.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient, e_coefficient, f_coefficient, g_coefficient, h_coefficient, i_coefficient, j_coefficient, k_coefficient, l_coefficient, m_coefficient, n_coefficient, o_coefficient, p_coefficient, q_coefficient, r_coefficient))
    root = Tk()
    root.title("3x3-product Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)
    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=3)
    d.bind("<FocusIn>", clear)
    e = Entry(frame, width=3)
    e.bind("<FocusIn>", clear)
    f = Entry(frame, width=3)
    f.bind("<FocusIn>", clear)
    g = Entry(frame, width=3)
    g.bind("<FocusIn>", clear)
    h = Entry(frame, width=3)
    h.bind("<FocusIn>", clear)
    i = Entry(frame, width=3)
    i.bind("<FocusIn>", clear)
    j = Entry(frame, width=3)
    j.bind("<FocusIn>", clear)
    k = Entry(frame, width=3)
    k.bind("<FocusIn>", clear)
    l = Entry(frame, width=3)
    l.bind("<FocusIn>", clear)
    m = Entry(frame, width=3)
    m.bind("<FocusIn>", clear)
    n = Entry(frame, width=3)
    n.bind("<FocusIn>", clear)
    o = Entry(frame, width=3)
    o.bind("<FocusIn>", clear)
    p = Entry(frame, width=3)
    p.bind("<FocusIn>", clear)
    q = Entry(frame, width=3)
    q.bind("<FocusIn>", clear)
    r = Entry(frame, width=3)
    r.bind("<FocusIn>", clear)
    #Creating labels and buttons
    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))
    opening_parenthesis3 = Label(frame, text="[")
    opening_parenthesis3.config(font=("Courier", 20))
    opening_parenthesis4 = Label(frame, text="[")
    opening_parenthesis4.config(font=("Courier", 20))
    opening_parenthesis5 = Label(frame, text="[")
    opening_parenthesis5.config(font=("Courier", 20))
    opening_parenthesis6 = Label(frame, text="[")
    opening_parenthesis6.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    closing_parenthesis3 = Label(frame, text="]")
    closing_parenthesis3.config(font=("Courier", 20))
    closing_parenthesis4 = Label(frame, text="]")
    closing_parenthesis4.config(font=("Courier", 20))
    closing_parenthesis5 = Label(frame, text="]")
    closing_parenthesis5.config(font=("Courier", 20))
    closing_parenthesis6 = Label(frame, text="]")
    closing_parenthesis6.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    comma3 = Label(frame, text=",")
    comma3.config(font=("Courier", 20))
    comma4 = Label(frame, text=",")
    comma4.config(font=("Courier", 20))
    comma5 = Label(frame, text=",")
    comma5.config(font=("Courier", 20))
    comma6 = Label(frame, text=",")
    comma6.config(font=("Courier", 20))
    comma7 = Label(frame, text=",")
    comma7.config(font=("Courier", 20))
    comma8 = Label(frame, text=",")
    comma8.config(font=("Courier", 20))
    comma9 = Label(frame, text=",")
    comma9.config(font=("Courier", 20))
    comma10 = Label(frame, text=",")
    comma10.config(font=("Courier", 20))
    comma11 = Label(frame, text=",")
    comma11.config(font=("Courier", 20))
    comma12 = Label(frame, text=",")
    comma12.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=7, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light grey", font="Arial 12", width=30, height=10)#background color, size and etc.
    product_symbol= Label(frame, text=".")
    product_symbol.config(font=("Courier", 20))
    #Location of everything
    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1, column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    comma2.grid(row=1,column=4)
    c.grid(row=1,column=5)
    closing_parenthesis.grid(row=1,column=6)
    product_symbol.grid(row=1, column=7)
    opening_parenthesis2.grid(row=1,column=8)
    j.grid(row=1, column=9)
    comma3.grid(row=1,column=10)
    k.grid(row=1,column=11)
    comma4.grid(row=1,column=12)
    l.grid(row=1,column=13)
    closing_parenthesis2.grid(row=1,column=14)
    opening_parenthesis3.grid(row=2,column=0)
    d.grid(row=2, column=1)
    comma5.grid(row=2,column=2)
    e.grid(row=2,column=3)
    comma6.grid(row=2,column=4)
    f.grid(row=2,column=5)
    closing_parenthesis3.grid(row=2,column=6)
    opening_parenthesis4.grid(row=2,column=8)
    m.grid(row=2, column=9)
    comma7.grid(row=2,column=10)
    n.grid(row=2,column=11)
    comma8.grid(row=2,column=12)
    o.grid(row=2,column=13)
    closing_parenthesis4.grid(row=2,column=14)
    opening_parenthesis5.grid(row=3,column=0)
    g.grid(row=3, column=1)
    comma9.grid(row=3,column=2)
    h.grid(row=3,column=3)
    comma10.grid(row=3,column=4)
    i.grid(row=3,column=5)
    closing_parenthesis5.grid(row=3,column=6)
    opening_parenthesis6.grid(row=3,column=8)
    p.grid(row=3, column=9)
    comma11.grid(row=3,column=10)
    q.grid(row=3,column=11)
    comma12.grid(row=3,column=12)
    r.grid(row=3,column=13)
    closing_parenthesis6.grid(row=3,column=14)
    Solve_button.grid(row=1, column=15, padx=(0,0))
    output.grid(row=4, columnspan=14)
    root.mainloop()
#*****************************************************3x3 Division Matrix Calculator ********************************************************************
if select_typeof_Calculator=="Divide 3*3 Matrix":
    import numpy as np
    from tkinter import *
    def calculator_Function(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
        x = np.array([[a, b, c],
                      [d, e, f],
                      [g, h, i]])
        y= np.array([[j, k, l],
                     [m, n, o],
                     [p, q, r]])
        text= np.division(x,y)
        return text

    def inserter(value):#inserting specified value in widget
        output.delete("0.0","end")
        output.insert("0.0",value)
        
    def clear(event):# Clear the entry form
        caller = event.widget
        caller.delete("0", "end")

    def variable_input_function():#Get the inputted values and plug them into the calculator function to be solved and then displayed in the output section
        a_coefficient = float(a.get())
        b_coefficient = float(b.get())
        c_coefficient = float(c.get())
        d_coefficient = float(d.get())
        e_coefficient = float(e.get())
        f_coefficient = float(f.get())
        g_coefficient = float(g.get())
        h_coefficient = float(h.get())
        i_coefficient = float(i.get())
        j_coefficient = float(j.get())
        k_coefficient = float(k.get())
        l_coefficient = float(l.get())
        m_coefficient = float(m.get())
        n_coefficient = float(n.get())
        o_coefficient = float(o.get())
        p_coefficient = float(p.get())
        q_coefficient = float(q.get())
        r_coefficient = float(r.get())
        inserter(calculator_Function(a_coefficient, b_coefficient, c_coefficient, d_coefficient, e_coefficient, f_coefficient, g_coefficient, h_coefficient, i_coefficient, j_coefficient, k_coefficient, l_coefficient, m_coefficient, n_coefficient, o_coefficient, p_coefficient, q_coefficient, r_coefficient))
    root = Tk()
    root.title("3x3-division Matrix Calculator")
    root.minsize(325,230)


    frame = Frame(root)
    frame.grid()
    # Creating entries
    a = Entry(frame, width=3)
    a.bind("<FocusIn>", clear)
    b = Entry(frame, width=3)
    b.bind("<FocusIn>", clear)
    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    d = Entry(frame, width=3)
    d.bind("<FocusIn>", clear)
    e = Entry(frame, width=3)
    e.bind("<FocusIn>", clear)
    f = Entry(frame, width=3)
    f.bind("<FocusIn>", clear)
    g = Entry(frame, width=3)
    g.bind("<FocusIn>", clear)
    h = Entry(frame, width=3)
    h.bind("<FocusIn>", clear)
    i = Entry(frame, width=3)
    i.bind("<FocusIn>", clear)
    j = Entry(frame, width=3)
    j.bind("<FocusIn>", clear)
    k = Entry(frame, width=3)
    k.bind("<FocusIn>", clear)
    l = Entry(frame, width=3)
    l.bind("<FocusIn>", clear)
    m = Entry(frame, width=3)
    m.bind("<FocusIn>", clear)
    n = Entry(frame, width=3)
    n.bind("<FocusIn>", clear)
    o = Entry(frame, width=3)
    o.bind("<FocusIn>", clear)
    p = Entry(frame, width=3)
    p.bind("<FocusIn>", clear)
    q = Entry(frame, width=3)
    q.bind("<FocusIn>", clear)
    r = Entry(frame, width=3)
    r.bind("<FocusIn>", clear)
    #Creating labels and buttons
    opening_parenthesis = Label(frame, text="[")
    opening_parenthesis.config(font=("Courier", 20))
    opening_parenthesis2 = Label(frame, text="[")
    opening_parenthesis2.config(font=("Courier", 20))

    opening_parenthesis3 = Label(frame, text="[")
    opening_parenthesis3.config(font=("Courier", 20))
    opening_parenthesis4 = Label(frame, text="[")
    opening_parenthesis4.config(font=("Courier", 20))
    opening_parenthesis5 = Label(frame, text="[")
    opening_parenthesis5.config(font=("Courier", 20))
    opening_parenthesis6 = Label(frame, text="[")
    opening_parenthesis6.config(font=("Courier", 20))
    closing_parenthesis = Label(frame, text="]")
    closing_parenthesis.config(font=("Courier", 20))
    closing_parenthesis2 = Label(frame, text="]")
    closing_parenthesis2.config(font=("Courier", 20))
    closing_parenthesis3 = Label(frame, text="]")
    closing_parenthesis3.config(font=("Courier", 20))
    closing_parenthesis4 = Label(frame, text="]")
    closing_parenthesis4.config(font=("Courier", 20))
    closing_parenthesis5 = Label(frame, text="]")
    closing_parenthesis5.config(font=("Courier", 20))
    closing_parenthesis6 = Label(frame, text="]")
    closing_parenthesis6.config(font=("Courier", 20))
    comma = Label(frame, text=",")
    comma.config(font=("Courier", 20))
    comma2 = Label(frame, text=",")
    comma2.config(font=("Courier", 20))
    comma3 = Label(frame, text=",")
    comma3.config(font=("Courier", 20))
    comma4 = Label(frame, text=",")
    comma4.config(font=("Courier", 20))
    comma5 = Label(frame, text=",")
    comma5.config(font=("Courier", 20))
    comma6 = Label(frame, text=",")
    comma6.config(font=("Courier", 20))
    comma7 = Label(frame, text=",")
    comma7.config(font=("Courier", 20))
    comma8 = Label(frame, text=",")
    comma8.config(font=("Courier", 20))
    comma9 = Label(frame, text=",")
    comma9.config(font=("Courier", 20))
    comma10 = Label(frame, text=",")
    comma10.config(font=("Courier", 20))
    comma11 = Label(frame, text=",")
    comma11.config(font=("Courier", 20))
    comma12 = Label(frame, text=",")
    comma12.config(font=("Courier", 20))
    Solve_button = Button(frame, text="Solve", width=7, height=2, command=variable_input_function)#Solve button
    output = Text(frame, bg="light grey", font="Arial 12", width=30, height=10)#background color, size and etc.
    division_symbol= Label(frame, text="/")
    division_symbol.config(font=("Courier", 20))
    #Location of everything
    opening_parenthesis.grid(row=1,column=0)
    a.grid(row=1, column=1)
    comma.grid(row=1,column=2)
    b.grid(row=1,column=3)
    comma2.grid(row=1,column=4)
    c.grid(row=1,column=5)
    closing_parenthesis.grid(row=1,column=6)
    division_symbol.grid(row=1, column=7)
    opening_parenthesis2.grid(row=1,column=8)
    j.grid(row=1, column=9)
    comma3.grid(row=1,column=10)
    k.grid(row=1,column=11)
    comma4.grid(row=1,column=12)
    l.grid(row=1,column=13)
    closing_parenthesis2.grid(row=1,column=14)
    opening_parenthesis3.grid(row=2,column=0)
    d.grid(row=2, column=1)
    comma5.grid(row=2,column=2)
    e.grid(row=2,column=3)
    comma6.grid(row=2,column=4)
    f.grid(row=2,column=5)
    closing_parenthesis3.grid(row=2,column=6)
    opening_parenthesis4.grid(row=2,column=8)
    m.grid(row=2, column=9)
    comma7.grid(row=2,column=10)
    n.grid(row=2,column=11)
    comma8.grid(row=2,column=12)
    o.grid(row=2,column=13)
    closing_parenthesis4.grid(row=2,column=14)
    opening_parenthesis5.grid(row=3,column=0)
    g.grid(row=3, column=1)
    comma9.grid(row=3,column=2)
    h.grid(row=3,column=3)
    comma10.grid(row=3,column=4)
    i.grid(row=3,column=5)
    closing_parenthesis5.grid(row=3,column=6)
    opening_parenthesis6.grid(row=3,column=8)
    p.grid(row=3, column=9)
    comma11.grid(row=3,column=10)
    q.grid(row=3,column=11)
    comma12.grid(row=3,column=12)
    r.grid(row=3,column=13)
    closing_parenthesis6.grid(row=3,column=14)
    Solve_button.grid(row=1, column=15, padx=(0,0))
    output.grid(row=4, columnspan=14)
    root.mainloop()


