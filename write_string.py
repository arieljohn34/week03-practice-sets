import os 


strings = ["Python", "is", "a", "powerful", "language"]

with open("strings.txt", "w") as file:
    for string in strings:
        file.write(string + "\n") 



with open("strings.txt", "a") as file:
    file.write("My python.")

