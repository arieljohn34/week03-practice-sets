import os

with open("new_notes05.txt", "w") as file:
    file.write("Hello World!")

with open("new_notes05.txt", "a") as file:
    file.write(" This is an appended text.")

with open("new_notes05.txt", "r") as source, open("destination.txt", "w") as destination:
    destination.write(source.read())

