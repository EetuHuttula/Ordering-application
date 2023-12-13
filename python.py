from tuotteet import Ruokapaikka, ruokapaikat, Tuotteet, tuotteet
saldo = 100
def print_tuotteet():
    for tuote in tuotteet:
        print(f"Numero: {tuote.tuotenro}, Nimi: {tuote.nimi}, hinta: {tuote.hinta} €")

def get_tuotteet_by_id(tuotteet_list, target_id):
    return [tuote for tuote in tuotteet_list if tuote.id == target_id]

def uusi_saldo(saldo, ostos_hinta):
    return saldo - ostos_hinta

def vastaanotto(saldo):

    vastaus = input("Haluatko tilata ruokaa? (1 = kyllä, 2 = ei): ")
    
    if vastaus == "1":
        print("Vaihtoehdot")

        for paikka in ruokapaikat:
            print(f"Numero: {paikka.id} Nimi: {paikka.nimi}, Sijainti: {paikka.sijainti}")
        vastaus = input("Mistä tilataan? : ")

        if vastaus == "1":
            print_tuotteet()
            vastaus = input("Mikä tuote? : ")

            if vastaus in ["1", "2", "3"]:
                valittu_tuote = tuotteet[int(vastaus) - 1]
                print(f"Numero: {valittu_tuote.tuotenro} Nimi: {valittu_tuote.nimi}, Hinta: {valittu_tuote.hinta}")
                saldo = uusi_saldo(saldo, valittu_tuote.hinta)
                print(f"Uusi saldosi on maksun jälkeen {saldo} euroa.")

        if vastaus == "2":
            tuotteet_with_id_2 = get_tuotteet_by_id(tuotteet, "2")

            for tuote in tuotteet_with_id_2:
                print(f"Tuotenro: {tuote.tuotenro}, Nimi: {tuote.nimi}, Hinta: {tuote.hinta}")
            vastaus = input("Mikä tuote : ")

            if vastaus in ["1", "2", "3"]:
                valittu_tuote = tuotteet_with_id_2[int(vastaus) - 1]
                print(f"Numero: {valittu_tuote.tuotenro} Nimi: {valittu_tuote.nimi}, Hinta: {valittu_tuote.hinta}")
                saldo = uusi_saldo(saldo, valittu_tuote.hinta)
                print(f"Uusi saldosi on maksun jälkeen {saldo} euroa.")
    
        if vastaus == "3":
            tuotteet_with_id_3 = get_tuotteet_by_id(tuotteet, "3")
            
         
            for tuote in tuotteet_with_id_3:
                print(f"Tuotenro: {tuote.tuotenro}, Nimi: {tuote.nimi}, Hinta: {tuote.hinta}")

            vastaus = input("Mikä tuote : ")

            if vastaus in ["1", "2", "3"]:
                valittu_tuote = tuotteet_with_id_3[int(vastaus) - 1]
                print(f"Numero: {valittu_tuote.tuotenro} Nimi: {valittu_tuote.nimi}, Hinta: {valittu_tuote.hinta}")
                saldo = uusi_saldo(saldo, valittu_tuote.hinta)
                print(f"Uusi saldosi on maksun jälkeen {saldo} euroa.")


    elif vastaus == "2":
        print("palataan astialle")

saldo = 100
vastaanotto(saldo)