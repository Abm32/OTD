from tkinter import *  
import pandas as pd

base = Tk()  
base.geometry("500x500")  
base.title("One Touch Diagonizer")  

data = pd.read_csv("bwd.csv")

name = []
ages = []
gend = []
sleepd = []
fh = []
exe = []
smok = []
alco = []
diab = []
par = []
gran = []
for (a,b,c,d,e,f,g,h,i,j,k) in zip(data.Age,data.gender,data.sleepdur,data.Foodhabit,data.exercise,data.smoker,data.alcohol,data.diabetic,data.Dopshd,data.Dogshd,data.NAME):
    ages.append(a)
    if b == "male":
        gend.append(1)
    elif b == "Female":
        gend.append(0.7)
    else :
        gend.append(0)
    if c == "less than 6 hours":
        sleepd.append(2)
    elif c == "6 hours":
        sleepd.append(0)
    else:
        sleepd.append(0)
    if d == "Healthy food":
        fh.append(-1)
    elif d == "Junk food":
        fh.append(5)
    else:
        fh.append(2)
    if e == "sometimes":
        exe.append(-1)
    elif e == "daily":
        exe.append(-3)
    else:
        exe.append(1)
    if f == "yes":
        smok.append(5)
    elif f == "no":
        smok.append(0)
    else:
        smok.append(3)
    if g == "yes":
        alco.append(5)
    elif g == "no":
        alco.append(0)
    else:
        alco.append(3)
    if h == "yes":
        diab.append(5)
    else:
        diab.append(0)
    if i == "yes":
        par.append(3)
    else:
        par.append(0)
    if j == "yes":
        gran.append(3)
    else:
        gran.append(0)
    name.append(k)

sumli = []
divv = []
for n in range(0,100):
        summ = float(gend[n]) + float(sleepd[n]) + float(fh[n]) + float(exe[n]) + float(smok[n]) + float(alco[n])+ float(diab[n]) + float(par[n]) + float(gran[n])
        sumli.append(summ)

for m in sumli:
    if float(m) < float(1):
        sumli.remove(m)
        sumli.append(1)

for k in range(0,100):
    agec = float(ages[k]) / float(sumli[k])
    itt = str(agec)
    new = itt[0:4]
    divv.append(new)
#print(divv)
divid = []
for l in range(0,100):
    aa = float(divv[l]) * 100
    aaaa = str(aa)
    divid.append(aaaa)

divid1 = []
for l in divid:
    add = l[0:2]
    divid1.append(add)

print(divid1)
#name ages gend sleepd fh exe smok alco diab par gran 


def LoginPage():
    def mnn():
        alp = svv.get()
        for a in name:
            if str(alp) == str(a):
                index1 = name.index(str(alp))
                divvv = str(divid1[index1]) + " %"
                print(divvv)
                Label(base, text=divvv).pack()
                #msg = Message(base, text = str(divvv)+"chance")  
                #msg.pack() 
    base.title("Sign In")
    #msg = Message(base, text = divvv)  
    #msg.pack()  
    #base.geometry("300x250")
    Label(base, text="Please enter your name").pack()
    Label(base, text="").pack()
    Label(base, text="Username").pack()
    svv = StringVar()
    #entry_1 = Entry(base, textvariable=sv, validatecommand=mmm)  
    username_login_entry = Entry(base, textvariable=svv, validatecommand=mnn)
    username_login_entry.pack()
    Label(base, text="").pack()
    Label(base, text="").pack()
    #aggg = svv.get()
    butt = Button(base, text="Login", width=10, height=1, command=neww)
    close = Button(base, text="Close", width=10, height=1, command=base.destroy)
    butt.pack()
    close.pack()
    base.mainloop()


def neww():
    def mmm():
        #entry_1.get()

        sum = float(vars.get()) + float(vars1.get()) + float(vars2.get()) + float(vars3.get()) + float(vars4.get()) + float(vars5.get()) + float(vars6.get()) + float(vars7.get()) #sum of all factor
        agg = sv.get() #age
        divv = float(agg) / float(sum)
        per = divv * 100 # in percentage
        print(str(int(per)) + " %")
        #c=float(0.1) + float(vars.get())
        #print(float(c))
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
    

LoginPage()

