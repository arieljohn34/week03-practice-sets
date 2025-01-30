import os

def replace_word_in_file(input_file, old_word, new_word, output_file=None):
   
   #analyzing files 
    with open(input_file, "r", ) as file:
        content = file.read()

    
    updated_content = content.replace(old_word, new_word)

   
    if output_file is None:
        output_file = input_file  

   #for changing purpose
    with open(output_file, "w", ) as file:
        file.write(updated_content)

    print(f"Replaced '{old_word}' with '{new_word}' in '{output_file}'.")

#need specific file ex:sheeshable.txt
replace_word_in_file("sheeshable.txt", "old", "aight")  
