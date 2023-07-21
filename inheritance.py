class Mammal:
    def __nit__(self, legs, eyes):
        self.legs = legs
        self.eyes = eyes

    def print_details(self):
        print(self.legs, self.eyes)

        class Humanbeing(Mammal):
            def __init__(self, brain, hands):
                self.brain = brain
                self.hands = hands
