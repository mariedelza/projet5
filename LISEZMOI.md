## tittre
Développer une application de Gestion de budget en Python(Application console).

## Description

Le projet consiste à mettre en place une application(console) de Gestion de budget.

La plateforme doit permettre une personne:

- D'enregistrer ses dépenses

- D'enregistrer ses revenus

- De voir l'écart qui est entre ses dépenses et ses revenus.
## Les pré-requis
tout d'abord installer visuel studio code et python3 , ensuite installer db browser for sqlite ou tinydb pour les systemes de bases de donnees et l'implementation des differents table cree.
## guide d’installation
pour installer db browser sur linux taper les commandes suivant:
D'abord ouvrir le terminal et mettre la commande suivant:

$ sudo apt update (pour la mise a jour des packages )
$ sudo apt install sqlite3 (installation de sqlite3)
$ sqlite3 --version (pour verifier la version installer)
$ sudo apt install sqlitebrowser (installation de dbbrowser)

## guide d’utilisation :
import sqlite3 permet d'importer sqlite 3
conn=sqlite3.connect('nom de la base de donnees.db') permet la creation de la base de donnees 
cursor=conn.cursor() est une variable qui permet de se connecter a la base de donnees
cursor.execute() permet d'executer la requete demandee
conn.commit() permet de retourner les modifications
conn.close() permet de fermer la connexion

Tout d'abord creer un dossier vide dans votre bureau ,ensuite ouvrir votre dossier avec vs code supposant que python3 est dejas installer sur votre machine .Ensuite creer un fichier python nom.py et importer sqlite 3.Creer votre base de donnees .ensuite ouvrir db browser for sqlite cliquer sur ouvrir une nouvelle base de donnees pour ouvrir votre base de donnees creer.Et par la suite on peut commencer a creer nos differents table par les requetes sql.


## roadmap
nous pensons ameliorer ce projet dans un futur proche .






