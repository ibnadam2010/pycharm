from tkinter import ttk
from tkinter import *
from  tkinter import messagebox
import sqlite3
import mysql.connector
from mysql.connector import errorcode

#methodes
print("ss")

def FieldInit():
    entrernom.focus()


#Inserer Data
def Ajouter():
    nom = entrernom.get()
    prenom = entrerprenom.get()
    age = entrerage.get()
    adresse = entreradresse.get()

    cnx = mysql.connector.connect(user='root', password='',
                                 host='127.0.0.1',
                                 database='pycharm-crud')
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO `membre` (`matricule`, `nom`, `prenom`, `age`, `adresse`) VALUES (NULL,"+"'"+nom+"',"+"'"+prenom+"', "+"'"+age+"', "+"'"+adresse+"')")
    cnx.commit()
    cnx.close()
    messagebox.showinfo("Confirmation","informations enregistées avec succès")

    entrernom.delete(0,'end')
    entrerprenom.delete(0,'end')
    entrerage.delete(0,'end')
    entreradresse.delete(0,'end')
    entrernom.focus()

    #Afficher dans le tableau
    cnx = mysql.connector.connect(user='root', password='',
                                 host='127.0.0.1',
                                 database='pycharm-crud')
    cursor = cnx.cursor()
    cursor.execute("select * from membre order by matricule desc")
    select=cursor.fetchall()
    select = list(select)
    table.insert('', END, value=select[0])




#titre general window
fenetre = Tk()
fenetre.title("Gestion des inscriptions")
fenetre.geometry("1200x680+70+0")
fenetre.configure(background ="#e9e9e9")

#Menu


#Ajouter le titre specifique window
lbtitre = Label(fenetre, text ="GESTION DES PLANNING", bg="white", fg="red", font= ("Arial",15))
lbtitre.place(x=0,y=0,width=1250)

#Ajouter les champs de saisie
lblnom = Label(fenetre, text = "Nom :", font =("Arial", 16), bg = "#e9e9e9", fg = "black" )
lblnom.place(x = 0, y = 80, width = 150 )
entrernom = Entry(fenetre)
entrernom.place(x = 50, y = 120, width = 200, height=30)
entrernom.focus()

lblprenom = Label(fenetre, text = "Prénom :", font =("Arial", 16), bg = "#e9e9e9", fg = "black" )
lblprenom.place(x = 300, y = 80, width = 200 )
entrerprenom = Entry(fenetre)
entrerprenom.place(x = 360, y = 120, width = 200, height=30)

lblage = Label(fenetre, text = "Age :", font =("Arial", 16), bg = "#e9e9e9", fg = "black" )
lblage.place(x = 570, y = 80, width = 200 )
entrerage = Entry(fenetre)
entrerage.place(x = 650, y = 120, width = 200, height=30)

lbladresse = Label(fenetre, text = "Adresse :", font =("Arial", 16), bg = "#e9e9e9", fg = "black" )
lbladresse.place(x = 890, y = 80, width = 200 )
entreradresse = Entry(fenetre, font=("Georgia",16))
entreradresse.place(x = 945, y = 120, width = 200, height=30)

#Bouton Valider
btnsave = Button(fenetre, text = "Valider", font = ("Arial", 16), bg = "blue", fg = "white", command=Ajouter)
btnsave.place(x=200, y = 200, width = 200)

#Bouton Modifier
btnedit = Button(fenetre, text = "Modifier", font = ("Arial", 16), bg = "blue", fg = "white")
btnedit.place(x=450, y = 200, width = 200)

#Boutons supprimier
btndelete = Button(fenetre, text = "Supprimer", font = ("Arial", 16), bg = "red", fg = "white")
btndelete.place(x=700, y = 200, width = 200)

#Ajouter un tableau
table = ttk.Treeview(fenetre, columns = (1, 2, 3, 4, 5), height = 5, show = "headings")
table.place(x = 50, y = 300, width = 1100, height = 400)
table.heading(1, text = "CODE")
table.heading(2, text = "NOM")
table.heading(3, text = "PRENOM")
table.heading(4, text = "AGE")
table.heading(5, text = "ADRESSE")


table.column(1, width = 50)
table.column(2, width = 150)
table.column(3, width = 150,)
table.column(4, width = 50)
table.column(5, width = 150)


cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='pycharm-crud')
curseur = cnx.cursor()
curseur.execute("select * from membre")
lignes = curseur.fetchall()
for ligne in lignes:
    table.insert('', END, value=ligne)
    cnx.close
fenetre.mainloop()
