from tkinter import *
from tkinter import messagebox as mbox
from tkinter import simpledialog,ttk
import mysql.connector as sq
import datetime as datym
import os
import random
import pyttsx3
global con,cur

schoolcode='_123THeZxen2o2*L!bR4rY.-!'
con=sq.connect(host='localhost',user='root',passwd='123')
cur=con.cursor()
cur.execute('create database if not exists LibraryManagement')
cur.execute('use LibraryManagement')
cur.execute('create table if not exists bookdetail(bookid varchar(6) ,Name varchar(30),quantity int,avilableqty int,Author varchar(25),doa varchar(50))')#set the primary keys
cur.execute('create table if not exists issuedbooks(adno int, Name varchar(50),Class varchar(50),bookid varchar(10),bookname varchar(50), D_O_I varchar(30),Due_Date varchar(50),D_O_S varchar(50))')
cur.execute('create table if not exists studetail(Adno int(6) ,Name varchar(30),dob date,Class varchar(3),Username varchar(20),Password varchar(20),fine int)')   #set the primary keys
cur.execute('create table if not exists adetail(Id int(4) ,Name varchar(30),datymofjoin varchar(30),Username varchar(20),Password varchar(20))')
con.commit()
#------------------------speak fn-------------------------------------
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
#--------------------------------------------VIEW HISTORY ---------------------------------------

def searchh():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    p=s1.get()
    if p!='':
        try:
            search2.delete(0,END)
            sql1=f'select * from issuedbooks where adno ="{p}"'
            cur.execute(sql1)
            r=cur.fetchall()
            total=len(r)
            labl.configure(text=total)
            for i in tree.get_children():
                tree.delete(i)
            for i in r:
                tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
            con.close()
        except:
            mbox.showinfo('ALERT!','Unable to search book.')


def delete_infoh(*event):
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    if tree.focus():
        c=tree.focus()
        f=tree.item(c)
        f=f['values']
        p1=str(f[0])
        p2 = str(f[3])
        s = f'delete from issuedbooks where adno = "{p1}" and bookid ="{p2}"'
        cur.execute(s)
        con.commit()
        for i in tree.get_children():
            tree.delete(i)
        cur.execute('select * from issuedbooks')
        r=cur.fetchall()
        total=len(r)
        labl.configure(text=total)
        for i in r:
            tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
        
def reh():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    cur.execute('select * from issuedbooks')
    r=cur.fetchall()
    total=len(r)
    labl.configure(text=total)
    for i in tree.get_children():
        tree.delete(i)
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
def viewbook_backh():
     viewform.destroy()
     admin_page()
     
def history():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    global labl,s1,search2,tree,viewform
    try:
        root6.destroy()
    except:  
        pass
    viewform=Tk()
    #------------------------------treeview styling------------------------------------------
    style = ttk.Style(viewform)

    style.theme_use("clam")
    style.configure("Treeview", background="black", fieldbackground="#D1A684", foreground="black")
    #-----------------------------------------------------------
    
    viewform.geometry('1200x650')
    viewform.title('BOOK HISTORY')
    s1=StringVar()
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=300,bg='#FE858D')
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    text = Label(TopViewForm, text="History", bg='#37CBBE',fg='white',font=('times', 18,'italic'), width=600)
    text.pack(fill=X)
    txtsearch = Label(LeftViewForm, text="BOOK ID",bg='#FE858D',fg='white',font=('times', 20,'bold','italic')).place(x=70,y=50)
    search2 = Entry(LeftViewForm, font=(15),bd=3,textvariable=s1 ,width=20)
    search2.place(x=50,y=100)
    photo = PhotoImage(file = "search.png")
    search = Button(LeftViewForm,image=photo,bd=0,bg='#FE858D',height=40,width=100,command=searchh).place(x=70,y=150)
    photo3 = PhotoImage(file = "delete.png")
    delete = Button(LeftViewForm,image=photo3,bd=0,bg='#FE858D',height=40,width=100,command=delete_infoh).place(x=70,y=310)
    photo4 = PhotoImage(file = "refresh.png")
    delete = Button(LeftViewForm,image=photo4,bd=0,bg='#FE858D',height=40,width=100,command=reh).place(x=60,y=390)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=('1','2','3','4','5','6','7','8'), height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree['columns']=('1','2','3','4','5','6','7','8')
    tree['show']='headings'
    tree.heading('1',text='Admission Number')
    tree.heading('2',text='Name')
    tree.heading('3',text='Class')
    tree.heading('4',text='BookId')
    tree.heading('5',text='Book Name')
    tree.heading('6',text='D.O.I')
    tree.heading('7',text='Due Date')
    tree.heading('8',text='D.O.S')
    tree.column('8',width=280,anchor='center')
    tree.column('7',width=280,anchor='center')
    tree.column('6',width=280,anchor='center')
    tree.column('5',width=280,anchor='center')
    tree.column('4',width=280,anchor='center')
    tree.column('3',width=240,anchor='center')
    tree.column('2',width=240,anchor='center')
    tree.column('1',width=170,anchor='center')
    tree.pack()
    cur.execute('select * from issuedbooks')
    r=cur.fetchall()
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    total=len(r)
    photo44 = PhotoImage(file = "back1.png")
    search = Button(LeftViewForm,image=photo44,height=40,width=70,bg='#FE858D',bd=0,command=viewbook_backh).place(x=80,y=460)
    Label(viewform,text='TOTAL RESULTS FOUND : ',bg='#FE858D',fg='white',font=('times',14,'italic')).place(x=40,y=575)
    labl=Label(viewform,text=total,bg='#FE858D',fg='white',font=('times',20,'bold'))
    labl.place(x=140,y=600)
    viewform.mainloop()

#------------------------------------------- VIEW ISSUED BOOKS--------------------------
def searchts():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    p=s1.get()
    if p!='':
        try:
            search2.delete(0,END)
            sql1=f'select * from issuedbooks where adno ="{p}" and D_O_S = ""'
            cur.execute(sql1)
            r=cur.fetchall()
            total=len(r)
            labl.configure(text=total)
            for i in tree.get_children():
                tree.delete(i)
            for i in r:
                tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
            con.close()
        except:
            mbox.showinfo('ALERT!','Unable to search book.')


def submit_infots(*event):
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    if tree.focus():
        c=tree.focus()
        f=tree.item(c)
        f=f['values']
        p1=str(f[0])
        p2 = str(f[3])
        today = datym.date.today()
        today_str = today.strftime("%Y-%m-%d")
        s=[f'update issuedbooks set D_O_S = "{today_str}" where adno="{p1}" and bookid="{p2}"',f"update bookdetail set avilableqty=avilableqty+1 where bookid='{p2}'"]
        for j in s:
            cur.execute(j)
            con.commit()
        s = f'select Due_date from issuedbooks where adno="{p1}" and bookid="{p2}"'
        cur.execute(s)
        duedate = cur.fetchone()[0]
        fduedate = datym.date.fromisoformat(duedate)
        day = (today - fduedate).days
        if day > 0:
            mbox.showinfo('FINE ',f"Total Fine amount to be paid Rs.{day*10}")
            s = f'update studetail set fine = fine + {day * 10} where Adno="{p1}"'
            cur.execute(a)
            con.commit()
        try:
            for i in tree.get_children():
                tree.delete(i)
            cur.execute('select * from issuedbooks where D_O_S = ""')
            r=cur.fetchall()
            total=len(r)
            labl.configure(text=total)
            for i in r:
                tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
        
        except:
            pass
def rets():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    cur.execute('select * from issuedbooks where D_O_S = ""')
    r=cur.fetchall()
    total=len(r)
    labl.configure(text=total)
    for i in tree.get_children():
        tree.delete(i)
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
def viewbook_backts():
     viewform.destroy()
     admin_page()
     
def to_submit():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    global labl,s1,search2,tree,viewform
    try:
        root6.destroy()
    except:  
        pass
    viewform=Tk()
    #--------------------------
    style = ttk.Style(viewform)

    style.theme_use("clam")
    style.configure("Treeview", background="black", fieldbackground="#D1A684", foreground="black")
    #---------------------
    
    viewform.geometry('1200x650')
    viewform.title('TO SUBMIT DETAILS')
    s1=StringVar()
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=300,bg='#FE858D')
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    text = Label(TopViewForm, text="Submission Details", bg='#37CBBE',fg='white',font=('times', 18,'italic'), width=600)
    text.pack(fill=X)
    txtsearch = Label(LeftViewForm, text="BOOK ID",bg='#FE858D',fg='white',font=('times', 20,'bold','italic')).place(x=70,y=50)
    search2 = Entry(LeftViewForm, font=(15),bd=3,textvariable=s1 ,width=20)
    search2.place(x=50,y=100)
    photo = PhotoImage(file = "search.png")
    search = Button(LeftViewForm,image=photo,bd=0,bg='#FE858D',height=40,width=100,command=searchts).place(x=70,y=150)
    photo3 = PhotoImage(file = "sub2.png")
    delete = Button(LeftViewForm,image=photo3,bd=0,bg='#FE858D',height=40,width=100,command=submit_infots).place(x=70,y=310)
    photo4 = PhotoImage(file = "refresh.png")
    delete = Button(LeftViewForm,image=photo4,bd=0,bg='#FE858D',height=40,width=100,command=rets).place(x=60,y=390)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=('1','2','3','4','5','6','7','8'), height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree['columns']=('1','2','3','4','5','6','7','8')
    tree['show']='headings'
    tree.heading('1',text='Admission Number')
    tree.heading('2',text='Name')
    tree.heading('3',text='Class')
    tree.heading('4',text='BookId')
    tree.heading('5',text='Book Name')
    tree.heading('6',text='D.O.I')
    tree.heading('7',text='Due Date')
    tree.heading('8',text='D.O.S')
    tree.column('8',width=280,anchor='center')
    tree.column('7',width=280,anchor='center')
    tree.column('6',width=280,anchor='center')
    tree.column('5',width=280,anchor='center')
    tree.column('4',width=280,anchor='center')
    tree.column('3',width=240,anchor='center')
    tree.column('2',width=240,anchor='center')
    tree.column('1',width=170,anchor='center')
    tree.pack()
    cur.execute('select * from issuedbooks where D_O_S = ""')
    r=cur.fetchall()
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    total=len(r)
    photo44 = PhotoImage(file = "back1.png")
    search = Button(LeftViewForm,image=photo44,height=40,width=70,bg='#FE858D',bd=0,command=viewbook_backts).place(x=80,y=460)
    Label(viewform,text='TOTAL RESULTS FOUND : ',bg='#FE858D',fg='white',font=('times',14,'italic')).place(x=40,y=575)
    labl=Label(viewform,text=total,bg='#FE858D',fg='white',font=('times',20,'bold'))
    labl.place(x=140,y=600)
    viewform.mainloop()

#--------------------------------------------------------------------
def search111():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    p=s1.get()
    if p!='':
        try:
            search2.delete(0,END)
            sql1=f'select * from studetail where Adno ="{p}"'
            cur.execute(sql1)
            r=cur.fetchall()
            total=len(r)
            labl.configure(text=total)
            for i in tree.get_children():
                tree.delete(i)
            for i in r:
                tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
            con.close()
        except:
            mbox.showinfo('ALERT!','Unable to search book.')


def delete_info11(*event):
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    speak('Are you sure?')
    if mbox.askquestion("Confirm Resubmission", "Are you sure?")=='yes':
        if tree.focus():
            c=tree.focus()
            f=tree.item(c)
            f=f['values']
            p1=str(f[0])
            s=f'delete from studetail where Adno ="{p1}"'
            cur.execute(s)
            con.commit()
            for i in tree.get_children():
                tree.delete(i)
            cur.execute('select * from studetail')
            r=cur.fetchall()
            total=len(r)
            labl.configure(text=total)
            for i in r:
                tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
    else:
        pass
def re11():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    cur.execute('select * from studetail')
    r=cur.fetchall()
    total=len(r)
    labl.configure(text=total)
    for i in tree.get_children():
        tree.delete(i)
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
def viewbook_back1():
     viewform.destroy()
     admin_page()

def pay_fine():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    if tree.focus():
        c=tree.focus()
        f=tree.item(c)
        f=f['values']
        p1=str(f[0])
        s=f'update studetail set fine = 0 where adno = "{p1}"'
        cur.execute(s)
        con.commit()
        for i in tree.get_children():
            tree.delete(i)
        cur.execute('select * from studetail')
        r=cur.fetchall()
        total=len(r)
        labl.configure(text=total)
        for i in r:
            tree.insert("",'end',values=(i[0],i[1],i[2],i[3]))
    
def student_details():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    global labl,s1,search2,tree,viewform
    try:
        root6.destroy()
    except:  
        pass
    viewform=Tk()
    #--------------------
    style = ttk.Style(viewform)

    style.theme_use("clam")
    style.configure("Treeview", background="black", fieldbackground="#D1A684", foreground="black")
    #-----------------
    
    viewform.geometry('1200x650')
    viewform.title('STUDENT DETAILS')
    s1=StringVar()
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=300,bg='#FE858D')
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    text = Label(TopViewForm, text="Student Details", bg='#37CBBE',fg='white',font=('times', 18,'italic'), width=600)
    text.pack(fill=X)
    txtsearch = Label(LeftViewForm, text="BOOK ID",bg='#FE858D',fg='white',font=('times', 20,'bold','italic')).place(x=70,y=50)
    search2 = Entry(LeftViewForm, font=(15),bd=3,textvariable=s1 ,width=20)
    search2.place(x=50,y=100)
    photo = PhotoImage(file = "search.png")
    search = Button(LeftViewForm,image=photo,bd=0,bg='#FE858D',height=40,width=100,command=search111).place(x=70,y=150)
    photo3 = PhotoImage(file = "delete.png")
    delete = Button(LeftViewForm,image=photo3,bd=0,bg='#FE858D',height=40,width=100,command=delete_info11).place(x=70,y=290)
    delpic=PhotoImage(file = "payfyn.png")
    delete = Button(LeftViewForm,image=delpic,bd=0,bg='#FE858D',height=40,width=100,command=pay_fine).place(x=70,y=350)
    photo4 = PhotoImage(file = "refresh.png")
    delete = Button(LeftViewForm,image=photo4,bd=0,bg='#FE858D',height=40,width=100,command=re11).place(x=70,y=410)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=('1','2','3','4','5'), height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree['columns']=('1','2','3','4','5')
    tree['show']='headings'
    tree.heading('1',text='Admission Number')
    tree.heading('2',text='Name')
    tree.heading('3',text='D.O.B')
    tree.heading('4',text='Class')
    tree.heading('5',text='Fine')
    tree.column('4',width=280,anchor='center')
    tree.column('3',width=240,anchor='center')
    tree.column('2',width=240,anchor='center')
    tree.column('1',width=170,anchor='center')
    tree.column('5',width=170,anchor='center')
    tree.pack()
    cur.execute('select * from studetail')
    r=cur.fetchall()
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[6]))
    total=len(r)
    photo44 = PhotoImage(file = "back1.png")
    search = Button(LeftViewForm,image=photo44,height=40,width=70,bg='#FE858D',bd=0,command=viewbook_back1).place(x=80,y=470)
    Label(viewform,text='TOTAL RESULTS FOUND : ',bg='#FE858D',fg='white',font=('times',14,'italic')).place(x=40,y=575)
    labl=Label(viewform,text=total,bg='#FE858D',fg='white',font=('times',20,'bold'))
    labl.place(x=140,y=600)
    viewform.mainloop()
##--------------------------------------------------------

#------------------------#admin login --------------------------------#
def search11():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    p=s1.get()
    if p!='':
        try:
            search2.delete(0,END)
            sql1=f'select * from bookdetail where bookid ="{p}"'
            cur.execute(sql1)
            r=cur.fetchall()
            total=len(r)
            labl.configure(text=total)
            for i in tree.get_children():
                tree.delete(i)
            for i in r:
                tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5]))
            con.close()
        except:
            mbox.showinfo('ALERT!','Unable to search book.')


def delete_info1(*event):
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    if tree.focus():
        c=tree.focus()
        f=tree.item(c)
        f=f['values']
        p1=str(f[0])
        s=f'delete from bookdetail where bookid ="{p1}"'
        cur.execute(s)
        con.commit()
        for i in tree.get_children():
            tree.delete(i)
        cur.execute('select * from bookdetail')
        r=cur.fetchall()
        total=len(r)
        labl.configure(text=total)
        for i in r:
            tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        
def re1():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    cur.execute('select * from bookdetail')
    r=cur.fetchall()
    total=len(r)
    labl.configure(text=total)
    for i in tree.get_children():
        tree.delete(i)
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5]))
def viewbook_back():
     viewform1.destroy()
     admin_page()
def view_book():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    global labl,s1,search2,tree,viewform1
    try:
        root6.destroy()
    except:
        pass
    viewform1=Tk()
    #-----
    style = ttk.Style(viewform1)

    style.theme_use("clam")
    style.configure("Treeview", background="black", fieldbackground="#D1A684", foreground="black")
    #-----
    
    viewform1.geometry('1200x650')
    viewform1.title('VIEW BOOK')
    s1=StringVar()
    Topviewform1 = Frame(viewform1, width=600, bd=1, relief=SOLID)
    Topviewform1.pack(side=TOP, fill=X)
    Leftviewform1 = Frame(viewform1, width=300,bg='#FE858D')
    Leftviewform1.pack(side=LEFT, fill=Y)
    Midviewform1 = Frame(viewform1, width=600)
    Midviewform1.pack(side=RIGHT)
    text = Label(Topviewform1, text="Book Details", bg='#37CBBE',fg='white',font=('times', 18,'italic'), width=600)
    text.pack(fill=X)
    txtsearch = Label(Leftviewform1, text="BOOK ID",bg='#FE858D',fg='white',font=('times', 20,'bold','italic')).place(x=70,y=50)
    search2 = Entry(Leftviewform1, font=(15),bd=3,textvariable=s1 ,width=20)
    search2.place(x=50,y=100)
    photo = PhotoImage(file = "search.png")
    search = Button(Leftviewform1,image=photo,bd=0,bg='#FE858D',height=40,width=100,command=search11).place(x=70,y=150)
    photo3 = PhotoImage(file = "delete.png")
    delete = Button(Leftviewform1,image=photo3,bd=0,bg='#FE858D',height=40,width=100,command=delete_info1).place(x=70,y=310)
    photo4 = PhotoImage(file = "refresh.png")
    delete = Button(Leftviewform1,image=photo4,bd=0,bg='#FE858D',height=40,width=100,command=re1).place(x=60,y=390)
    scrollbarx = Scrollbar(Midviewform1, orient=HORIZONTAL)
    scrollbary = Scrollbar(Midviewform1, orient=VERTICAL)
    tree = ttk.Treeview(Midviewform1, columns=('1','2','3','4','5','6'), height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree['columns']=('1','2','3','4','5','6')
    tree['show']='headings'
    tree.heading('1',text='Book Id')
    tree.heading('2',text='Book Name')
    tree.heading('3',text='Supplied Quantity')
    tree.heading('4',text='Avilable Quantity')
    tree.heading('5',text='Author')
    tree.heading('6',text='D.O.A')
    tree.column('6',width=280,anchor='center')
    tree.column('5',width=280,anchor='center')
    tree.column('4',width=280,anchor='center')
    tree.column('3',width=240,anchor='center')
    tree.column('2',width=240,anchor='center')
    tree.column('1',width=170,anchor='center')
    tree.pack()
    cur.execute('select * from bookdetail')
    r=cur.fetchall()
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5]))
    total=len(r)
    photo44 = PhotoImage(file = "back1.png")
    search = Button(Leftviewform1,image=photo44,height=40,width=70,bg='#FE858D',bd=0,command=viewbook_back).place(x=80,y=460)
    Label(viewform1,text='TOTAL RESULTS FOUND : ',bg='#FE858D',fg='white',font=('times',14,'italic')).place(x=40,y=575)
    labl=Label(viewform1,text=total,bg='#FE858D',fg='white',font=('times',20,'bold'))
    labl.place(x=140,y=600)
    viewform1.mainloop()

def submitbook():
     try:
          st = f"insert into bookdetail values('{bookid.get()}','{bookname.get()}',{bookqty.get()},{bookqty.get()},'{bookdealer.get()}','{datym.date.today()}')"
          cur.execute(st)
          con.commit()
          mbox.showinfo("SUCCESS","Book Registered")
     except:
          mbox.showinfo("ERROR","Failed to register book. Try again")
def add_bookback():
    try :
          root7.destroy()
          admin_page()
    except:pass
def add_book():
     global root7,bookid,bookname,bookqty,bookdealer
     try:
          root6.destroy()
     except:
          pass
     root7 = Tk()
     bookid = StringVar()
     bookname = StringVar()
     bookqty = StringVar()
     bookdealer = StringVar()
     root7.geometry("1000x700")
     pic=PhotoImage(file='zencred2.png')
     Label(root7,image=pic).place(relwidth=1,relheight=1)
     Label(root7,text = "Book id",bg='black',fg='white').place(x=200,y=200)
     
     b1 = Entry(root7,textvariable = bookid)
     b1.place(x=200,y=220)
     
     Label(root7,text = "Book Name",bg='black',fg='white').place(x=200,y=240)
     
     b2 = Entry(root7,textvariable = bookname)
     b2.place(x=200,y=260)

     Label(root7,text = "Book Quantity",bg='black',fg='white').place(x=200,y=280)
     
     b3 = Entry(root7,textvariable = bookqty)
     b3.place(x=200,y=300)

     Label(root7,text = "Book Author",bg='black',fg='white').place(x=200,y=320)
     
     b4 = Entry(root7,textvariable = bookdealer)
     b4.place(x=200,y=340)
     pic2=PhotoImage(file='subutton.png')
     button1 = Button(root7,image=pic2,width=120,height=25,bg='black',command = submitbook)
     button1.place(x=200,y=380)
     pic3=PhotoImage(file='back.png')
     button2 = Button(root7,image=pic3,width=120,height=25,bg='black',command=add_bookback)                #,command
     button2.place(x=200,y=420)
     root7.mainloop()

def addm_book():
     admno = addno.get()
     bookid = bid.get()
     if admno and bookid:
          st = f'select Name,Class from studetail where Adno = {admno}' 
          cur.execute(st)
          stdname = cur.fetchone()
          st = f"select Name,avilableqty from bookdetail where bookid = '{bookid}'"
          cur.execute(st)
          values = cur.fetchone()
          if values and stdname:
               if values[-1] >0:
                    today = datym.date.today()
                    DD = datym.timedelta(days=10)
                    earlier = today + DD
                    earlier_str = earlier.strftime("%Y-%m-%d")
                    today_str = today.strftime("%Y-%m-%d")
                    st = f"insert into issuedbooks values({admno},'{stdname[0]}','{stdname[1]}','{bookid}','{values[0]}','{today_str}','{earlier_str}','')"
                    cur.execute(st)
                    con.commit()
                    st = f"update bookdetail set avilableqty=avilableqty-1 where bookid='{bookid}'"
                    cur.execute(st)
                    con.commit()
                    mbox.showinfo("SUCCESS",f"Book nammed {values[0]} issued to {stdname[0]}\n Due date for submission {earlier_str}")
                    
               else:
                    mbox.showinfo("ERROR","Book Currently Not Available")
          else:
               mbox.showinfo("ERROR","Enter Correct Addmission number or Book Id")
     else:
          mbox.showinfo("Enter","Fill All Parameters.")
def issue_booksback():
     try :
          root8.destroy()
          admin_page()
     except:pass
def issue_books():
     try:
          root6.destroy()
     except:
          pass
     global root8,addno,bid
     root8 = Tk()
     root8.geometry('1000x700')
     addno = StringVar()
     bid = StringVar()
     pic=PhotoImage(file='zenew.png')
     Label(root8,image=pic).place(relwidth=1,relheight=1)
     Label(root8,text="Admission Number:",bg='black',fg='white',font=('times',18,'italic')).place(x=410,y=300)
     b1 = Entry(root8,textvariable = addno)
     b1.place(x=450,y=330)

     Label(root8,text="Book Id:",bg='black',fg='white',font=('times',18,'italic')).place(x=450,y=380)
     b2 = Entry(root8,textvariable = bid)
     b2.place(x=450,y=410)
     pic2=PhotoImage(file='subutton.png')
     b3 = Button(root8,image=pic2,command= addm_book,width=120,height=25,bg='black')
     pic3=PhotoImage(file='back.png')
     button2 = Button(root8,image=pic3,width=120,height=25,bg='black',command=issue_booksback)                #,command
     button2.place(x=450,y=500)
     b3.place(x=450,y=450)
     root8.mainloop()
#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----#-----##

def adminlogout():
     try:
          root6.destroy()
          admin()
     except:
          pass
def admin_page():
     global root6
     try:
          root1.destroy()
     except:
          pass
     root6 = Tk()
     root6.geometry("1000x700")
     pic=PhotoImage(file='zenauth.png')
     Label(root6,image=pic).place(relwidth=1,relheight=1)
     b1=PhotoImage(file='adbook.png')
     bb1=Button(root6,image=b1,height=25,width=150,command = add_book)
     bb1.place(x=460,y=250)
     b2=PhotoImage(file='bkdet.png')
     bb2=Button(root6,image=b2,height=25,width=150, command = view_book)
     bb2.place(x=460,y=290)
     b3=PhotoImage(file='issue.png')
     bb3=Button(root6,image=b3,height=25,width=150, command = issue_books)
     bb3.place(x=460,y=330)
     
     ty=PhotoImage(file='submibook.png')
     bb4=Button(root6,image=ty, height=25,width=150,command= to_submit)
     bb4.place(x=460,y=370)

     b5=PhotoImage(file='histry.png')
     bb5=Button(root6,image=b5,height=25,width=150,bg='white',command = history)
     bb5.place(x=460,y=410)
     
     b4=PhotoImage(file='studet.png')
     bb6=Button(root6,image=b4,height=25,width=150,command = student_details)
     bb6.place(x=460,y=450)
     
     pic3=PhotoImage(file='logout.png')
     button2 = Button(root6,image=pic3,width=160,height=25,bg='black',command=adminlogout)   
     button2.place(x=460,y=490)
     root6.mainloop()
     


def admin_login():
     adnusn = adnvalue.get()
     adnpwd = adnvalue2.get()
     cur.execute("select * from adetail")
     adndetails = cur.fetchall()
     for i in adndetails:
          if adnusn == i[-2] and adnpwd == i[-1]:
               admin_page()
          else:
               mbox.showinfo("ERROR!","Incorrect Password or Username.")
     
def admin():
     global root1,adnvalue,adnvalue2
     try:
          root.destroy()
     except:
          pass
     root1= Tk()
     root1.geometry("1000x700")
     adnvalue=StringVar()
     adnvalue2=StringVar()
     bg=PhotoImage(file='wlecome.png')
     Label(root1,image=bg).place(relwidth=1,relheight=1)
     bck=PhotoImage(file='backbtn.png')

   
     Backbtn=Button(root1,bg='#2A382B',image=bck,height=30,width=80,command=admin_back)
     Backbtn.grid(row=1,column=1)
     username=Entry(root1,width=30,textvariable=adnvalue).place(x=450,y=300)
     password=Entry(root1,width=30,textvariable=adnvalue2,show='•').place(x=450,y=325)
     login=PhotoImage(file='login.png')
     loginbtn=Button(root1,image=login,bg='black',height=25,width=175,command  = admin_login)
     loginbtn.place(x=450,y=360)

     
     signin=PhotoImage(file='signin.png')
     signinbtn=Button(root1,image=signin,bg='black',height=25,width=175,command=enter_code)
     signinbtn.place(x=450,y=450)

     signup=PhotoImage(file='signin.png')
     signupbtn=Button(root1,image=signup,bg='black',height=25,width=175, command = studregister)
     signupbtn.place(x=450,y=525)
     Label(root1,text='New admin?',fg='white',bg='#37322F').place(x=450,y=425)
     Label(root1,text='New student?',fg='white',bg='#37322F').place(x=450,y=500)
     root1.mainloop()

def admin_valid():
     code = passvalue.get()
     if code == schoolcode:
          admin_registration()
     else:
          mbox.showinfo("ERROR!","Incorrect school code") 

def enter_codeback():
     root3.destroy()
     admin()
def enter_code():
     global root3,passvalue
     try:
          root1.destroy()
     except:
          pass

     root3 =Tk()
     root3.geometry("1000x700")
     passvalue = StringVar()
     bg=PhotoImage(file='zenauth.png')
     Label(root3,image=bg).place(relwidth=1,relheight=1)
     l1=Label(root3,text="Enter school code",bg='#1C1C1A',fg='white')
     l1.place(x=650,y= 250)
     e1 = Entry(root3,textvariable = passvalue)
     e1.place(x=650,y=300)
     b1 = Button(root3,text="OK",bg='#252525',fg='white', command= admin_valid)
     b1.place(x=650,y= 350)
     b2 = Button(root3,text="BACK",bg='#191919',fg='white',command = enter_codeback)##command
     b2.place(x=680,y= 350)
     root3.mainloop()
def submit_values():
     global cur,con
     adnom=adno.get()
     nam=lastvalue.get()
     uname=uservalue.get()
     pwd=pwdvalue.get()
     conpwd=conpwdvalue.get()
     doj=datym.datetime.now()
     
     if pwd!=conpwd:
          mbox.showinfo('Alert','Password Does Not Match!')
     elif len(uname)>20 or len(pwd)>20:
          mbox.showinfo('Alert!','Maximum limit is 20 characters')
     elif len(uname)<5 or len(pwd)<5:
          mbox.showinfo('Alert!','Minimum limit is 5 characters')
     else:
          cur.execute(f"insert into adetail values({adnom},'{nam}','{doj}','{uname}','{pwd}')")
          con.commit()
          mbox.showinfo("SUCCESS","Admin registered. Please login with your login crdentials.")
          
def adminreg_back():
     root4.destroy()
     admin()
def admin_registration():
     global root4,adno,lastvalue,uservalue,pwdvalue,conpwdvalue
     try:
          root3.destroy()
     except:
          pass
     root4 = Tk()
     root4.geometry("1000x700")
     adno=StringVar()
     lastvalue=StringVar()
     uservalue=StringVar()
     pwdvalue=StringVar()
     conpwdvalue=StringVar()
     def intrback():
          root2.destroy()
          newroot()
     
     bg=PhotoImage(file='zenregis.png')
     Label(root4,image=bg).place(relwidth=1,relheight=1)
     Label(root4,text='Name:',bg='#39322C',fg='white').place(x=540,y=200)
     frstname=Entry(root4,width=30,textvariable=lastvalue).place(x=650,y=200)

     Label(root4,text='Adno:',bg='#39322C',fg='white').place(x=540,y=250)
     adno1=Entry(root4,width=30,textvariable=adno).place(x=650,y=250)

     Label(root4,text='Username:',bg='#38302D',fg='white').place(x=540,y=300)
     username=Entry(root4,width=30,textvariable=uservalue).place(x=650,y=300)

     Label(root4,text='Password:',bg='#332B28',fg='white').place(x=540,y=325)
     passwd=Entry(root4,width=30,textvariable=pwdvalue,show='•').place(x=650,y=325)

     Label(root4,text='Confirm password:',bg='#342D27',fg='white').place(x=540,y=350)
     confirmpwd=Entry(root4,width=30,textvariable=conpwdvalue,show='•').place(x=650,y=350)

     sub=PhotoImage(file='subutton.png')
     submit1=Button(root4,image=sub,bg='black',height=50,width=175,command = submit_values)
     submit1.place(x=650,y=450)
     

     back=PhotoImage(file='backbtn.png')
     intr=Button(root4,bg='#16120F',image=back,height=30,width=80, command = adminreg_back)
     intr.grid(row=1,column=1)     
     root4.mainloop()

def studentreg_back():
     root2.destroy()
     main_window()
     
def admin_back():
     root1.destroy()
     main_window()

def validate_resetpwd():
    usr = rusr.get()
    pwd= rpwd.get()
    cpwd = rcpwd.get()
    notp = rotp.get()
    if usr and pwd and cpwd and notp:
        if int(notp) == int(otp):
            s = f'select * from studetail where Username = "{usr}"'
            cur.execute(s)
            r = cur.fetchone()
            if r:
                if pwd == cpwd:
                    s = f'update studetail set Password = "{pwd}" where Username = "{usr}"'
                    cur.execute(s)
                    con.commit()
                    mbox.showinfo('SUCCUESS','Password updated successfully')
                else:
                    mbox.showinfo('ERROR','Passwords do not match!')
            else:
                mbox.showinfo('ERROR','Invalid Username')
        else:
            mbox.showinfo('ERROR','Enter correct OTP')
    else:
        mbox.showinfo('ERROR','Enter All values')
def otps(otp):
    mbox.showinfo('OTP',f"Your OTP for passwword reset is {otp}")
def speakagain():
    global c
    speak(c)
    c=''
def forgotpassword():
    global root10,otp,rotp,rusr,rpwd,rcpwd,c
    try:
        root2.destroy()
    except:
        pass
    otp = random.randint(1000,9999)
    
    root10=Tk()
    
    root10.geometry('1000x700')
    
    rusr=StringVar()
    rpwd = StringVar()
    rcpwd = StringVar()
    rotp = StringVar()
   
    pic=PhotoImage(file='zenauth2.png')
    Label(root10,image=pic).place(relwidth=1,relheight=1)

    e = Entry(root10,textvariable = rusr)
    e.place(x=520,y=240)

    en = Entry(root10,textvariable = rpwd,show='•')
    en.place(x=520,y=275)


    e = Entry(root10,textvariable = rcpwd,show='•')
    e.place(x=610,y=310)


    e = Entry(root10,textvariable = rotp)
    e.place(x=460,y=360)
    sub3=PhotoImage(file='sub3.png')
    bu = Button(root10,image=sub3,bg='white',height=25,width=150,command=validate_resetpwd)
    bu.place(x=320,y=500)
    sub2=PhotoImage(file='backw.png')
    bu = Button(root10,image=sub2,bg='white',height=25,width=150,command=pwdback)
    bu.place(x=500,y=500)
    
##    Label(root10,text=f'YOUR OPT IS:{otp}',fg='red').grid(row = 6,columnspan = 2)
    c=f'YOUR O,..T,..P,.. IS.. {otp}'
    speak(c)
    sub=PhotoImage(file='rpotp.png')
    spa = Button(root10,image=sub,bg='white',height=25,width=150,command=speakagain)
    spa.place(x=680,y=500)
##    otps(otp)
    root10.mainloop()
def pwdback():
    root10.destroy()
    student()

def searchhis():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    p=s1.get()
    if p!='':
        try:
            search2.delete(0,END)
            sql1=f'select * from issuedbooks where bookid ="{p}" and adno="{val[0]}" '
            cur.execute(sql1)
            r=cur.fetchall()
            total=len(r)
            labl.configure(text=total)
            for i in tree.get_children():
                tree.delete(i)
            for i in r:
                tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
            con.close()
        except:
            mbox.showinfo('ALERT!','Unable to search book.')



def rehis():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    cur.execute(f'select * from issuedbooks where adno="{val[0]}"')
    r=cur.fetchall()
    total=len(r)
    labl.configure(text=total)
    for i in tree.get_children():
        tree.delete(i)
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))

        
def view_history():
    con=sq.connect(host='localhost',user='root',passwd='123',database="librarymanagement")
    cur=con.cursor()
    global labl,s1,search2,tree,viewform
    try:
        root11.destroy()
    except:  
        pass
    viewform=Tk()
    #-----
    style = ttk.Style(viewform)

    style.theme_use("clam")
    style.configure("Treeview", background="black", fieldbackground="#D1A684", foreground="black")
    #-----
    
    viewform.geometry('1200x650')
    viewform.title('TO SUBMIT DETAILS')
    s1=StringVar()
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=300,bg='#FE858D')
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    text = Label(TopViewForm, text="Student Details", bg='#37CBBE',fg='white',font=('times', 18,'italic'), width=600)
    text.pack(fill=X)
    txtsearch = Label(LeftViewForm, text="BOOK ID",bg='#FE858D',fg='white',font=('times', 20,'bold','italic')).place(x=70,y=50)
    search2 = Entry(LeftViewForm, font=(15),bd=3,textvariable=s1 ,width=20)
    search2.place(x=50,y=100)
    photo = PhotoImage(file = "search.png")
    search = Button(LeftViewForm,image=photo,bd=0,bg='#FE858D',height=40,width=100,command=searchhis).place(x=70,y=150)

    photo4 = PhotoImage(file = "refresh.png")
    delete = Button(LeftViewForm,image=photo4,bd=0,bg='#FE858D',height=40,width=100,command=rehis).place(x=60,y=390)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=('1','2','3','4','5','6','7','8'), height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree['columns']=('1','2','3','4','5','6','7','8')
    tree['show']='headings'
    tree.heading('1',text='Admission Number')
    tree.heading('2',text='Name')
    tree.heading('3',text='Class')
    tree.heading('4',text='BookId')
    tree.heading('5',text='Book Name')
    tree.heading('6',text='D.O.I')
    tree.heading('7',text='Due Date')
    tree.heading('8',text='D.O.S')
    tree.column('8',width=280,anchor='center')
    tree.column('7',width=280,anchor='center')
    tree.column('6',width=280,anchor='center')
    tree.column('5',width=280,anchor='center')
    tree.column('4',width=280,anchor='center')
    tree.column('3',width=240,anchor='center')
    tree.column('2',width=240,anchor='center')
    tree.column('1',width=170,anchor='center')
    tree.pack()
    cur.execute(f'select * from issuedbooks where adno="{val[0]}"')
    r=cur.fetchall()
    for i in r:
        tree.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    cur.execute(f'select fine from studetail where Adno="{val[0]}"')
    total_fine = cur.fetchone()
    photo44 = PhotoImage(file = "back1.png")
    search = Button(LeftViewForm,image=photo44,height=40,width=70,bg='#FE858D',bd=0,command=history_back).place(x=80,y=460)
    Label(viewform,text='TOTAL FINE : ',bg='#FE858D',fg='white',font=('times',14,'italic')).place(x=40,y=575)
    labl=Label(viewform,text=total_fine,bg='#FE858D',fg='white',font=('times',20,'bold'))
    labl.place(x=140,y=600)
    viewform.mainloop()

def history_back():
    viewform.destroy()
    student_page()
def hlogout():
    root11.destroy()
    student()
def student_page():
    global root11,val
    try:
        root2.destroy()
    except:
        pass
    root11 =Tk()
    root11.geometry('1000x700')
    s = f'select * from studetail where Username = "{studentusr}"'
    cur.execute(s)
    val = cur.fetchone()
    bg=PhotoImage(file='woood.png')
    Label(root11,image=bg).place(relwidth=1,relheight=1)
    Label(root11,text= 'STUDENT DETAILS',fg='white',font=('times',30,'italic'),bg='#95512B').place(x =350, y=180)
    Label(root11,text= '='*24,fg='white',font=('times',16,'italic'),bg='#95512B').place(x =350, y=220)
    Label(root11,text= 'Addmission No:',fg='white',bg='#95512B',font=('times',16,'italic')).place(x =350, y=250)
    Label(root11,text= f'{val[0]}',fg='white',bg='#95512B',font=('times',16,'italic')).place(x =550, y=250)
    Label(root11,text= 'Name:',fg='white',bg='#95512B',font=('times',16,'italic')).place(x =350, y=300)
    Label(root11,text= f'{val[1]}',fg='white',bg='#95512B',font=('times',16,'italic')).place(x =550, y=300)
    Label(root11,text= 'D.O.B:',fg='white',bg='#95512B',font=('times',16,'italic')).place(x =350, y=350)
    Label(root11,text= f'{val[2]}',fg='white',bg='#95512B',font=('times',16,'italic')).place(x =550, y=350)
    Label(root11,text= 'Class:',fg='white',bg='#95512B',font=('times',16,'italic')).place(x =350, y=400)
    Label(root11,text= f'{val[3]}',fg='white',bg='#95512B',font=('times',16,'italic')).place(x =550, y=400)
    Label(root11,text= 'Fine amount:',fg='white',bg='#95512B',font=('times',16,'italic')).place(x =350, y=450)
    Label(root11,text= f'{val[6]}',fg='white',bg='#95512B',font=('times',16,'italic')).place(x =550, y=450)

    pic2=PhotoImage(file='hstrvw.png')
    b = Button(root11,image=pic2,width=165,height=25,bg='black',command = view_history)
    b.place(x=400,y=550)
    pic=PhotoImage(file='logout.png')
    b1 = Button(root11,image=pic,width=175,height=25,bg='black',command = hlogout)
    b1.place(x=400,y=600)
    root11.mainloop()

def validate_student_login():
    global studentusr
    studentusr = susername.get()
    pwd = spwd.get()
    s = f"select * from studetail where Username='{studentusr}' and Password = '{pwd}'"
    cur.execute(s)
    result = cur.fetchone()
    if result:
        student_page()
    else:
        mbox.showinfo("ERROR",'Invalid Login Credentials')
    
    
    
#-----#-----#-----#-----#-------------##

def student():
     global root2,susername,spwd
     try:
          root.destroy()
     except:
          pass
     root2=Tk()
     root2.title('Student Page')
     root2.geometry('1000x700')
     
     
     susername=StringVar()
     spwd=StringVar()
     bg=PhotoImage(file='wlecome.png')
     Label(root2,image=bg).place(relwidth=1,relheight=1)

    
     username=Entry(root2,width=30,textvariable=susername).place(x=450,y=300)
     password=Entry(root2,width=30,textvariable=spwd,show='•').place(x=450,y=325)

     bck=PhotoImage(file='backbtn.png')

   
     Backbtn=Button(root2,bg='#2A382B',image=bck,height=30,width=80,command=studentreg_back)
     Backbtn.grid(row=1,column=1)

     
     login=PhotoImage(file='login.png')
     loginbtn=Button(root2,image=login,bg='black',height=25,width=175,command = validate_student_login)
     loginbtn.place(x=450,y=360)
     fpwd=PhotoImage(file='frgtpwd.png')
     pwdresetbutton = Button(root2,image=fpwd,bg='#4C98BE',height=30,width=160,command = forgotpassword)
     pwdresetbutton.place(x = 460,y = 410)
     
     root2.mainloop()


def submitstud():
     global cur
     global con
     idstud=stdvalue.get()
     nam=stdlastvalue.get()
     dob=stddobvalue.get()
     classec=stdclassvalue.get()
     uname=stduservalue.get()
     pwd=stdpwdvalue.get()
     conpwd=stdconpwdvalue.get()
     
     if pwd!=conpwd:
          mbox.showinfo('Alert','Password Does Not Match!')
     elif len(uname)>20 or len(pwd)>20:
          mbox.showinfo('Alert!','Maximum limit is 20 characters')
     elif len(uname)<5 or len(pwd)<5:
          mbox.showinfo('Alert!','Maximum limit is 20 characters')
     else:
          st='insert into studetail values({},"{}","{}","{}","{}","{}",0)'.format(idstud,nam,dob,classec,uname,pwd)
          cur.execute(st)
          con.commit()
          mbox.showinfo("success","Student registration successful!")
          

def student_back():
     root5.destroy()
     admin()
def studregister():
     global root5,stdvalue,stdlastvalue,stddobvalue,stduservalue,stdclassvalue,stdpwdvalue,stdconpwdvalue
     try:
          root1.destroy()
     except:
          pass
     root5=Tk()
     root5.title(' Page')
     root5.geometry('1000x700')
     
     stdvalue=StringVar()
     stdlastvalue=StringVar()
     stddobvalue=StringVar()
     stduservalue=StringVar()
     stdclassvalue=StringVar()
     stdpwdvalue=StringVar()
     stdconpwdvalue=StringVar()
     

     bg=PhotoImage(file='zenregis.png')
     Label(root5,image=bg).place(relwidth=1,relheight=1)
     
     Label(root5,text='Admission Number:',bg='#4B4138',fg='white').place(x=540,y=200)
     frstname=Entry(root5,width=30,textvariable=stdvalue).place(x=650,y=200)

     Label(root5,text='Name:',bg='#39322C',fg='white').place(x=540,y=225)
     lastname=frstname=Entry(root5,width=30,textvariable=stdlastvalue).place(x=650,y=225)

     Label(root5,text='Dob(YYYY-MM-DD):',bg='#413A33',fg='white').place(x=540,y=250)
     DOB=Entry(root5,width=30,textvariable=stddobvalue).place(x=650,y=250)

     Label(root5,text='Class:',bg='#342D27',fg='white').place(x=540,y=275)
     classs=Entry(root5,width=30,textvariable=stdclassvalue).place(x=650,y=275)

     Label(root5,text='Username:',bg='#38302D',fg='white').place(x=540,y=300)
     username=Entry(root5,width=30,textvariable=stduservalue).place(x=650,y=300)

     Label(root5,text='Password:',bg='#332B28',fg='white').place(x=540,y=325)
     passwd=Entry(root5,width=30,textvariable=stdpwdvalue,show='•').place(x=650,y=325)

     Label(root5,text='Confirm password:',bg='#342D27',fg='white').place(x=540,y=350)
     confirmpwd=Entry(root5,width=30,textvariable=stdconpwdvalue,show='•').place(x=650,y=350)

     sub=PhotoImage(file='subutton.png')
     submit=Button(root5,image=sub,bg='black',height=20,width=175,command=submitstud)
     submit.place(x=650,y=450)
     

     back=PhotoImage(file='backbtn.png')
     intr=Button(root5,bg='#16120F',image=back,command=student_back,height=30,width=80)
     intr.grid(row=1,column=1)
     root5.mainloop()


def main_window():
     global root
     root=Tk()
     root.title('Enter as')
     root.geometry('1000x700')
     pic1=PhotoImage(file='zenbg.png')
     Label(root,image=pic1).place(relwidth=1,relheight=1)
     btpic1=PhotoImage(file='admin.png')
     b1=Button(root,text='ADMIN',padx=30,pady=15,bg='#372515',image=btpic1, command=admin)
     b1.place(x=460,y=300)

    
     btpic=PhotoImage(file='student.png')
     b2=Button(root,text='STUDENT',padx=30,pady=15,bg='#372515',image=btpic,command = student)
     b2.place(x=450,y=390)
     
     root.mainloop()

if __name__ == "__main__":
    main_window()    
