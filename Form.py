from ast import Pass, main
import re
from textwrap import fill
from tkinter import*
from tkinter import colorchooser
from tkinter import messagebox
from tkinter.tix import MAIN
import tkinter.messagebox as tmsg

root = Tk()
root.title('Fill-Up Form')
root.geometry('450x650')
root.resizable(width=False, height=False)
root.config(bg='white')
root.iconbitmap("./form.ico")


def get_input():
    first_var = first.get()
    mid_var = mid.get()
    last_var = last.get()
    name = (f"{first_var} {mid_var} {last_var}")
    name = name.upper()
    phone_var = phone.get()
    if v.get() == 1:
        radio_var = "YES, Already Visited"
    else:
        radio_var = "NO, Never Visited"
    value = symptoms_entry.get(1.0, 'end-1c')
    value = value.upper()
    preMed = prev_med_entry.get("1.0", "end-1c")
    preMed = preMed.upper()
    CurrMed = curr_med_entry.get("1.0", "end-1c")
    CurrMed = CurrMed.upper()
    reqDoc_var = reqDoc.get()
    reqDoc_var = reqDoc_var.upper()

    with open("./data.txt", "a") as data:
        data.write(f"\nNAME:- {name}\nPHONE NUMBER:- {phone_var}\n{radio_var}\nSYMPTOMS:- {value}\nPREVIOUS TREATMENT:- {preMed}\nCURRENTLY CONSUMING MEDICINE:- {CurrMed}\nREQUIRED CONSULTANT:- {reqDoc_var}\n")

    tmsg.showinfo("Thank You", "Submitted Successfully!")
    first.set("")
    mid.set("")
    last.set("")
    phone.set("")
    v.set(0)
    symptoms_entry.delete(1.0, 'end-1c')
    prev_med_entry.delete(1.0, 'end-1c')
    curr_med_entry.delete(1.0, 'end-1c')
    reqDoc.set("")


def click(event):
    pass


first = StringVar()
mid = StringVar()
last = StringVar()

frame1 = Frame(root, bg='#00cbb3', pady=10).place(x=0, y=10)
Label(frame1, text='Patient\'s Information', font='CooperBlack 13 bold',
      bg='#00cbb3', foreground='white').pack(fill=X, ipady=7)
app_det = Label(root, text='Appointment Details', font='CooperBlack 13 bold',
                bg='#00cbb3', foreground='white').place(x=0, y=250, width=450, height=37)

first_name = Label(text='First Name ', font='TimesNewRoman 9',
                   pady=2, bg='white').place(x=10, y=50)
entry_name = Entry(textvariable=first, highlightthickness=0.5,
                   highlightbackground='#00cbb3').place(height=27, x=10, y=73)

mid_name = Label(text='Middle Initial', font='TimesNewRoman 9',
                 pady=2, bg='white').place(x=170, y=50)
entry_mid = Entry(textvariable=mid, highlightthickness=0.5,
                  highlightbackground='#00cbb3', width=9, ).place(height=27, x=170, y=73)

last_name = Label(text='Last Name ', font='TimesNewRoman 9',
                  pady=2, bg='white').place(x=300, y=50)
entry_last = Entry(textvariable=last, highlightthickness=0.5,
                   highlightbackground='#00cbb3').place(height=27, x=300, y=73)

phone = StringVar()
phone_no = Label(text='Phone Number ', font='TimesNewRoman 9',
                 pady=2, bg='white').place(x=10, y=120)
entry_phone = Entry(textvariable=phone, highlightthickness=0.5,
                    highlightbackground='#00cbb3').place(height=27, x=10, y=143)

v = IntVar()
Label(text='Is This Your First Visit To Our Clinic?',
      bg='white').place(x=10, y=190)
r1 = Radiobutton(bg='white', text='YES', value=1, variable=v,
                 font='TimesNewRoman 8').place(x=10, y=210)
r2 = Radiobutton(bg='white', text='NO', value=2, variable=v,
                 font='TimesNewRoman 8').place(x=70, y=210)

symptoms = Label(root, text='Symptoms', font='TimesNewRoman 9',
                 pady=2, bg='white').place(x=10, y=300)
symptoms_entry = Text(highlightthickness=0.5,
                      highlightbackground='#00cbb3', width=40, height=4)
symptoms_entry.place(x=10, y=320)

prev_med = Label(root, text='Previous Treatment',
                 font='TimesNewRoman 9', pady=2, bg='white').place(x=10, y=395)
prev_med_entry = Text(highlightthickness=0.5,
                      highlightbackground='#00cbb3', width=40, height=2)
prev_med_entry.place(x=10, y=415)

curr_med = Label(root, text='Currently Consuming Medicine',
                 font='TimesNewRoman 9', pady=2, bg='white').place(x=10, y=460)
curr_med_entry = Text(highlightthickness=0.5,
                      highlightbackground='#00cbb3', width=40, height=2)
curr_med_entry.place(x=10, y=480)

reqDoc = StringVar()
req_doc = Label(root, text='Required Consultant',
                font='TimesNewRoman 9', pady=2, bg='white').place(x=10, y=525)
req_doc_entry = Entry(textvariable=reqDoc, highlightthickness=0.5,
                      highlightbackground='#00cbb3').place(height=27, x=10, y=545)

submit = Button(command=get_input, text='Submit', font='TimesNewRoman 9 bold', relief='flat',
                foreground='white', bg='#00cbb3', activebackground='#00cbb3', activeforeground='white', width=10, height=1)
submit.place(x=145, y=600)
submit.bind("<ButtonRelease-1>", click)
quit_butt = Button(text='Quit', font='TimesNewRoman 9 bold', relief='flat', foreground='white',
                   bg='#00cbb3', activebackground='#00cbb3', activeforeground='white', width=10, height=1)
quit_butt.place(x=235, y=600)
quit_butt.bind("<ButtonRelease-1>", quit)

root.mainloop()
