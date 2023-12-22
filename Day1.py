#day1

import re

def split(arr, count):
    lukui = [arr[i::count] for i in range(count)]
    return min(lukui), max(lukui)

input = open("day1input.txt", "r")

nrot = []
nrot_tekstina = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
nrot_numeroina = [0,1,2,3,4,5,6,7,8,9]
nrot_dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

for row in input:
    sanakirja = {}
    for character in row:
        if character.isnumeric():
            indeksi = row.rfind(character)
            sanakirja[indeksi] = str(character)

    for numero in nrot_tekstina:
        if numero in row:
            indeksi = [m.start() for m in re.finditer(numero, row)]
            if len(indeksi) > 1:
                indeksi1, indeksi2 = split(indeksi, len(indeksi))
                sanakirja[indeksi1[0]] = str(nrot_dic[numero])
                sanakirja[indeksi2[0]] = str(nrot_dic[numero])
            else:
                sanakirja[str(indeksi)] = str(nrot_dic[numero])
    print(sanakirja)
    nro = sanakirja[min(sanakirja)] + sanakirja[max(sanakirja)]
    nrot.append(int(nro))
    print(f"{nro}: {row}")

print(len(nrot))
print(sum(nrot))