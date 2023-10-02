def main():
    """
    Main functie. Roept de andere functies op om hun werk te doen. 
    """
    x = blaat(5) + blaat(3)
    print(x)

def testing():
    """
    Test functie. Hier staan alle assertions om de functies te testen.
    """

def blaat(x):
    l = list(range(5))
    return sum(l)

main()
testing()
