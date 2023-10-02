speler1 = input("Steen, papier of schaar voor speler 1: ").lower()
speler2 = input("Steen, papier of schaar voor speler 2: ").lower()

if speler1 == speler2:
    print("Gelijkspel!")
elif (
    (speler1 == "steen" and speler2 == "schaar") or
    (speler1 == "papier" and speler2 == "steen") or
    (speler1 == "schaar" and speler2 == "papier")
):
    print("Speler 1 wint!")
else:
    print("Speler 2 wint!")