class Dog:
    def speak(self):
        print("woof")

    def learn_name(self, name):
        self.name = name

    def do_trick(self):
        pass

class Chihuahua(Dog):
    pass

class TrainedChihuahua(Chihuahua):
    def do_trick(self):
        print("The chihuahua spins in the air and turns briefly into a chicken.")