class catalog:
    
    lista_obiecte=[]
    clasa = ""
    subclasa = ""
    nume_producator = "" 
    subclasa_cautata = "" 

    def __init__ (self):

        catalog.lista_obiecte.append(self)
        self.pret = int(input("Dati pret: ")) 
        self.consum = int(input("Dati consum: ")) 
        self.producator = input("Dati producator: ") 
        self.cod_produs = int(input("Dati cod produs: "))
        
    def sortare_dupa_pret(self):

        for object in sorted (catalog.lista_obiecte,key=lambda obj:obj.pret):
            print("pret: ",object.pret,"cod: ",object.cod_produs)

    def sortare_dupa_consum(self):

        for object in sorted (catalog.lista_obiecte,key=lambda obj:obj.consum):
            print("consum: ",object.consum,"cod: ",object.cod_produs)

    def cauta_dupa_producator(self):

        for object in catalog.lista_obiecte:
            if object.producator == nume_producator:
                print("producator: ",object.producator,"subclasa: ",object.subclasa,"cod: ",object.cod_produs)

    def afisare_dupa_subclasa(self):
  
        for object in catalog.lista_obiecte:
            if object.subclasa == subclasa_cautata:
                print("subclasa: ",object.subclasa,"cod: ",object.cod_produs)
        


class Electrocasnice_mari(catalog):

    clasa = "Electrocasnice mari"
    
    def __init__(self):
        
        catalog.__init__(self)
        self.adancime = int(input("Dati adancimea: "))
        self.latime = int(input("Dati latimea: "))
        self.inaltime = int(input("Dati inaltimea: "))
        

class Electrocasnice_mici(catalog):

    clasa = "Electrocasnice mici"

    def __init__(self):
        
        catalog.__init__ (self)
        self.lungime_cablu = input("Dati lungime cablu: ")
        self.baterie = input("Dati baterie: ")
        


class Frigider(Electrocasnice_mari):

    subclasa = "Frigider"
    
    def __init__(self,capacitate_congelator,capacitate_frigider):
        
        Electrocasnice_mari.__init__(self)
        self.capacitate_congelator = capacitate_congelator  
        self.capacitate_frigider = capacitate_frigider
        
print("Obiectul 1:")
obiect1 = Frigider("5 litrii","10 litrii")
print("Obiectul 2:")
obiect2 = Frigider("3 litrii","7 litrii")

class Aragaz(Electrocasnice_mari):

    subclasa = "Aragaz"

    def __init__(self,nr_arzatoare):
        
        Electrocasnice_mari.__init__(self)
        self.nr_arzatoare = nr_arzatoare
        
print("Obiectul 3:")
obiect3 = Aragaz(4)
print("Obiectul 4:")
obiect4 = Aragaz(2)

class Mixer(Electrocasnice_mici):

    subclasa = "Mixer"

    def __init__(self,rotatii_min):
        
        Electrocasnice_mici.__init__(self)
        self.rotatii_min = rotatii_min   

print("Obiectul 5:")
obiect5 = Mixer(200)
print("Obiectul 6:")
obiect6 = Mixer(500)

class Fier_Calcat(Electrocasnice_mici):

    subclasa = "Fier_calcat"

    def __init__(self,rezervor):
        
        Electrocasnice_mici.__init__(self)
        self.rezervor = rezervor   

print("Obiectul 7:")
obiect7 = Fier_Calcat("200 ml")
print("Obiectul 8:")
obiect8 = Fier_Calcat("500 ml")


print("Sortate dupa pret: ")
obiect1.sortare_dupa_pret()
print("Sortate dupa consum: ")
obiect3.sortare_dupa_consum()
print("Sortate dupa producator: ")
nume_producator = input("Dati nume producator: ")
obiect4.cauta_dupa_producator()
subclasa_cautata = input("Dati subclasa: ")
print("Afisate dupa subclasa: ")
obiect5.afisare_dupa_subclasa()
