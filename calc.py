from datetime import timedelta

class Resource:
    """A ressource"""
    name = None
    neededAmountOfResources = []
    duration = timedelta(seconds=0)
    
    def __init__(self, name, neededAmountOfResources, duration):
        self.name = name
        self.neededAmountOfResources = neededAmountOfResources
        self.duration = duration

    def __str__(self):
        return self.name + " braucht " + str(len(self.neededAmountOfResources)) + " Resources und dauert " + str(self.duration)

    def get_amount_of_needed_basic_resources(self):
        for amount in self.neededAmountOfResources:
            aResource = amount.resource
            print ("name: " + aResource.name)
        else:
            print "no resources needed"
        return "hallo"

class Amount:
    """Amount of resource
    amount = 0
    resource = None
    """

    def __init__(self, amount, resource):
        self.amount = amount
        self.resource = resource

# Fabrik
metall = Resource("Metall", [], timedelta(minutes=1))
holz = Resource("Holz", [], timedelta(minutes=3))
plastik = Resource("Plastik", [], timedelta(minutes=9))
samen = Resource("Samen", [], timedelta(minutes=20))
mineralstoff = Resource("Mineralstoff", [], timedelta(minutes=30))
chemikalien = Resource("Chemikalien", [], timedelta(hours=2))
textilien = Resource("Textilien", [], timedelta(hours=3))
zuckerUndGewuerze = Resource("Zucker und Gewuerze", [], timedelta(hours=4))
glas = Resource("Glas", [], timedelta(hours=5))
tiernahrung = Resource("Tiernahrung", [], timedelta(hours=6))

# Baustoffhandel
naegel = Resource("Naegel", [Amount(2, metall)], timedelta(minutes=4) + timedelta(seconds=15))
bretter = Resource("Bretter", [Amount(2, holz)], timedelta(minutes=25) + timedelta(seconds=30))
backsteine = Resource("Backsteine", [Amount(2, mineralstoff)], timedelta(minutes=11))
zement = Resource("Zement", [Amount(2, mineralstoff), Amount(1, chemikalien)], timedelta(minutes=42) + timedelta(seconds=30))
kleber = Resource("Kleber", [Amount(1, plastik), Amount(2, chemikalien)], timedelta(minutes=51))
farbe = Resource("Farbe", [Amount(2, metall), Amount(1, mineralstoff), Amount(2, chemikalien)], timedelta(minutes=51))

#Werkzeug-Laden
hammer = Resource("Hammer", [Amount(1, metall), Amount(1, holz)], timedelta(minutes=12) + timedelta(seconds=36))
maszband = Resource("Maszband", [Amount(1, metall), Amount(1, plastik)], timedelta(minutes=18))
schaufel = Resource("Schaufel", [Amount(1, metall), Amount(1, holz), Amount(1, plastik)], timedelta(minutes=17))
kochutensilien = Resource("Kochutensilien", [Amount(2, metall), Amount(2, plastik), Amount(2, holz)], timedelta(minutes=40) + timedelta(seconds=30))
leiter = Resource("Leiter", [Amount(2, bretter), Amount(2, metall)], timedelta(minutes=54))

# Bauermarkt


print("===")
leiter.get_amount_of_needed_basic_resources()
