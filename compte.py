

listedescomptes = []


def estceunnombre(element):
    while(element is not int):
        element = input("Entrez le nombre correct")
    return element

def creerCompte():
    nom = input("               Entrez le nom du compte -->")
    solde = int(input("         Entrez le solde de départ -->"))
    #solde = estceunnombre(solde)
    compte = { "nom":nom, "solde" : solde, "numero":len(listedescomptes), "numeroparent": -1 ,"type":"Principal" ,"pourcentagerestant": 100 }
    listedescomptes.append(compte)
    print('Votre compte a été crée' )

def selectionneruncompte():
    c = 0
    l =[]
    for item in listedescomptes:
        if item['type'] == "Principal":
            c += 1
            l.append(item['numero'])
            print("Compte : {} , avec un solde de : {},      N°{} \n".format(item['nom'],item['solde'],item['numero']))
    choix = int(input("     Entrez le numéro correspondant -->"))
    while(choix not in l or choix ):
        choix = int(input("     Entrez le numéro correspondant correct -->"))
    if (c == 0):
        choix = -1
    #choix = estceunnombre(choix)
    return int(choix)

def selectionnerunsouscompte():
    c = 0
    l =[]
    print("         Veuillez d'abord selectionner un sous compte")
    for item in listedescomptes:
        if item['type'] == "SousCompte":
            c+=1
            l.append(item['numero'])
            print("Compte : {} , avec un solde de : {},      N°{} \n".format(item['nom'],item['solde'],item['numero']))
    if(c!=0):
        choix = int(input("         Entrez le numéro correspondant -->"))
        while (choix not in l or choix):
            choix = int(input("     Entrez le numéro correspondant correct -->"))
    else:
        choix = -1
    #choix = estceunnombre(choix)
    return int(choix)


def affecterpourcentage(numerocompte):
    pourcent = int(input("Inserer un pourcentage à affecter à ce sous compte"))
    #pourcent = estceunnombre(pourcent)
    pourcentagerestant = int(listedescomptes[int(numerocompte)]['pourcentagerestant'])
    while(pourcent < 0 or pourcent > pourcentagerestant ):
        pourcent = int(input("Inserer un pourcentage à affecter à ce sous compte correct "))
    return int(pourcent)

def creerSousCompte():
    if(len(listedescomptes) != 0):
        print("Veuillez d'abord selectionner un compte !!")

        numerocompteparent = selectionneruncompte()
        nom = input("           Entrez le nom du sous compte -->")
        pourcentage = int(affecterpourcentage(numerocompteparent))
        pourcentag = (listedescomptes[int(numerocompteparent)]["solde"] * int(pourcentage)) / 100
        souscompte = {"nom": nom, "solde": pourcentag, "numero": len(listedescomptes), "numeroparent": numerocompteparent, "type": "SousCompte",
                      "pourcentage": pourcentage,"pourcentagerestant": 100}
        listedescomptes[int(numerocompteparent)]["pourcentagerestant"]=listedescomptes[int(numerocompteparent)]["pourcentagerestant"]-pourcentage
        print('Votre sous compte a été crée')
        listedescomptes.append(souscompte)
    else:
        print("vous devez d'abord créer un compte !!")


def Crediter( ):
    if (len(listedescomptes) != 0):
        numerodecompteselectionne = selectionneruncompte()
        montantCrediter = int(input("       Entrez le montant à ajouter du sous compte -->"))
        listedescomptes[numerodecompteselectionne]["solde"] = montantCrediter + listedescomptes[numerodecompteselectionne]["solde"]
        miseajour(numerodecompteselectionne, montantCrediter)
        print('Votre depôt en compte a été effectué avec succès')
    else:
        print("vous devez d'abord créer un compte")

def miseajour(numerocompte, montant):
    for item in listedescomptes:
        if item['numeroparent'] == numerocompte:
            item['solde'] = item['solde'] + (item['pourcentage']*montant)/100

def Debiter():
    numerosouscompteselectionne = selectionnerunsouscompte()
    if(numerosouscompteselectionne != -1):
        try:
            montantDebiter = int(input("        Entrez le montant à retirer du sous compte -->"))
        except:
            erreur()
        if(listedescomptes[numerosouscompteselectionne]["solde"] >= montantDebiter):
            listedescomptes[numerosouscompteselectionne]["solde"] =  listedescomptes[numerosouscompteselectionne]["solde"] - montantDebiter
            parentnumero =  listedescomptes[numerosouscompteselectionne]["numeroparent"]
            listedescomptes[parentnumero]['solde'] = listedescomptes[parentnumero]['solde'] - montantDebiter
            print('Votre retrait a été effectué avec succès')
        else: print("Solde Insuffisant pour effectuer l'opération")
    else:
        print('Aucun Sous Compte crée impossible de faire un retrait')

def estceunsouscompte(liste):
    if(liste["type"] == "Principal"):
        return 1
    else: return 0

def menu():
    print("--> --> -->       Bienvenue Choississez une opération !      <-- <-- <-- \n"
          "Créer un Compte :                1\n"
          "Créer un Sous-Compte :           2\n"
          "Effectuer un dépôt en compte :   3\n"
          "Effectuer un retrait en compte : 4\n"
          "Consulter mes Comptes :          5\n"
          "Supprimer un compte :            6\n"
          "Supprimer un sous compte :       7\n"
          "Quitter :                        8\n"
          )
def Consulter():
    if (len(listedescomptes) != 0):
        for item in listedescomptes:
            if item['type'] == "Principal":
                print("Compte : {} , avec un solde de : {},      N°{} , avec {}% restant\n".format(item['nom'], item['solde'], item['numero'], item['pourcentagerestant']))
            else:
                if item['type'] == "SousCompte":
                    print("             Sous Compte : {} , avec un solde de : {},      N°{}, du Compte parent N°{} \n".format(item['nom'], item['solde'], item['numero'],item['numeroparent']))
    else: print("Aucun Compte crée pour l'instant")

def Quitter():
    return 0
def choix():
    menu()
    choix = input('tapez ici -->')
    try:
        while int(choix) not in [1,2,3,4,5,6,7,8]:
            print("Entrez un numéro corrrect : ")
            choix = input()
    except :
        print("ERREUR entrez un élément correct!")
        choix = 0
        while int(choix) not in [1,2,3,4,5,6,7,8]:
            print("Entrez un numéro corrrect : ")
            choix = input()
    return int(choix)

def Supprimercompte():
    if (len(listedescomptes) != 0):
        numerodecompteselectionne = selectionneruncompte()
        listedescomptes.pop(numerodecompteselectionne)
        print('Compte supprimé avec succès ainsi que tous ses sous comptes')
        for item in listedescomptes:
            if(item['numeroparent'] == numerodecompteselectionne):
                listedescomptes.pop(item['numero'])
    else :
        print("vous devez d'abord créer un compte")

def erreur():
    print('Entrez des informations correctes')
def Supprimersouscompte():
    numerosouscompteselectionne = selectionnerunsouscompte()
    if (numerosouscompteselectionne != -1):
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




