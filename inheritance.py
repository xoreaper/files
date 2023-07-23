class Mammal:
    def __init__(self, grade, eyes, name):
        self.grade = grade
        self.eyes = eyes
        self.name = name

    def greeting(self):
        print("Hello , This is a brief about myself cv")


class Humanbeing(Mammal):
    def __init__(self, brain, hands, grade, eyes, name):
        self.brain = brain
        self.hands = hands
        super().__init__(grade, eyes, name)

    def print_details(self):
        print(
            f'Name is : {self.name} ,I have {self.eyes} eyes, I study in grade {self.grade}, I have an IQ of  {self.brain} , I have {self.hands} hands')


bibidh_object = Humanbeing("100", "2", "12", "2", "Bibidh")
bibidh_object.print_details()
bibidh_object.greeting()
