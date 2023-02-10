##from tkinter import*
####def admin():
####     tk.destroy()
####     root=Tk()
####     root.title('%s Page'%t)
####     root.geometry('1000x700')
####
####     value=StringVar()
####     value2=StringVar()
####     bg=PhotoImage(file='wlecome.png')
####     Label(root,image=bg).place(relwidth=1,relheight=1)
####    
####     username=Entry(root,width=30,textvariable=value).place(x=450,y=300)
####     password=Entry(root,width=30,textvariable=value2).place(x=450,y=325)
####
####     bck=PhotoImage(file='backbtn.png')
####     Backbtn=Button(root,bg='#2A382B',padx=15,pady=10,image=bck)
####     Backbtn.grid(row=1,column=1)
####     root.mainloop()
####
##
##def studregister():
##     root2=Tk()
##     root2.title(' Page')
##     root2.geometry('1000x700')
##
##     value=StringVar()
##     lastvalue=StringVar()
##     dobvalue=StringVar()
##     uservalue=StringVar()
##     pwdvalue=StringVar()
##     conpwdvalue=StringVar()
##
##
##     bg=PhotoImage(file='zenregis.png')
##     Label(root2,image=bg).place(relwidth=1,relheight=1)
##
##     Label(root2,text='First Name:',bg='#4B4138',fg='white').place(x=540,y=200)
##     frstname=Entry(root2,width=30,textvariable=value).place(x=650,y=200)
##
##     Label(root2,text='Last Name:',bg='#39322C',fg='white').place(x=540,y=225)
##     lastname=frstname=Entry(root2,width=30,textvariable=lastvalue).place(x=650,y=225)
##
##     Label(root2,text='Dob:',bg='#413A33',fg='white').place(x=540,y=250)
##     DOB=Entry(root2,width=30,textvariable=dobvalue).place(x=650,y=250)
##
##     Label(root2,text='Username:',bg='#38302D',fg='white').place(x=540,y=275)
##     username=Entry(root2,width=30,textvariable=uservalue).place(x=650,y=275)
##
##     Label(root2,text='Password:',bg='#332B28',fg='white').place(x=540,y=300)
##     passwd=Entry(root2,width=30,textvariable=pwdvalue,show='*').place(x=650,y=300)
##
##     Label(root2,text='Confirm password:',bg='#342D27',fg='white').place(x=540,y=325)
##     confirmpwd=Entry(root2,width=30,textvariable=conpwdvalue,show='*').place(x=650,y=325)
##
##     bck=PhotoImage(file='backbtn.png')
##     Backbtn=Button(root,bg='#16120F',padx=15,pady=10,image=bck,command=intrback)
##     Backbtn.grid(row=1,column=1)
##     root2.mainloop()
import tkinter as tk
import webbrowser

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

root = tk.Tk()
lbl = tk.Label(root, text=r"http://www.google.com", fg="blue", cursor="hand2")
lbl.pack()
lbl.bind("<Button-1>", callback)
root.mainloop()
##def callback(event):
##    webbrowser.open_new(event.widget.cget("text"))
##
##root = tk.Tk()
##lbl = tk.Label(root, text=r"https://link.springer.com/", fg="blue", cursor="hand2")
##lbl.pack()
##lbl.bind("<Button-1>", callback)
##root.mainloop()
##
