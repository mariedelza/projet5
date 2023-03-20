import sqlite3
#creation de la base de donnees nommee myDB.db
conn = sqlite3.connect('marieDB.db')
#creation de la table depense et demande d'information concernant les attributs
cur = conn.cursor()

hab=int(input("donner la depense de l'habilement"))
loy = int(input("donner la depense du loyer"))
man = int(input("donner la depense de la nourriture"))
trans = int(input("donner la depense du transport"))
loi = int(input("donner la depense des loisirs"))
req="CREATE TABLE depense_personne(id integer primary key , habilement numeric, loyer numeric, manger numeric, transport numeric, loisirs numeric)"
req ="insert into depense_personnel(habilement,loyer,manger,transport,loisirs) values (?,?,?,?,?)"
#execution de la requete
cur.execute(req, (hab, loy, man,trans, loi))
conn.commit()
# calcul du depense total
total_depense = hab+loy+man+trans+loi

print("vous avez depensez au total:"+str(total_depense)+"fcfa")
if total_depense > 500000:
  print("Attention vous avez trop depensez ce mois !!!")
else:
 print("votre depense est a la normale")

# #envoie la requete a la connexion ou valider les modifications
conn.commit()
   
# #creation de la table revenu
sa=int(input("quel est votre salaire? "))
bus=int(input("quels sont vos revenus en busness? "))
pen=int(input("quel est la somme de votre pension ? "))
all=int(input("quel est la somme de votre allocation social? "))
loy=int(input("quels sont les revenues du loyer?"))
#creation de la table revenu et ces attributs
req1="CREATE TABLE revenu (id integer primary key ,salaire numeric, busness numeric, pension numeric,allocation_social numeric,loyer numeric)"
req1 = "insert into revenu(salaire, busness, pension, allocation_social, loyer) values (?,?,?,?,?)"
#  #execution de la requete 1   
cur.execute(req1,(sa,bus,pen,all,loy))
conn.commit()
#calcul du revenu total
total_revenu=sa+bus+pen+all+loy

print("la somme de vos revenue est: " +str(total_revenu)+ "fcfa")
# #condition sur la revenu
if total_revenu > total_depense:
 print("vous pouvez augmenter vos depenses pour plus de revenus merci!!")
else:
 print("reduisez vos depenses svp vous avez trop depenser cette fois ci !!!") 
conn.commit()

# calcul de l'ecart
if total_depense < total_revenu:
    ecart = total_revenu-total_depense
    print("l'ecart entre les depenses et les revenus est :"+str(ecart)+"fcfa")
elif total_revenu < total_depense:
    ecart = total_depense-total_revenu
    print("l'ecart entre les depenses est :"+str(ecart)+"fcfa")
else:
    print("pas d'ecart entre les depenses et les revenues")

# print("l'ecart entre vos depense et revenus est estimee a :" + str(ecart) + "fcfa")

conn.commit()

# fermer la connexion
conn.close()

