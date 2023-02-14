"""

Kirjuta programm:
1. Küsi looma nimesid kuni tühja sisestuseni
2. Kuva sama tähega algavate loomade kõige pikemad nimed

Näiteks:
Sisend -< Karu, Kass, Koaala, Siil, Saarmas, Rebane
Tulem: K – Koaala S – Saarmas R – Rebane
"""

animals = []
letters = []
first_letter = ""
longest_word = ""
longest_word_len = 0

while True:
    # capitalize the first letter
    name = input("Sisesta looma nimi: ").capitalize()
    if name == "":
        break
    else:
        animals.append(name)
        # if we don't have animals that begin with the letter then add to the letter list
        if(name[0]) not in letters:
            letters.append(name[0])
# loop over all the letters
for i in range(len(letters)):
    # print the letter, add space to the end instead of the newline
    print(f"{letters[i]} –", end=" ")
    # loop over all the animals
    for j in range(len(animals)):
        # if the first letter is the same as our letter
        if letters[i] == animals[j][0]:
            # test if the length is the longest
            if len(animals[j]) > longest_word_len:
                longest_word_len = len(animals[j])
                longest_word = animals[j]
    print(longest_word)

