cake = """
        ___{}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
bday = input("Your bday (dd/mm/yyyy): ")
year = int(bday.split("/")[-1])
cypher = int(str(2020 - year)[-1])
print(cake.format("i"*cypher))