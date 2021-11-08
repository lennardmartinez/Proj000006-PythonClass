class Cat:

    def __init__(self, name):
        self.mood = "neutral"
        self.name = name

    def speak(self):
        if self.mood == "happy":
            print("Purrr")
        elif self.mood == "angry":
            print("Hiss!")
        else:
            print("Meow!")