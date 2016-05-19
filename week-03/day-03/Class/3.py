# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise


class Pirate():

    def __init__(self):
        self.drink = 0

    def drink_rum(self):
        self.drink += 1
        return self.drink


    def how_goin_mate(self):
        if self.drink >= 5:
            print ('Arrrr')
        else:
            print ('Nothin')

pirate1 = Pirate()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.how_goin_mate()

pirate2 = Pirate()
pirate2.how_goin_mate()
