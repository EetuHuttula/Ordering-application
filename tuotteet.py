class Ruokapaikka:
    def __init__(self,id, nimi, sijanti):
        self.id = id
        self.nimi = nimi
        self.sijainti = sijanti
ruokapaikat = []

ruokapaikat.append(Ruokapaikka("1","Kotipizza", "Mäntylä"))
ruokapaikat.append(Ruokapaikka("2","Naantalin Aurinko", "Naantali"))
ruokapaikat.append(Ruokapaikka("3","Mcdonalds", "Haukipudas"))


class Tuotteet:
    def __init__(self, id, tuotenro, nimi, hinta: int):
        self.id = id
        self.tuotenro = tuotenro
        self.nimi = nimi
        self.hinta = hinta
    
tuotteet = []

tuotteet.append(Tuotteet("1", "1", "Opera Specialen", 12))
tuotteet.append(Tuotteet("1", "2", "Monster Haukipudas", 16))
tuotteet.append(Tuotteet("1", "3", "Ankkalankku", 15))

tuotteet.append(Tuotteet("2", "1", "Kanniaisen Ankka", 34))
tuotteet.append(Tuotteet("2", "2", "Petsamon Pässiä", 42))
tuotteet.append(Tuotteet("2", "3", "Makaronimössö", 10))

tuotteet.append(Tuotteet("3", "1", "Mccreamy", 12))
tuotteet.append(Tuotteet("3", "2", "Double qp", 13))
tuotteet.append(Tuotteet("3", "3", "Nuggets", 8))






