animal = input("enter the type of animal(omnivorous,carnivorous,herbivorous):")

if animal == "omnivorous" or animal == "Both":
    print("Omnivorous eat both meat and vegetable!")

elif animal == "carnivorous" or animal == "meat only":
    print("Carnivorous eat only meat!")

elif animal == "herbivorous" or animal == "vegetable only":
    print("Herbivorous eat  only vegetable!")

else:
    print("Unknown animal")
