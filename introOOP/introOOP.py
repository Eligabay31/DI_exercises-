# class House:
#     def __init__(self, city ,num_rooms, landlord):
#         self.city = city
#         self.num_rooms = num_rooms
#         self.landlord = landlord
#
#         self.rent = 1000 * self.num_rooms
#         if city == "TA":
#             self.rent *= 2
#
#
#     def sign_contract(self, name, date):
#         if self.landlord == "Moti":
#            self.rent *= 2
#         print(f"Rental agreement between {name} and {self.landlord}")
#
#     def complain_about_broken_window(self):
#         print(f"{self.landlord} says 'Sorry, I can\'t help'" )
#

# exercise 1

# class Dog:
#     def __init__(self, nameDog, heightDog):
#         self.nameDog = nameDog
#         self.heightDog = heightDog
#         self.jump = 2 * self.heightDog
#
#
#     def talk(self):
#         print(f" Wouaf, my name is {self.nameDog} !")
#
#     def jump(self):
#         self.heightDog *=2
#         print(self.heightDog)

# davids_dog = Dog("Rex", 50)
# sarahs_dog = Dog("Teacup", 20)
#
#     def bigger(self):
#         if davids_dog.heightDog > sarahs_dog.heightDog:
#             print("Rex is the winner")
#         else:
#             print("Teacup is the winner")


#exercise2

# class Zoo:
#     def __init__(self, zooName):
#         self.animals = []
#         self.zooName = zooName
#
#     def addAnimal(self, newAnimal):
#         if newAnimal not in self.animals:
#             self.animals.append(newAnimal)
#
#     def getAnimals(self):
#         print(self.animals)
#
#     def sellAnimals(self,byeAnimal):
#         if byeAnimal in self.animals:
#             self.animals.remove(byeAnimal)
#             print(f"Goodbye {byeAnimal}!")
#
#     def sortAnimal(self):
#         self.animals.sort()
#         print(self.animals)
#
# falta la parte 6



# elizoo = Zoo("eliszoo")
# elizoo.addAnimal("giraffe")
# elizoo.addAnimal("monkey")
# elizoo.addAnimal("lion")
# elizoo.addAnimal("manati")
# elizoo.addAnimal("lizard")
# elizoo.addAnimal("gorilla")
# elizoo.addAnimal("ave")
# elizoo.getAnimals()
# elizoo.sellAnimals("gorilla")
# elizoo.sortAnimal()




















