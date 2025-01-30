import os

def count_word_frequency(input_file, output_file):

    word_count = {}

    
    with open(input_file, 'r') as file:
       
        text = file.read()
        
        words = text.split()

        for word in words:
            word = word.lower().strip('.,!?()[]{}":;')  
            if word: 
                word_count[word] = word_count.get(word, 0) + 1

    
    with open(output_file, 'w') as output:
        for word, count in word_count.items():
            output.write(f"{word}: {count}\n")
    print(f"Word frequency has been saved to {output_file}")


input_file = 'edo_tensei.txt'  #text analyze
output_file = 'absolute_zero.txt' # output of each frequent words
count_word_frequency(input_file, output_file)
