
import csv
class BloodData:
    def __init__(self,CBC, Gender, Normalvalues, lessObserv, moreObserv):
        self.CBC = CBC
        self.Gender = Gender
        self.Normalvalues = Normalvalues
        self.lessObserv = lessObserv
        self.moreObserv = moreObserv

    def blooddataCSV(self):
        return "'{}','{}', '{}', '{}','{}'\n".format(self.CBC,self.Gender,self.Normalvalues,self.lessObserv,self.moreObserv)

reply = "yes"
while reply == "yes":
    CBC = input("Enter the CBC:")
    Gender = input("Enter the Gender:")
    Normalvalues = input("Enter the Normalvalues:")
    lessObserv = input("Enter the lessObserv:")
    moreObserv = input("Enter the moreObserv:")

    oRef = BloodData(CBC, Gender,Normalvalues, lessObserv, moreObserv)
    reply = input("Would you like enter another record:")

    file = open("BloodData.csv","a")
    file.write(oRef.blooddataCSV())