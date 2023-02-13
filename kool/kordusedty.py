import random

"""
Ülesanne 1
"""

def multiply():
    numbers = [1, 3, 6, 8, 7, 5, 2, 4, 9, 10]
    multiply = int(input("Sisesta tegur: "))
    for n in numbers:
        result = n * multiply
        print(f"{n} * {multiply} = {result}")

"""
Ülesanne 2
"""

def city():
    cities = ["Berliin", "Helsingi", "Rooma", "Pariis", "Viin", "Varssavi", "Tallinn", "Oslo", "Madriid", "Ateena"]
    for c in cities:
        print (c)
    cities.sort()
    city1 = input("Sisesta Euroopa pealinn: ").capitalize()
    city2 = input("Sisesta veel üks Euroopa pealinn: ").capitalize()
    cities.append(city1)
    cities.append(city2)
    cities.sort()
    for i in range(len(cities)):
        print(f"{i + 1}. {cities[i]}")
    print(f"Meie järjendis on {len(cities)} Euroopa pealinna.")

"""
Ülesanne 3
"""

def dictionary():
    number = [1, 2, 3, 4]
    estonian = ["üks", "kaks", "kolm", "neli"]
    english = ["one", "two", "three", "four"]
    italian = ["uno", "due", "tre", "quattro"]
    for i in range(len(number)):
        print(f"{number[i]} - {estonian[i]} - {english[i]} - {italian[i]}")
    number.append(5)
    number.append(6)
    estonian.append("viis")
    estonian.append("kuus")
    if "tre" in italian:
        print("Eksisteerib")
    else:
        print("Ei eksisteeri")
    number.sort()
    estonian.sort()
    english.sort()
    italian.sort()
    for element in number:
        print(element)
    print("\n")
    for element in estonian:
        print(element)
    print("\n")
    for element in english:
        print(element)
    print("\n")
    for element in italian:
        print(element)

"""
Ülesanne 4
"""

def magic():
    answers = ["Jah, kindlasti!", "See on kindlasti nii!", "Jah", "Kahtlemata nii.", "Võid selles kindel olla.",
             "Tõenäoliselt.", "Kõik märgid viitavad sellele.", "Võib-olla!", "Vastus on segane, küsi uuesti.",
             "Küsi hiljem uuesti.", "Parem on, kui ma ei ütle sulle seda.", "Ei oska hetkel öelda.","Keskendu ja küsi uuesti.",
             "Ei!", "Kahtlen selles.", "Mu allikad vastavad eitavalt.", "Mu vastus on Ei!", "Ma ei loodaks sellele."]
    print("Ma oskan tulevikku ennustada, lihtsalt sisesta oma küsimus ja sa saad vastuse."
              "\n(Kui soovid meie seanssi lõpetada, siis sisesta 'aitab') ")
    while True:
        ans = input("Sisesta küsimus: ")
        if ans == 'aitab':
            break
        randomnr = random.randint(0, len(answers)-1)
        print(answers[randomnr])
    print("Ma loodan, et need vastused olid Sulle kasulikud.")

"""
Ülesanne 5
"""

def wordsearch():
    words = ["ajukirurgia", "südamekirurgia","ratsionaalne arv","irratsionaalne arv", "sülearvuti", "lauaarvuti",
             "algkool", "põhikool", "keskkool", "ülikool", "kutsekool", "pastapliiats", "harilik pliiats"]
    word = input("Sisesta otsitav sõna: ")
    result = False
    for element in words:
        if word in element:
            result = True
            print(f"Jah, {element} sisaldab sõna {word}.")
    if not result:
        print("Otsing ei andnud tulemusi")


multiply()
city()
dictionary()
magic()
wordsearch()