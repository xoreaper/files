class HumanBeing():
    greet ="Welcome to the program"
    def __init__(self,name):
        self.name=name
    def greeting(self):
        print(f'{self.greet}, {self.name}')
        
bibidh_object = HumanBeing("Bibidh")
bibidh_object.greeting()
        