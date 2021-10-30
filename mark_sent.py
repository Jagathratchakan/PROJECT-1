from tkinter import Button, Label, Frame, PhotoImage, Canvas, messagebox, Entry, Text,StringVar
import tkinter as tk
from tkinter import Scrollbar, Toplevel
import pyautogui as pg
import numpy as np
#import pywhatkit.exceptions
from PIL import ImageTk, Image
from tkinter import filedialog
import pandas as pd
from tabulate import tabulate
from datetime import datetime
import pyautogui as py
from selenium import webdriver
import time
import sys
import sqlite3 as sq
# ex = pd.read_excel(r"C:\Users\tamil\Desktop\EVEN MID SEMESTER-I OVERALL MARKS-converted.xlsx")

home_bg = '#E9EDEC'
butt_bg = '#FF1493'
global sp_fram
csv = ""


# To exit the application
def quit():
    sys.exit()


def sub_email(email_ent, pas_ent):
    global email, password
    email = email_ent.get()
    password = pas_ent.get()
    messagebox.showinfo('message', 'You have entered')


def login():
    messagebox.showerror('error','Email login is not Available.')
    global fram
    for widget in s.winfo_children():
        if widget != fram:
            widget.destroy()

    ef = Frame(s, height=800, width=1100, bg=home_bg)
    ef.place(x=200, y=0)
    email_lab = Label(ef, text='Email Id', font=16)
    email_ent = Entry(ef, width=40)

    password_lab = Label(ef, text='Password', font=16)
    pas_ent = Entry(ef, width=40)
    sub_butt = Button(ef, text="submit", command=lambda: sub_email(email_ent, pas_ent))

    email_lab.place(x=300, y=300)
    email_ent.place(x=500, y=300)
    password_lab.place(x=300, y=350)
    pas_ent.place(x=500, y=350)
    sub_butt.place(x=500, y=400)





def analys():

    global fram,performancers
    for widget in s.winfo_children():
        if widget != fram:
               widget.destroy()

    def upload_analyze():
        analys()
        file_name = filedialog.askopenfilename()
        global csv
        csv = pd.read_excel(file_name)
        csv = pd.DataFrame(csv)
        print(csv)
        csv.set_index('regno', inplace=True)
        if str(csv):
              global info_lab,filt_butt,quick_analys_butt
              filt_butt.configure(state='active')
              quick_analys_butt.configure(state='active')
              info_lab.destroy()



    global analys_fram
    analys_fram = Frame(s,width=20,bg=home_bg)
    analys_fram.pack(expand=True,fill='both',side='left')
    share_bg = Label(analys_fram, image=new_6)
    share_bg.place(x=0, y=0)
    in_fram = Frame(analys_fram,width=500,height=500,bg="#3F8BA8")
    in_fram.pack(pady=150)



    global info_lab,filt_butt,quick_analys_butt
    info_lab = Label(in_fram, text="You need to upload a file!",bg='#E9EDEC', font=('Comic Sans MS', 24))
    info_lab.pack(side='bottom')

    filt_butt = Button(in_fram,text='Filter',width=20,bg='#A3E4D7',state='disabled',command = filter_analys)
    filt_butt.pack(pady=20)

    quick_analys_butt = Button(in_fram,text='Quick analyse',width=20,bg='#A3E4D7',state='disabled',command = quick_analys)
    quick_analys_butt.pack(pady=20)


    upload_butt2 = Button(analys_fram, text="Upload File", width=20, bg='#A3E4D7', command=upload_analyze)
    upload_butt2.pack(side='bottom', pady=20)




global performancers
def filter_analys():
    global csv, performancers, analys_fram
    performancers = []
    def filter():
            percentage = min_mark_ent.get()
            percentage = int(percentage)
            no_sub = int(no_ent.get())
            #print(csv)

            for reg in csv.index:
                count = 0
                for mark in csv.loc[reg]:
                      if mark == 'A':
                           performancers.append(reg)

                      try:
                          print(mark)

                          if int(mark) < percentage :
                                 count += 1

                      except TypeError:
                             pass
                      except ValueError:
                          pass

                if count >= no_sub:
                     if reg not in performancers:
                         performancers.append(reg)
            print(performancers)
            print(csv.loc[performancers]['mobile_no'])

            t = 0
            r = 0
            c = 0
            filt_window = Toplevel()
            filt_window.geometry("500x500")
            for i in performancers:

              name_but = Button(filt_window, text=i, bd=3, bg='#ADA3E4', relief='groove', command=lambda i=i: show_mark(i))
              name_but.grid(row=r,column = c,pady=10)#place(x=w,y=h)
              r += 1
              t += 1
              if t>10:
                  r += 1
                  c +=1
                  t = 0

            share_but=Button(filt_window,text="Share",bg="red",command=share_what)
            share_but.grid(row=10,column=200)
            mark_win.destroy()

    mark_win = Toplevel()
    mark_win.geometry("400x400")
    mark_win.resizable('false','false')
    min_mark_lab = Label(mark_win,text="Minimum Marks : ")
    no = Label(mark_win,text="No of subjects: ")
    min_mark_ent = Entry(mark_win)
    no_ent = Entry(mark_win)
    sub_butt = Button(mark_win,text="Submit",width=20,command=filter)

    min_mark_lab.place(x=0,y=0)
    min_mark_ent.place(x=150,y=0)
    no.place(x=0,y=40)
    no_ent.place(x=150,y=40)
    sub_butt.pack(side="bottom")


subjects = []
def quick_analys():
    global csv,analys_fram
    import matplotlib.pyplot as plt
    print(csv)


    def select(sub):
        global subjects
        if sub in subjects:
            subjects.remove(sub)
        else:
            subjects.append(sub)
        print(subjects)

    def save():
        sub_select_win.destroy()

    sub_select_win = Toplevel()
    sub_select_win.title("Subjects")
    sub_select_win.geometry("500x500")
    for col in csv.columns:
       sub_chk = tk.Checkbutton(sub_select_win,text=col,variable=col,command=lambda col=col:select(col))
       sub_chk.pack()
    sub_button = Button(sub_select_win,text='Submit',width=20,command=save)
    sub_button.pack(side="bottom")

    def visualize(regno):
        import matplotlib.pyplot as plt
        sub_df = csv[subjects]
        plt.bar(sub_df.columns,sub_df.loc[regno][subjects])
        plt.show()

    h = 170
    w = 50

    for i in csv.index:

        name_but_visual = Button(analys_fram, text=i, bd=3, bg='#ADA3E4', relief='groove', command=lambda i=i: visualize(i))
        name_but_visual.place(x=w, y=h)
        if h > 700:
            w += 200
            h = 170
        else:
            h += 50

    #plt.show()



msg = ""
def show_mark(i):
    global fram
    '''for widget in s.winfo_children():
        if widget != fram:
            widget.destroy()'''

    open_new()
    df = pd.DataFrame(csv.loc[i])
    nam = csv.loc[i]['Name']
    batch = ""
    year_sem = ""
    exam = ""
    try:
        batch = csv.loc[i]['batch']
        year = str(csv.loc[i]['year'])
        sem = str(csv.loc[i]['sem'])
        exam = csv.loc[i]['exam']
    except KeyError:

        pass
    df.loc['Name'] = 'Marks'
    num = df.loc['mobile_no']
    if csv.loc[i]['mobile_no'] != np.NaN:
        num = float(num);
        num = int(num)
        num = "+%.0f" % num
        df.loc['mobile_no'] = num
    df = df.rename({'Name': 'Subject'})

    #table = tabulate(df, headers='keys', tablefmt='orgtbl')

    global msg
    msg = f"M.KUMARASAMY COLLEGE OF ENGINNERING\nDepartment of Artificial Intelligence and DataScience\nBatch  : {batch}  \
        Year/sem : {year}/{sem}\n  Exam :{exam}\n\nName    :  {nam}\nRegno : " + str(df.head(6))
   # print(table)
    mark_label = Label(mark_win, text=msg)

    mark_label.pack()  # place(x=0,y=0)#(y=h,x=w+10)
    share_butt = Button(mark_win, bg='#A3E4D7', relief='solid', text='Share',
                        command=lambda: share(i))

    comm_butt = Button(mark_win, bg='#A3E4D7', relief='solid', text='Comment', command=comment)

    back_butt = Button(mark_win, bg='#A3E4D7', relief='solid', text='back',
                       command=lambda: back([mark_label, share_butt, back_butt]))

    share_butt.place(x=200, y=350)
    comm_butt.place(x=400, y=350)
    back_butt.place(x=550, y=350)


def comment():
    def gett():
        global msg
        comments = comm.get('1.0', 'end-1c')
        c.destroy()
        print(comments)
        msg += "\n\n comments : " + comments
        print(msg)

    c = Toplevel()
    c.title("Comments")
    c.resizable('false', 'false')
    comm = Text(c, height=20, width=52)
    back_butt = Button(c,bg=butt_bg, text='back', command=c.destroy,width=15)
    ok_butt = Button(c,bg=butt_bg, text='ok', command=gett,width=15)
    comm.pack()
    ok_butt.pack(side='left')
    back_butt.pack(side='right')


def upload():
    global csv, sp_fram,name_but
    home()
    send_page()
    file_name = filedialog.askopenfilename()

    csv = pd.read_excel(file_name)
    csv = pd.DataFrame(csv)
    print(csv)
    csv.set_index('regno', inplace=True)

    global h, w
    h = 170
    w = 50


    for i in csv.index:

        name_but = Button(sp_fram, text=i, bd=3, bg='#ADA3E4', relief='groove', command=lambda i=i: show_mark(i))
        name_but.place(x=w,y=h)
        if h > 700:
            w += 200
            h = 170
        else:
            h += 50


def share_what():
    driver = webdriver.Chrome()
    driver.get('https:web.whatsapp.com/')
    time.sleep(20)
    py.moveTo(240, 260, duration=1)
    time.sleep(15)
    py.press('tab')
    time.sleep(10)
    for x in performancers:
        ps_mark=str(csv.loc[x]["PS"])
        oopj=str(csv.loc[x]["OOPJ"])
        ds=str(csv.loc[x]["DS"])
        coa=str(csv.loc[x]["COA"])
        dld=str(csv.loc[x]["DLD"])
        faids=str(csv.loc[x]["FAIDS"])
        mobile=str(csv.loc[x]["mobile_no"])
        name=str(csv.loc[x]["Name"])
        try:
            batch = csv.loc[x]['batch']
            year = str(csv.loc[x]['year'])
            sem = str(csv.loc[x]['sem'])
            exam = csv.loc[x]['exam']
        except KeyError:
            pass
        mes="M.KUMARASAMY COLLEGE OF ENGINNERING                               Department of Artificial Intelligence and DataScience                              Batch  : " +batch+"        YEAR/SEM:"+year+"/"+sem+"                             NAME: "+name+"                                        PS         :"+ps_mark+"                                                         OOPJ     :"+oopj+"                                                              DS         :"+ds+"                                                         COA       :"+coa+"                                                     DLD       :"+dld+"                                                       FAIDS    :"+faids

        py.typewrite(mobile)
        time.sleep(2)
        py.press('enter')
        time.sleep(2)
        py.typewrite(mes.upper())
        py.press('enter')
        time.sleep(2)
        py.click(240, 280, duration=1)
        time.sleep(4)



def back(frame):
    for widget in frame:
        widget.destroy()
    mark_win.destroy()


def share(i):
    global num
    res = messagebox.askquestion('yesorno', f"Want to send to {csv.loc[i]['Name']}'s parents?")
    if res == 'yes':
        print("yes")

        import pywhatkit as pw

        pw.sendwhatmsg_instantly(num, msg, wait_time=20, tab_close=False)
        pg.press("enter")
        pg.alert("hi")


    elif res == 'no':
        pass


def send_page():

    global fram,sp_fram
    for widget in s.winfo_children():
        if widget != fram:
            widget.destroy()

    sp_fram = Frame(s, bg=home_bg)
    sp_fram.pack(expand=True,fill='both',side='left')#pack(expand=True,fill='y',side='right')#
    share_bg = Label(sp_fram, image=new_6)
    share_bg.place(x=0, y=0)
    #share_png = PhotoImage('download.jpeg')
    # img_lab = Label(sp_fram, image=img)
    # img_lab.pack(side='left',anchor='nw')

    upload_butt = Button(sp_fram, text="Upload", bg='#A3E4D7', height=1, width=40, relief='solid', command=upload)
    lab = Label(sp_fram, text="Students Marks", bg='#E9EDEC', font=('Comic Sans MS', 24))

    # c = Scrollbar(sp_fram,orient='vertical')
    # c.place(x=800,y=10)
    lab.pack(side='top')#place(x=650,y=0)
    upload_butt.pack(side='bottom',pady=30)#(x=630,y=900)#pack(side='bottom')
                     #side='bottom')


def open_new():
    global mark_win
    mark_win = Toplevel()
    mark_win.title('Marks')
    mark_win.geometry('700x400')
    mark_win.resizable('false', 'false')

def help():
    global fram
    for widget in s.winfo_children():
        if widget != fram:
            widget.destroy()



def home():
    global fram
    for widget in s.winfo_children():
        if widget != fram:
            widget.destroy()

    col = Label(s, image=home_new)
    col.place(x=150, y=0)

def faculty():
    global user_name
    global user_password, name, name_enter
    global password , password_enter, login
    teacher_login.destroy()
    student_login.destroy()
    fac_lab.destroy()
    stu_lab.destroy()
    user_name = StringVar()
    user_password = StringVar()
    name = Label(s, text="USER NAME: ", font=("Times", 20))
    name.place( x=350, y=150)
    name_enter = tk.Entry(s, textvariable=user_name, font=("Times", 13))
    name_enter.place(height=35, x=600, y=140)
    password = Label(s, text="ENTER PASSWORD:", font=("Times", 20)).place(height=30, x=320, y=200)
    password_enter = tk.Entry(s, textvariable=user_password, font=("Times", 16),show="*")
    password_enter.place(height=35, x=600, y=200)
    login=Button(s,text="LOG IN ", font=("Times", 20),fg="green",command=login_home)
    login.place(height=32, x=600, y=350)



def login_home():
    name1 = user_name.get()
    password1 = user_password.get()
    con = sq.connect("informations.db")
    d = con.cursor()
    find = ("SELECT * FROM Faculty WHERE NAME = ? AND PASSWORD = ?")
    d.execute(find, [(name1), (password1)])
    results = d.fetchall()
    if results:
        for i in results:
            home_set()
    else:
        print("no")

    con.commit()
    con.close()


def home_set():
    global mkce_lab,fram
    global image, fram
    image = Label(s, image=img_4)
    image.place(x=150, y=0)

    fram = Frame(s, bg="#070606", width=200)
    fram.pack(fill='y', side='left')
    home_butt = Button(fram, text='Home', bg=butt_bg, fg='#E9EDEC', height=1, width=20, command=home)
    home_butt.place(x=0, y=160)  # pack(pady=100)

    send_butt = Button(fram, text='Send Marks', bg=butt_bg, height=1, width=20, fg='#E9EDEC', command=send_page)
    send_butt.place(x=0, y=240)

    analys_butt = Button(fram, text="Analyse marks", height=1, width=20, bg=butt_bg, fg='#E9EDEC', command=analys)
    analys_butt.place(x=0, y=320)

    email_butt = Button(fram, text='Email login', height=1, width=20, bg=butt_bg, fg='#E9EDEC', command=login)
    # email_butt.place(x=0, y=400)

    help_butt = Button(fram, text='Help', height=1, width=20, bg=butt_bg, fg='#E9EDEC', command=help)
    help_butt.place(x=0, y=400)

    exit_butt = Button(fram, text='Exit', height=1, width=20, bg=butt_bg, fg="#E9EDEC", command=quit)
    exit_butt.place(x=0, y=480)

    '''img = Image.open("C:\\Users\\test\\Desktop\\mark_sender\\mkce.png")
    img = ImageTk.PhotoImage(img)
    image = Label(s, image=img)
    image.pack(side='left',anchor='nw')#(x=200, y=0)'''

    '''kr_logo = Image.open("C:\\Users\\tamil\\Desktop\\mark_sender\\kr.png")
    kr_logo = ImageTk.PhotoImage(kr_logo)
    kr_img = Label(s,image=kr_logo)
    kr_img.pack(side='right',anchor='ne')'''

    var1 = StringVar()

    def show(i):
        print(i)


# img_lab = Label(s, image=img)
# img_lab.place(x=800,y=0)

s = tk.Tk()
s.title("Mkce")
#s.iconbitmap("logo.ico")

s.configure(bg='#E9EDEC')
s.geometry("1550x800")

print(s.winfo_height())
print(s.winfo_width())

'''img = PhotoImage(file="C:\\Users\\test\\Downloads\\img.png")
img_lab=Label(s,image=img)
img_lab.place(x=20,y=0)'''
img = Image.open("C:\\Users\\test\\Downloads\\mkce3.png")
img_3 = img.resize((1350,800), Image.ANTIALIAS)
img_4= ImageTk.PhotoImage(img_3)


log_img_1= Image.open("C:\\Users\\test\\Downloads\\img.png")
img_5 = log_img_1.resize((1550, 800), Image.ANTIALIAS)
new_6 = ImageTk.PhotoImage(img_5)

home_img = Image.open("C:\\Users\\test\\Downloads\\mkce2.png")
img_2 = home_img.resize((1270, 700), Image.ANTIALIAS)
home_new = ImageTk.PhotoImage(img_2)

log_img = Image.open("C:\\Users\\test\\Downloads\\home1.png")
img_1 = log_img.resize((1550, 800), Image.ANTIALIAS)
new = ImageTk.PhotoImage(img_1)


bglab=Label(s,image=new)
bglab.place(x=0,y=0)
global new_1,stu
name=Label(s,text="M.KUMARASAMY COLLEGE OF ENGINEERING",font=("Times New Roman",32),bg="#26668B",fg="white")
name.place(x=200,y=1)

fac_img= Image.open("C:\\Users\\test\\Downloads\\fac.png")
re_reg = fac_img.resize((200,200),Image.ANTIALIAS)
new_1= ImageTk.PhotoImage(re_reg)
teacher_login=Button(s,image=new_1,command=faculty)
teacher_login.place(x=350,y=400)
fac_lab=Label(s,text="FACULTY LOGIN",font=("Times New Roman",20),bg="#60B1C6")
fac_lab.place(x=350,y=300)

stu_lab=Label(s,text="STUDENT LOGIN",font=("Times New Roman",20),bg="#60B1C6")
stu_lab.place(x=720,y=300)
stu_img= Image.open("C:\\Users\\test\\Downloads\\images.png")
stu_reg = stu_img.resize((200,200),Image.ANTIALIAS)
stu= ImageTk.PhotoImage(stu_reg)
student_login=Button(s,image=stu)
student_login.place(x=720,y=400)





s.mainloop()
