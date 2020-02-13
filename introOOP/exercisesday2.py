class Family:
    def __init__(self, members):
        self.members = []



    def born(self, name, age, sex, is_child):
        self.members.append({"name": name, "age": age, "sex": sex, "is_child": is_child })
        print("Mazal Tov, for your new member!")

    def is_18(self, name):
        family = self.members
        for item in family:
            if item.get('name') != name:
                continue
            elif item["name"] == name:
                if item["age"] >= 18:
                    return True
                else:
                    return  False
                break


# class TheIncredibles(Family)








member1 = Family("e")
member1.born("eli", 16, "boy", True)
member1.born("edssddf", 19, "boy", True)
print(member1.is_18("eli"))
print(member1.members)

# class Family:
#     def __init__(self, members, last_name):
#         self.members = members
#         self.last_name = last_name
#
#     def born(self, **kwargs):
#         self.members[kwargs["name"]] = kwargs
#         print(f"mazel tov for the birth of {kwargs.get('name')} !")
#
#     def is_18(self, name):
#         if self.members.get(name)
#             member = self.members.get(name)
#             return member["age"] >= 18
#         else:
#             raise KeyError(f"{name}blah blah")
#
# class Theincredibles(Family)
#
#     def use_power(self, name):
#         member = self.members.get(name)
#         if member:
#             power = member.get('power')
#
#         else:
#             raise KeyError
#
# if __name__ == '__main__':
#     fam_dic = {
#     'Michael'{'name':'Michael','age':35,'sex':'Male','is_child':False},
#     'Sarah'{'name':'Sarah','age':32,'sex':'Female','is_child':False},
#     'Kevin'{'name':'Kevin','age':16,'sex':'Male','is_child':True},
#     }
#
#     family = Family(fam_dic, "Cohen")
#
#     def
#
# print(family.members)
# print()

