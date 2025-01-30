import os


with open("numbers01.txt", "w") as file:
    for i in range(1, 11): 
        file.write(str(i) + "\n")  
