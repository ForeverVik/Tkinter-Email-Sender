import tkinter as tk
from tkinter import *
import smtplib
from email.message import EmailMessage

# Set Connection
port = 465

root = tk.Tk()
root.configure(bg="#FEFEFE")
root.title("Email Sender")

root.rowconfigure((0,1,2,3,4), weight=0)
root.columnconfigure((0,1), weight=0)

userTxt = tk.StringVar()
passTxt = tk.StringVar()
receiverTxt = tk.StringVar()
subjectTxt = tk.StringVar()
msgTxt = tk.StringVar()

def setEmailInfo():
    Label(text="Username:", width=10).grid(row=0, column=0)
    Label(text="Password:", width=10).grid(row=1, column=0)
    Label(text="Receiver Email:", width=10).grid(row=2, column=0)
    Label(text="Subject:", width=10).grid(row=3, column=0)
    Label(text="Message:", width=10).grid(row=4, column=0)

    userEntry = Entry(root, width=25, textvariable=userTxt).grid(row=0, column=1)
    passEntry = Entry(root, width=25, textvariable=passTxt).grid(row=1, column=1)
    receiverEntry = Entry(root, width=25, textvariable=receiverTxt).grid(row=2, column=1)
    subjectEntry = Entry(root, width=25, textvariable=subjectTxt).grid(row=3, column=1)
    msgEntry = Entry(root, width=50, textvariable=msgTxt).grid(row=4, column=1)

    uapBtn = Button(root, text="Send", width=25, command=emailSent).grid(row=5, column=1)

def emailSent():
    msg = EmailMessage()
    msg.set_content(msgTxt.get())
    msg["Subject"] = subjectTxt.get()
    msg["From"] = userTxt.get() + "@gmail.com"
    msg["To"] = receiverTxt.get()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
            server.login(userTxt.get(), passTxt.get())
            server.send_message(msg)
            server.quit()
        print("Email Sent")
    except Exception as e:
        print(e)

    quit()

setEmailInfo()

root.mainloop()
