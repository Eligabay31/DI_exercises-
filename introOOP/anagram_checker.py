from itertools import permutations

class AnagramChecker:
    def __init__(self):
        self.allwords = open("englishwords.txt", "r").read().split("\n")

    def is_valid(self, word):
        return True if word in self.allwords else False

    def get_anagrams(self, word):
        temp = []
        letter = list(word)
        tocheck = permutations(letter)
        for item in tocheck:
            join = (''.join(item))
            temp.append(join)
        print(join)







        # temp = []
        # for item in range(len(self.allwords)):
        #     for combination in itertools.combinations(word, item):
        #         joinword = (''.join(combination))
        #         temp.append(joinword)
        # print(temp)














check = AnagramChecker()
print(check.allwords)
print(check.is_valid("meat".upper()))
print(check.get_anagrams("meat".upper()))

