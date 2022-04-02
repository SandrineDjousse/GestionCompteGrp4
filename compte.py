from classe import Compte
from sc import SousCompte
import pickle
import os


def enregistrer(objet):
    with open("fichier.txt","wb") as f:
        pi=pickle.Pickler(f)
        pi.dump(objet)

def recuperer(f):
    with open(f,"rb") as fic:
        pi =pickle.Unpickler(fic)
        object=pi.load()
        return object
# l=[]
# enregistrer(l)
listedescomptes = recuperer('fichier.txt')
def intec():
    try:
        nombre = input("         Entrez le montant à déposer -->")
        return int(nombre)
    except ValueError:
        print(f"{nombre} n'est pas un nombre.")
        return inte()


def creerCompte():
    nom = input("               Entrez le nom du compte -->")
    solde = intec()
    #solde = estceunnombre(solde)
    compte = Compte(nom,solde,len(listedescomptes))
    listedescomptes.append(compte)
    print('Votre compte a été crée' )

def selectionnerunsouscompte():
    c = 0
    l =[]
    print("         Veuillez d'abord selectionner un sous compte")
    for item in listedescomptes:
        if item.getnumerocompteparent() != -1:
            c+=1
            l.append(item.getnumero())
            print(item.__repr__())
    if(c!=0):
        choix = inte()
        while (choix not in l ):
            choix = int(input("     Entrez un numéro de compte présent dans la liste des choix -->"))
    else:
        choix = -1
    #choix = estceunnombre(choix)
    return int(choix)

def intep():
    try:
        nombre = input("Inserer un pourcentage à affecter à ce sous compte")
        return int(nombre)
    except ValueError:
        print(f"{nombre} n'est pas un nombre.")
        return inte()

def affecterpourcentage(numerocompte):
    pourcent = intep()
    #pourcent = estceunnombre(pourcent)
    pourcentagerestant = int(listedescomptes[int(numerocompte)].getpourcentagerestant())
    while(pourcent < 0 or pourcent > pourcentagerestant ):
        pourcent = intep()
    return int(pourcent)

def creerSousCompte():
    if(len(listedescomptes) != 0):
        print("Veuillez d'abord selectionner un compte !!")
        numerocompteparent = selectionneruncompte()
        nom = input("           Entrez le nom du sous compte -->")
        pourcentage = int(affecterpourcentage(numerocompteparent))
        solde = (listedescomptes[int(numerocompteparent)].getsolde() * int(pourcentage)) / 100
        souscompte = SousCompte(nom,solde,len(listedescomptes),numerocompteparent,pourcentage)
        listedescomptes[int(numerocompteparent)].setpourcentagerestant(listedescomptes[int(numerocompteparent)].getpourcentagerestant()-pourcentage)
        print('Votre sous compte a été crée')
        listedescomptes.append(souscompte)
    else:
        print("vous devez d'abord créer un compte !!")

def Crediter( ):
    if (len(listedescomptes) != 0):
        numerodecompteselectionne = selectionneruncompte()
        if(listedescomptes[numerodecompteselectionne].getpourcentagerestant()== 0):
            montantCrediter = intec()
            listedescomptes[numerodecompteselectionne].setsolde(montantCrediter + listedescomptes[numerodecompteselectionne].getsolde())
            miseajour(numerodecompteselectionne, montantCrediter)
            print('Votre depôt en compte a été effectué avec succès')
        else:
            print("Veuillez d'abord complètement partager votre compte en sous compte")
    else:
        print("vous devez d'abord créer un compte")

def intsec():
    try:
        nombre = input("     Entrez un numéro de compte présent dans la liste des choix -->")
        return int(nombre)
    except ValueError:
        print(f"{nombre} n'est pas un nombre.")
        return inte()

def selectionneruncompte():
    c = 0
    l =[]
    for Compte in listedescomptes:
        if Compte.getnumerocompteparent() == -1:
            c += 1
            l.append(Compte.getnumero())
            print(Compte.__repr__())
    choix = inte()
    while(choix not in l ):
        choix = intsec()
    if (c == 0):
        choix = -1
    #choix = estceunnombre(choix)
    return int(choix)
def miseajour(numerocompte, montant):
    for item in listedescomptes:
        if item.getnumerocompteparent() == numerocompte:
            item.setsolde(item.getsolde() + ((item.getpourcentage()*montant)/100))

def intde():
    try:
        nombre = input("        Entrez le montant à retirer du sous compte -->")
        return int(nombre)
    except ValueError:
        print(f"{nombre} n'est pas un nombre.")
        return inte()

def Debiter():
    numerosouscompteselectionne = selectionnerunsouscompte()
    if(numerosouscompteselectionne != -1):
        montantDebiter = intde()
        if(listedescomptes[numerosouscompteselectionne].getsolde() >= montantDebiter):
            listedescomptes[numerosouscompteselectionne].setsolde(listedescomptes[numerosouscompteselectionne].getsolde() - montantDebiter)
            parentnumero =  listedescomptes[numerosouscompteselectionne].getnumerocompteparent()
            listedescomptes[parentnumero].setsolde(listedescomptes[parentnumero].getsolde() - montantDebiter )
            print('Votre retrait a été effectué avec succès')
        else: print("Solde Insuffisant pour effectuer l'opération")
    else:
        print('Aucun Sous Compte crée impossible de faire un retrait')

def inte():
    #user_value = input("Enter an integer: ")
    try:
        nombre=input("     Entrez le numéro correspondant -->")
        return int(nombre)
    except ValueError:
        print(f"{nombre} n'est pas un nombre.")
        return inte()


def menu():
    print("--> --> -->       Bienvenue Choississez une opération !      <-- <-- <-- \n"
          "Créer un Compte :                --> 1\n"
          "Créer un Sous-Compte :           --> 2\n"
          "Effectuer un dépôt en compte :   --> 3\n"
          "Effectuer un retrait en compte : --> 4\n"
          "Consulter mes Comptes :          --> 5\n"
          "Supprimer un compte :            --> 6\n"
          "Supprimer un sous compte :       --> 7\n"
          "Quitter et Enrégistrer:          --> 8\n"
          )
def Consulter():
    if (len(listedescomptes) != 0):
        for Compte in listedescomptes:
            print(Compte.__repr__())
    else: print("Aucun Compte crée pour l'instant")

def Quitter():
    enregistrer(listedescomptes)
    return 0
def choix():
    menu()
    choix = input('tapez ici -->')
    try:
        while int(choix) not in [1,2,3,4,5,6,7,8]:
            print("Entrez un numéro corrrect : ")
            choix = inte()
    except :
        print("ERREUR entrez un élément correct!")
        choix = 0
        while int(choix) not in [1,2,3,4,5,6,7,8]:
            print("Entrez un numéro corrrect : ")
            choix = input()
    return int(choix)
def erase(element):
    for item in  reversed(listedescomptes):
        if (item.getnumerocompteparent() == element):
            listedescomptes.pop(item.getnumero())
def Supprimercompte():
    if (len(listedescomptes) != 0):
        numerodecompteselectionne = selectionneruncompte()
        print('Compte supprimé avec succès ainsi que tous ses sous comptes')
        erase(numerodecompteselectionne)
        listedescomptes.pop(numerodecompteselectionne)

    else :
        print("vous devez d'abord créer un compte")

def Supprimersouscompte():
    numerosouscompteselectionne = selectionnerunsouscompte()
    if (numerosouscompteselectionne != -1):
        numeroparent = listedescomptes[numerosouscompteselectionne].getnumerocompteparent()
        pourcentagerestant = listedescomptes[numeroparent].getpourcentagerestant() + listedescomptes[numerosouscompteselectionne].getpourcentage()
        listedescomptes[numeroparent].setpourcentagerestant(pourcentagerestant)
        listedescomptes.pop(numerosouscompteselectionne)
        print('Sous Compte supprimé avec succès')
    else:
        print('Créez avant tout un sous compte')

def traitement(choix):
    if(choix == 1 ):
        creerCompte()
    if (choix == 2):
        creerSousCompte()
    if (choix == 3):
            Crediter()
    if (choix == 4):
        Debiter()
    if (choix == 5):
            Consulter()
    if (choix == 6):
        Supprimercompte()
    if (choix == 7):
        Supprimersouscompte()
    if (choix == 8):
        Quitter()




