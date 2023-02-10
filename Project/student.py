##import mysql.connector as sq
##
##def initials():
##     mycon=sq.connect(host='localhost',user='root',passwd='123')
##     cur=mycon.cursor()
##     cur.execute('create database if not exists LibraryManagement')
##     cur.execute('use LibraryManagement')
##     cur.execute('create table if not exists studetail(Adno int(6) ,Name varchar(30),dob date,Class varchar(3),Username varchar(20),Password varchar(20),Primary Key(Adno))')
##     cur.execute('create table if not exists adetail(Id int(4) ,Name varchar(30),dateofjoin datetime,Username varchar(20),Password varchar(20),Primary Key(Id))')
##     mycon.commit()
##     cur.close()
##     mycon.close()
##initials()
##
##''' stud register be in admin itself .....changes in studsub function'''


from tkinter import *
from tkinter import messagebox as mbox
import mysql.connector as sq
import pyttsx3
import speech_recognition as sr
import datetime as datym
import os
import wikipedia as wiki
import webbrowser as browser
import smtplib as smt

school_code='THeZen202*L!bR4RY'


def oldwindow():
     global tk
     tk=Tk()
     tk.title('Enter as')
     tk.geometry('1000x700')
     pic1=PhotoImage(file='zenbg.png')
     Label(tk,image=pic1).place(relwidth=1,relheight=1)
     btpic1=PhotoImage(file='admin.png')
     def initials():
          global mycon
          global cur
          mycon=sq.connect(host='localhost',user='root',passwd='123')
          cur=mycon.cursor()
          cur.execute('create database if not exists LibraryManagement')
          cur.execute('use LibraryManagement')
          cur.execute('create table if not exists studetail(Adno int(6) ,Name varchar(30),dob date,Class varchar(3),Username varchar(20),Password varchar(20))')   #set the primary keys
          cur.execute('create table if not exists adetail(Id int(4) ,Name varchar(30),dateofjoin datetime,Username varchar(20),Password varchar(20))')
          mycon.commit()
     initials()
     def back():
          root.destroy()
          oldwindow()
##-----------------------------------------------------------------------ADMIN ZONE------------------------------------------------------------------------------------

     def admin():
          tk.destroy()
          def newroot():
               global root
               root=Tk()
               root.title('Admin Page')
               root.geometry('1000x700')

     ##          def adminregister():
     ##               global accepted_code
     ##               
     ##               if accepted_code==school_code:
                         
               value=StringVar()
               value2=StringVar()
               bg=PhotoImage(file='wlecome.png')
               Label(root,image=bg).place(relwidth=1,relheight=1)
              
               username=Entry(root,width=30,textvariable=value).place(x=450,y=300)
               password=Entry(root,width=30,textvariable=value2,show='•').place(x=450,y=325)
               def back1():
                         root.destroy()
                         oldwindow()
                         
               bck=PhotoImage(file='backbtn.png')
               Backbtn=Button(root,bg='#2A382B',image=bck,command=back,height=30,width=80)
               Backbtn.grid(row=1,column=1)
               def studregister():
                    global root2
                    root.destroy()
                    root2=Tk()
                    root2.title(' Page')
                    root2.geometry('1000x700')
                    def submitstud():
                         global cur
                         global con
                         adno=value.get()
                         nam=lastvalue.get()
                         dob=dobvalue.get()
                         classec=classvalue.get()
                         uname=uservalue.get()
                         pwd=pwdvalue.get()
                         conpwd=conpwdvalue.get()
                         
                         if pwd!=conpwd:
                              mbox.showinfo('Alert','Password Does Not Match!')
                         elif len(uname)>20 or len(pwd)>20:
                              mbox.showinfo('Alert!','Maximum limit is 20 characters')
                         elif len(uname)<5 or len(pwd)<5:
                              mbox.showinfo('Alert!','Maximum limit is 20 characters')
                         else:

##                              st='insert into studetail values({},'{}','{}','{}','{}','{}')'.format(adno,nam,dob,classec,uname,pwd)
##                              cur.execute(st)
##                              con.commit()


                    value=StringVar()
                    lastvalue=StringVar()
                    dobvalue=StringVar()
                    uservalue=StringVar()
                    classvalue=StringVar()
                    pwdvalue=StringVar()
                    conpwdvalue=StringVar()
                    def intrback():
                         root2.destroy()
                         newroot()

                    bg=PhotoImage(file='zenregis.png')
                    Label(root2,image=bg).place(relwidth=1,relheight=1)

                    Label(root2,text='Admission Number:',bg='#4B4138',fg='white').place(x=540,y=200)
                    frstname=Entry(root2,width=30,textvariable=value).place(x=650,y=200)

                    Label(root2,text='Name:',bg='#39322C',fg='white').place(x=540,y=225)
                    lastname=frstname=Entry(root2,width=30,textvariable=lastvalue).place(x=650,y=225)

                    Label(root2,text='Dob:',bg='#413A33',fg='white').place(x=540,y=250)
                    DOB=Entry(root2,width=30,textvariable=dobvalue).place(x=650,y=250)

                    Label(root2,text='Class:',bg='#342D27',fg='white').place(x=540,y=275)
                    classs=Entry(root2,width=30,textvariable=classvalue).place(x=650,y=275)

                    Label(root2,text='Username:',bg='#38302D',fg='white').place(x=540,y=300)
                    username=Entry(root2,width=30,textvariable=uservalue).place(x=650,y=300)

                    Label(root2,text='Password:',bg='#332B28',fg='white').place(x=540,y=325)
                    passwd=Entry(root2,width=30,textvariable=pwdvalue,show='*').place(x=650,y=325)

                    Label(root2,text='Confirm password:',bg='#342D27',fg='white').place(x=540,y=350)
                    confirmpwd=Entry(root2,width=30,textvariable=conpwdvalue,show='*').place(x=650,y=350)

                    sub=PhotoImage(file='subutton.png')
                    submit=Button(root2,image=sub,bg='black',height=20,width=175,command=submitstud)
                    submit.place(x=650,y=450)
                    

                    back=PhotoImage(file='backbtn.png')
                    intr=Button(root2,bg='#16120F',image=back,command=intrback,height=30,width=80)
                    intr.grid(row=1,column=1)
                    root2.mainloop()
                         

               

               login=PhotoImage(file='login.png')
               loginbtn=Button(root,image=login,bg='black',height=25,width=175)
               loginbtn.place(x=450,y=360)
               
               signin=PhotoImage(file='signin.png')
               signinbtn=Button(root,image=signin,bg='black',height=25,width=175)
               signinbtn.place(x=450,y=450)

               signup=PhotoImage(file='signin.png')
               signupbtn=Button(root,image=signup,bg='black',height=25,width=175,command=studregister)
               signupbtn.place(x=450,y=525)
               Label(root,text='New admin?',fg='white',bg='#37322F').place(x=450,y=425)
               Label(root,text='New student?',fg='white',bg='#37322F').place(x=450,y=500)
               root.mainloop()
          newroot()
##-------------------------------------------------------------------------STUDENT ZONE--------------------------------------------------------------------------------          

     def student():
          global root
          tk.destroy()
          def newroot():
               root=Tk()
               root.title('Student Page')
               root.geometry('1000x700')

               value=StringVar()
               value2=StringVar()
               bg=PhotoImage(file='wlecome.png')
               Label(root,image=bg).place(relwidth=1,relheight=1)
              
               username=Entry(root,width=30,textvariable=value).place(x=450,y=300)
               password=Entry(root,width=30,textvariable=value2,show='•').place(x=450,y=325)

               bck=PhotoImage(file='backbtn.png')

               def back1():
                    root.destroy()
                    oldwindow()
               Backbtn=Button(root,bg='#2A382B',image=bck,command=back1,height=30,width=80)
               Backbtn.grid(row=1,column=1)
          
               
               login=PhotoImage(file='login.png')
               loginbtn=Button(root,image=login,bg='black',height=25,width=175)
               loginbtn.place(x=450,y=360)
               
               root.mainloop()
          


          newroot()
     b1=Button(tk,text='ADMIN',padx=30,pady=15,bg='#372515',image=btpic1,command=admin)
     b1.place(x=460,y=300)

    
     btpic=PhotoImage(file='student.png')
     b2=Button(tk,text='STUDENT',padx=30,pady=15,bg='#372515',image=btpic,command=student)
     b2.place(x=450,y=390)
     
     tk.mainloop()
oldwindow()
