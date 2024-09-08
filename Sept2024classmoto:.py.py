class moto:
    def __init__ (self, marque, modele, annee, vitesse, moteur_en_marche):
        self.marque = marque
        self.modele = modele
        self.annee = int(annee)
        self.vitesse = float(vitesse)
        self.moteur_en_marche = False

    def __str__ (self):
        return f"Marque : {self.marque} \n Modèle : {self.modele} \n Année : {self.annee} \n Vitesse : {self.vitesse} \n Moteur en marche : {self.moteur_en_marche}"
    
    def demarrer(self):
        self.moteur_en_marche = True
        return self.moteur_en_marche
    
    def arreter(self):
        self.moteur_en_marche = False
        return self.moteur_en_marche
    
    def accelerer(self, vit):
        if self.moteur_en_marche == True:
            self.vitesse += vit
            return self.vitesse
        return "Le moteur est éteint"
    
    def freiner(self, vit):
        if self.moteur_en_marche == True:
            self.vitesse -= vit
            return self.vitesse
        return "Le moteur est éteint"
    
    




