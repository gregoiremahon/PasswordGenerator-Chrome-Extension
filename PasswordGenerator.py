#gregoiremahon 2022/03/30

# Importing dependencies

from ast import Pass
from curses import BUTTON2_CLICKED
from itertools import count
import random
from string import *
import tkinter as tk

ValMin = int 
ValMax = int
Password = ''


PasswordSizeWindow = tk.Tk()
PasswordWindow = tk.Tk()
PasswordWindow.title("Password Generator")
label = tk.Label(PasswordSizeWindow, text="Bienvenue dans Password Generator. Entrez la taille souhaitée de votre mot de passe (entre 1 et 99)\n github.com/gregoiremahon")
label.pack()
PasswordSizeWindow.geometry("800x300")
PasswordWindow.geometry("800x300")
PasswordWindow.withdraw()
PasswordSizeWindow.title("Sélectionnez la taille de votre mot de passe")
def getEntryMin():
    global ValMin
    ValMin = myEntry1.get()
    
myEntry1 = tk.Entry(PasswordSizeWindow, width=40)
myEntry1.pack(pady=20)
valeur=myEntry1
btn1 = tk.Button(PasswordSizeWindow, height=2, width=30, text="Valider la taille minimale", command=getEntryMin)
btn1.pack()

def getEntryMax():
    global ValMax
    ValMax = int(myEntry2.get())

myEntry2 = tk.Entry(PasswordSizeWindow, width=40)
myEntry2.pack(pady=20)
btn2= tk.Button(PasswordSizeWindow, height=2, width=30, text="Valider la taille maximale", command=getEntryMax)
btn2.pack()


def closeWindow():
    PasswordSizeWindow.destroy()
    MinLength = int(ValMin)
    MaxLength = int(ValMax)
    print("valmin", MinLength)
    print("valmax", MaxLength)

    
    
    if(MinLength == MaxLength):
        PassLength = MinLength
    else:
        PassLength = random.randrange(MinLength, MaxLength, 2)
    Alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[]^_`{|}~tnrx0bx0c"

    PasswordChar = random.sample(Alphabet, PassLength)
    Password="".join(PasswordChar)


    PassSize = ("Votre mot de passe de %s" %PassLength)
    PassInfo = (" caractères est :\n{}".format(Password))
    VarPass = (PassSize,PassInfo)
    PasswordFinal ="".join(VarPass)
    PrintingPassword = tk.Label(PasswordWindow, text=PasswordFinal)
    PrintingPassword.pack()
    PasswordWindow.deiconify()

    PasswordWindow.mainloop()

btn3= tk.Button(PasswordSizeWindow,text= 'Créer le mot de passe', command = closeWindow)
btn3.pack()

PasswordSizeWindow.mainloop()