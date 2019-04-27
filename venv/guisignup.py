from tkinter import *
import mysql.connector
class report:
    def __init__(self, Pid, Name, Phone, Age, Gender, Address, Username, Password):
        self.Pid = Pid
        self.Name = Name
        self.Phone = Phone
        self.Age = Age
        self.Gender = Gender
        self.Address = Address
        self.Username = Username
        self.Password = Password

    def showPatient(self):
        print("==", self.Pid, "|", self.Name, "==")
        print("Name", self.Name)
        print("Phone", self.Phone)
        print("Age", self.Age)
        print("Gender", self.Gender)
        print("Address", self.Address)
        print("Username", self.Username)
        print("Password", self.Password)
        print("==============")

def fetchreportFromDB():
    Username = entryUsername.get()
    sql = "select * from report where Username ='{}' ".format(Username)
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="patientdatabase")
    cursor = con.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    print(row)
    lab = Label(window, text=row)
    lab.place(relx=0.37, rely=0.7)


"""
    def fetchreportFromDB(Password):
        sql = "select * from report where Password ='{}'".format(Password)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="patientdatabase")
        cursor = con.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()
        print(row)

"""

window = Tk()
lblUsername = Label(window, text="Username")
lblUsername.grid(row=0)

entryUsername = Entry(window)
entryUsername.grid(row=0, column=1)

lblPassword = Label(window, text ="Password")
lblPassword.grid(row=1)

entryPassword = Entry(window)
entryPassword.grid(row=1, column=1)

btnLogin = Button(window, text="Button", command = fetchreportFromDB)
btnLogin.grid(row=2, column=1)


window.mainloop()

#fetchreportFromDB(Password)

