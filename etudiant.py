class Etudiant:
    def __init__(self,nom,noteUn,noteDeux):
        self.nom = nom
        self.noteUn = noteUn
        self.noteDeux = noteDeux

    def calculer_note_moyenne(self,noteUn,noteDeux):
        self.noteUn = noteUn
        self.noteDeux = noteDeux
        notes_liste = [noteUn,noteDeux]
        somme = sum(notes_liste)
        moyenne = somme/2
        return moyenne 
    def afficher_nom_moyenne(self,nom,moyenne):
        self.nom = nom
        self.moyenne = moyenne
        afficher_nom_moyenne=f"L'etudiant {nom} a eu comme moyenne {moyenne}"
        print(afficher_nom_moyenne)
nom = input("Entrer le nom de l etudiant: ")
noteUn = float(input("Enter la note Un: "))
noteDeux = float(input("Entrer la note Deux: "))

moyenne = Etudiant(nom,noteUn,noteDeux)
calcul_moyenne = moyenne.calculer_note_moyenne(noteUn,noteDeux)

afficher = Etudiant(nom,noteUn,noteDeux)
afficher.afficher_nom_moyenne(nom,calcul_moyenne)