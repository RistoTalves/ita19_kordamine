from laul import Laul
from album import Album
from laulja import Laulja

# testime laulu objekti loomist

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

laulja.albumid.append(albumid_1)
laulja.albumid.append(albumid_2)

# testime albumite sisu

for album in laulja.albumid:
    print(album.pealkiri)
    for laul in album:
        print(laul.laulja, laul.pealkiri)