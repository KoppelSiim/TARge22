

def nimi():
    nimi = input("sisesta nimi ")
    print("Tere", nimi)
    print(f"Tere {nimi}")

def lahuta():
    arv1 = float(input("Sisesta palun esimene arv "))
    arv2 = float(input("Sisesta palun teine arv "))
    summa = arv1-arv2
    print(f"Summa on {summa}")
    print("Summa on", summa)
    print("Summa on", arv1+arv2)
    print(f"{arv1} - {arv2} on {summa}")
    print("tore")

if __name__ == "__main__":
    #nimi()
    lahuta()
    

    