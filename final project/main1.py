from tkinter import *  
base = Tk()  
base.geometry("700x700")  
base.title("registration form")  




def mmm():
    #entry_1.get()
    sum = float(vars.get()) + float(vars1.get()) + float(vars2.get()) + float(vars3.get()) + float(vars4.get()) + float(vars5.get()) + float(vars6.get()) + float(vars7.get()) #sum of all factor
    agg = sv.get() #age
    divv = float(agg) / float(sum)
    pe = divv * 100 # in percentage
    per = pe / 10
    print(str(int(per)) + " %")
    #c=float(0.1) + float(vars.get())
    #print(float(c))
    lalb9 = Label(base, text=(str(int(per)) + " %"), width=15,font=("arial",12)) 
    lalb9.place(x=0, y=440)
    a = 0
    if int(per) > 85 :
        a = """Stop smoking / Alcohol /n
        Follow a proper diet"""
    elif 75 < int(per) < 85 :
        a = """medium"""
    else:
        a = """low chance"""

    labl10 = Label(base, text=(str(a)), width=35,font=("arial",12)) 
    labl10.place(x=180, y=550)


labl_1 = Label(base, text="Age",width=15,font=("arial", 12))  
labl_1.place(x=5,y=80)  
sv = StringVar()
entry_1 = Entry(base, textvariable=sv, validatecommand=mmm)  
entry_1.place(x=190,y=80)  

lb1= Label(base, text="Sleeping duration", width=15, font=("arial",12))  
lb1.place(x=5, y=120)  
vars1 = IntVar()  
Radiobutton(base, text="6 hours", padx=5,variable=vars1, value=2).place(x=180, y=120)  
Radiobutton(base, text="less than 6 hours", padx =10,variable=vars1, value=0).place(x=240,y=120) 

  
lb3= Label(base, text="Food habit", width=15, font=("arial",12))  
lb3.place(x=5, y=160)  
vars2 = IntVar()
Radiobutton(base, text="Junk ", padx=5,variable=vars2, value=5).place(x=180, y=160)
Radiobutton(base, text="Healthy ", padx=10,variable=vars2, value=-1).place(x=240, y=160)
Radiobutton(base, text="Both", padx=10,variable=vars2, value=2).place(x=335, y=160)
  
lb4= Label(base, text="Exercise", width=15,font=("arial",12))  
lb4.place(x=5, y=200)  
vars3 = IntVar()
Radiobutton(base, text="Daily", padx=5,variable=vars3, value=-3).place(x=180, y=200)
Radiobutton(base, text="Sometimes", padx=10,variable=vars3, value=-1).place(x=240, y=200)
Radiobutton(base, text="Never", padx=10,variable=vars3, value=1).place(x=335, y=200)
  
lb5= Label(base, text="Select Gender", width=15, font=("arial",12))  
lb5.place(x=5, y=240)  
vars = IntVar()  
Radiobutton(base, text="Male", padx=5,variable=vars, value=float(1)).place(x=180, y=240)  
Radiobutton(base, text="Female", padx =10,variable=vars, value=float(0.7)).place(x=240,y=240) 
Radiobutton(base, text="Others", padx =10,variable=vars, value=float(0)).place(x=335,y=240) 
  
#list_of_cntry = ("United States", "India", "Nepal", "Germany")  
#cv = StringVar()  
#drplist= OptionMenu(base, cv, *list_of_cntry)  
#drplist.config(width=15)  
#cv.set("United States")  
lb2= Label(base, text="Smoker?", width=15,font=("arial",12))  
lb2.place(x=5,y=280)  
vars4 = IntVar()  
Radiobutton(base, text="Yes", padx=5,variable=vars4, value=5).place(x=180, y=280)  
Radiobutton(base, text="No", padx =10,variable=vars4, value=0).place(x=240,y=280) 
Radiobutton(base, text="Often", padx =10,variable=vars4, value=3).place(x=335,y=280) 
#drplist.place(x=200, y=275)  
  
lb6= Label(base, text="Alcohol", width=15,font=("arial",12))  
lb6.place(x=5, y=320)  
vars5 = IntVar()  
Radiobutton(base, text="Yes", padx=5,variable=vars5, value=5).place(x=180, y=320)  
Radiobutton(base, text="No", padx =10,variable=vars5, value=0).place(x=240,y=320) 
Radiobutton(base, text="Often", padx =10,variable=vars5, value=3).place(x=335,y=320)
  
lb7= Label(base, text="Diabetic", width=15,font=("arial",12))  
lb7.place(x=5, y=360)  
vars6 = IntVar()  
Radiobutton(base, text="Yes", padx=5,variable=vars6, value=5).place(x=180, y=360)  
Radiobutton(base, text="No", padx =10,variable=vars6, value=0).place(x=240,y=360) 

lb8= Label(base, text="Parentic heart disease", width=15,font=("arial",12))  
lb8.place(x=0, y=400)  
vars7 = IntVar()  
Radiobutton(base, text="Yes", padx=5,variable=vars7, value=3).place(x=180, y=400)  
Radiobutton(base, text="No", padx =10,variable=vars7, value=0).place(x=240,y=400) 


Button(base, text="Calculate", width=10, command=mmm).place(x=200,y=440)  
base.mainloop()

#send = "You -> " + e.get()
#txt.insert(END, "\n" + send)
#send = Button(r, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).grid(row=2, column=1)
#txt = Text(r, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
#txt.grid(row=1, column=0, columnspan=2)
