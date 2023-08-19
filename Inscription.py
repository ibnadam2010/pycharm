from tkinter import ttk
from tkinter import *
from  tkinter import messagebox
import sqlite3

#titre general window
fenetre = Tk()
fenetre.title("Gestion des inscriptions")
fenetre.geometry("1200x680+70+0")
fenetre.configure(background ="#e9e9e9")

#Ajouter le titre specifique window
lbtitre = Label(fenetre, text ="GESTION DES PLANNING", bg="white", fg="red", font= ("Arial",15))
lbtitre.place(x=0,y=0,width=1250)

#Ajouter les champs de saisie
lblnom = Label(fenetre, text = "Nom :", font =("Arial", 16), bg = "#e9e9e9", fg = "black" )
lblnom.place(x = 30, y = 80, width = 200 )
entrernom = Entry(fenetre)
entrernom.place(x = 100, y = 120, width = 200, height=30)

lblprenom = Label(fenetre, text = "Prénom :", font =("Arial", 16), bg = "#e9e9e9", fg = "black" )
lblprenom.place(x = 340, y = 80, width = 200 )
entrerprenom = Entry(fenetre)
entrerprenom.place(x = 400, y = 120, width = 200, height=30)

lblage = Label(fenetre, text = "Age :", font =("Arial", 16), bg = "#e9e9e9", fg = "black" )
lblage.place(x = 620, y = 80, width = 200 )
entrerage = Entry(fenetre)
entrerage.place(x = 700, y = 120, width = 200, height=30)

lbladresse = Label(fenetre, text = "Adresse :", font =("Arial", 16), bg = "#e9e9e9", fg = "black" )
lbladresse.place(x = 930, y = 80, width = 200 )
entreradresse = Entry(fenetre, font=("Georgia",16))
entreradresse.place(x = 985, y = 120, width = 200, height=30)

#Ajouter un tableau
table = ttk.Treeview(fenetre, columns = (1, 2, 3, 4, 5, 6, 7), height = 5, show = "headings")
table.place(x = 100, y = 300, width = 1000, height = 400)
table.heading(1, text = "CODE")
table.heading(2, text = "NOM")
table.heading(3, text = "PRENOM")
table.heading(4, text = "AGE")
table.heading(5, text = "ADRESSE")
table.heading(6, text = "TELEPHONE")
table.heading(7, text = "REMARQUE")

table.column(1, width = 50)
table.column(2, width = 150)
table.column(3, width = 150)
table.column(4, width = 50)
table.column(5, width = 150)
table.column(6, width = 150)
table.column(7, width = 150)

fenetre.mainloop()
