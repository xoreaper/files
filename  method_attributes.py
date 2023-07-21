class HumanBeing:
    welcome_message = "Welcome to the program"  # class variable
    a = 10

    def __init__(self, name):  # constructor
        self.my_name = name  # instance variable
        self.height = 6  # instance variable

    # instance method
    def print_name(self):
        print(
            f'name is {self.my_name} {self.height} {self.welcome_message} {self.a}')

    # class method
    @classmethod  # decorators
    def welcome(cls):
        print(f'{cls.welcome_message} {cls.a}')

    # static method
    @staticmethod  # decorators
    def do_something():
        hello = "Welcome from static method"
        print(hello)


# instance way
oshan_object = HumanBeing("Oshan")
# can call all types of method but required instance to call instance method
oshan_object.print_name()
oshan_object.welcome()
    
oshan_object.do_something()

# class way
