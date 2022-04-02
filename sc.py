import classe

class SousCompte(classe.Compte):
    def __init__(self,nom, solde,numero,numerocompteparent, pourcentage):
        super().__init__(nom,solde,numero)
        self.numerocompteparent=numerocompteparent
        self.pourcentage = pourcentage

    def __repr__(self):
        return "Compte : {} , avec un solde de : {},      N°{} , avec comme parent le numéro de compte :  {} et représente :  {}% du compte Principal\n".format(self.nom, self.solde, self.numero, self.numerocompteparent, self.pourcentage)
    def getpourcentage(self):
        return self.pourcentage