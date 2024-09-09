class moto:
    def __init__ (self, marque, modele, annee, vitesse, moteur_en_marche):
        self.marque = marque
        self.modele = modele
        self.annee = int(annee)
        self.vitesse = float(vitesse)
        self.moteur_en_marche = False

    def __str__ (self):
        """Prints out all info on chosen motorbike"""
        return f"Marque : {self.marque} \n Modèle : {self.modele} \n Année : {self.annee} \n Vitesse : {self.vitesse} \n Moteur en marche : {self.moteur_en_marche}"
    
    def demarrer(self):
        """Makes var be true"""
        self.moteur_en_marche = True
        return self.moteur_en_marche
    
    def arreter(self):
        """Makes var be false"""
        self.moteur_en_marche = False
        return self.moteur_en_marche
    
    def accelerer(self, vit):
        """Checks veracity of moteur_en_marche = True and adds user input speed onto current speed"""
        if self.moteur_en_marche == True:
            self.vitesse += vit
            return self.vitesse
        return "Le moteur est éteint"             
    
    def freiner(self, vit):
        """Checks veracity of moteur_en_marche = True and subtracts user input speed onto current speed"""
        if self.moteur_en_marche == True:
            self.vitesse -= vit
            return self.vitesse
        return "Le moteur est éteint"
    print(help(accelerer))
    def __repr__ (self):
        return "moto(\""+self.marque +"\")"
    

moto1 = moto("Yamaha", "Raider", 1982)
    



