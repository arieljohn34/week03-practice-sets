import os 

def merge_files(file1, file2, output_file,):
    try:
       
        with open(file1, 'r') as files1, open(file2, 'r') as files2:
            content1 = files1.read()
            content2 = files2.read()
       

        with open(output_file, 'w') as output:
            output.write(content1 + '\n' + content2)
        print(f"Content merged successfully into {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")

#if i put anything on files it will be created inside the create file text
file1 = 'file_merge1.txt'
file2 = 'file_merge2.txt'
output_file = 'createfile.txt'



merge_files(file1, file2, output_file, )
