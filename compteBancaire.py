class Account:
    def __init__(self,solde_initial=0):
        self.solde_initial = solde_initial
        self.solde_actuel = solde_initial
    def getBalance(self):
        return self.solde_actuel
    def deposer(self,montant_deposer):
        self.solde_actuel = self.solde_actuel+montant_deposer
    def retirer(self,montant_retirer):
        self.solde_actuel = self.solde_actuel-montant_retirer
    def ajout_interet(self,taux_interet):
        self.solde_actuel = self.solde_actuel*(1+taux_interet)
account1 = Account()
account1.deposer(200)
account1.retirer(50)
account1.ajout_interet(5)
print(account1.getBalance())
