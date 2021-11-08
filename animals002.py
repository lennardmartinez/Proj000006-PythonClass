class DogPark:

    def __init__(self, dogs):
        self.dogs = dogs

    def rollcall(self):
        print("The dogs inside the park are:")
        for dog in self.dogs:
            print(f{dogs.name})

    def shout(self, words):
        for dog in self.dogs:
            dog.hear(words)

    def converse(self):
        self.rollcall()
        while True:
            words = input("Talk to doggos! ('quit' to quit) > ")
            if 'quit' in words:
                print("Bye!")
                break
            else:
                # The shout method is used here.
                self.shout(words)

if __name__ == '__main__':
    dogs = [animals.Husky("Toklat"),
            animals.Chihuahua("Scrappy"),
            animals.Labrador("Barrett")]
    park = DogPark(dogs)
    park.converse()


class Dog:

    def __init__(self, name):
        self.mood = "neutral"
        self.name = name

    def speak(self):
        print("woof")

    def hear(self, words):
        if self.name in words:
            self.speak()

    def do_trick(self):
        pass

class Shitzu(Dog):
    pass

class TrainedChihuahua(Chihuahua):
    def do_trick(self):
        print("The chihuahua spins in the air and turns briefly into a chicken.")

class Husky(Dog):
    origin = "Siberia"

    def speak(self):
        print("Awoo!")

class Chihuahua(Dog):
    origin = "Mexico"

    def speak(self):
        print("Yip!")

class Labrador(Dog):
     origin = "Canada"