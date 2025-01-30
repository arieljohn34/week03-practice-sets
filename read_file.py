import os

def read_file(file_name1):
    with open(file_name1, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        
        print("File Contents:")
        for line in lines:
            print(line.strip())

       
        total_lines = len(lines)
        print(f"\nTotal number of lines: {total_lines}")

        
        total_words = sum(len(line.split()) for line in lines)
        print(f"Total number of words: {total_words}")

        
        total_characters = sum(len(line) for line in lines)
        print(f"Total number of characters: {total_characters}")


file_name = "new_notes05.txt"  
read_file(file_name)
