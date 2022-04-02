class Compte:
    def __init__(self, nom, solde, numero):
        self.nom = nom
        self.solde = solde
        self.numero = numero
        self.numerocompteparent = -1
        self.pourcentagerestant = 100
    def __repr__(self):
        return "Compte : {} , avec un solde de : {},      N°{} , avec {}% restant\n".format(self.nom, self.solde, self.numero, self.pourcentagerestant)
    def getnumerocompteparent(self):
        return self.numerocompteparent
    def getnumero(self):
        return self.numero

    def getpourcentagerestant(self):
        return self.pourcentagerestant
    def getsolde(self):
        return self.solde
    def setsolde(self,nouveausolde):
        self.solde = nouveausolde
    def setpourcentagerestant(self,nouveau):
        self.pourcentagerestant = nouveau


