
# parent class
class Organism:
    name = 'Unknown'
    species = 'Unknown'
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}\n".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

    def history(self):
        msg = "\nOrganisms first appeared around 3.7 billion years ago."


#child class instance
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg
    
    def history(self):
        msg = "\nModern humans evolved around 300,000 years ago."
        return msg


#another child class instance
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = 'Earth'

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg

    def history(self):
        msg = "\nDogs evolved from Miacis around 30-40 million years ago."
        return msg


#another child class instance
class Bacteria(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = 'Mars'

    def replication(self):
        msg = "\nThe cells begin to devide and multiply into two seperate organisms!"
        return msg

    def history(self):
        msg = "\nBacteria appeared around 3.5 billion years ago."
        return msg





if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())
    print(human.history())

    dog = Dog()
    print(dog.information())
    print(dog.bite())
    print(dog.history())

    bacteria = Bacteria()
    print(bacteria.information())
    print(bacteria.replication())
    print(bacteria.history())
