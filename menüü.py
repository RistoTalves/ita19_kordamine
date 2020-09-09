print("1 - näita tervet faili sisu")
print("2 - otsi pealkirja või aastaarvu järgi")
print("3 - otsi failist nime järgi")
print("4 - otsi lauljaid")
valik = int(input("Mida soovite teha?(1, 2, 3, 4) "))

lineList = []

with open('albumid') as f:
    lineList = f.readlines()

with open('albumid') as f:
    for line in f:
        lineList.append(line)

lineList = [line.rstrip('\n') for line in open('albumid')]
with open('albumid', 'r', encoding=UTF-8) as fail:
    info = csv.reader(fail, delimiter="\t")
    for rida in info:
        tabel.append(rida)

if valik == 1:
    for rida in fail:
        print(rida)
        print("----------------")
    fail.close
elif valik == 2:
    print("qwerty")
else:
    pass












"""
laul_1 = Laul("Für Oksana", "Nublu")
print(laul_1.laulja, laul_1.pealkiri)

laul_2 = Laul("12", "Nublu")
print(laul_2.laulja, laul_2.pealkiri)

laul_3 = Laul("Crousandid", "Nublu")
print(laul_3.laulja, laul_3.pealkiri)

laul_4 = Laul("Öölaps", "Nublu")
print(laul_4.laulja, laul_4.pealkiri)

# testime albumi loomist

album_1 = Album("Uus album", 2019, "Nublu")

# lisame laulud albumisse

album_1.laulud.append(laul_1)
album_1.laulud.append(laul_2)

# testimie albumi loomist

album_2 = Album("Uus album 2", 2019, "Nublu")

# lisame laulud albumisse

album_2.laulud.append(laul_3)
album_2.laulud.append(laul_4)

# vaatame loodud albumi sisu

print(album_2.pealkiri)

for laul in album_2.laulud:
    print(laul.laulja, laul.pealkiri)
# testime Laulja loomist

laulja = Laulja("Nublu")

laulja.albumid.append(album_1)
laulja.albumid.append(album_2)

# testime albumite sisu

for album in laulja.albumid:
    print(album.pealkiri)
    for laul in album:
        print(laul.laulja, laul.pealkiri)
"""