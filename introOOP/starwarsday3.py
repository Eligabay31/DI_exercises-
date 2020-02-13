import random

class ForceWielder:
    def __init__(self, name):
        self.name = name
        self.power = random.randint(1,15)
        self.wisdom = random.randint(1,15)


    def train(self):
        if self.is_jedi():
            self.power = random.randint(1, 15) + random.randint(5, 10)
            self.wisdom = random.randint(1, 15) + random.randint(10, 20)
        else:
            self.power = random.randint(1, 15) + random.randint(10, 20)
            self.wisdom = random.randint(1, 15) + random.randint(5, 15)

    def fight(self, power):
        power1 = self.power * self.wisdom/self.power + self.wisdom
        power2 = power.power * power.wisdom / power.power + power.wisdom



        if power1 > power2:
            print(f"{self.name} is the winner with: {power1} using the {self.lightsaber} and {power.name} loses with {power2} using the {power.lightsaber}!!")

        else:
            print(f"{power.name} is the winner with: {power2} using the {power.lightsaber} and {self.name} loses with {power1} using the {self.lightsaber}!!")




    def is_jedi(self):
        if isinstance(self, Jedi):
            return True
        else:
            return False


class Jedi(ForceWielder):
        def __init__(self, name):
            super().__init__(name)
            self.power = random.randint(1, 15)
            self.wisdom = random.randint(1, 15) + 10

            if self.wisdom > self.power:
                self.lightsaber = "green lightsaber"
            elif self.power > self.wisdom:
                self.lightsaber = "blue lightsaber"
            else:
                self.lightsaber = "violet lightsaber"


class Sith(ForceWielder):
    def __init__(self, name):
        super().__init__(name)
        self.name = "Darth " + name
        self.lightsaber = "red lightsaber"
        self.power = random.randint(1, 15) + 10



