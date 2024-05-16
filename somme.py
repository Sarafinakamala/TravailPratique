class Somme:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def somme(self,n1,n2):
        reponse = n1 + n2
        return reponse

nombreUn = int(input("Entrer le nombre Un: "))
nombreDeux = int(input("Entrer le nombre deux: "))

sommeUn = Somme(nombreUn,nombreDeux)

print(f"La somme de {nombreUn} et {nombreDeux} donne {sommeUn.Somme(nombreUn,nombreDeux)}")
