# Your code here
import os
dirpath = os.path.dirname(os.path.abspath(__file__))
with open(dirpath + "/robin.txt") as f:
    lines = f.readlines() # array of lines
    # words = f.read()

dictionary = {}
for line in lines:
    ignored_characters = ''.join(c for c in line if (not c.isalnum()) and c!="'")  
    new_string = ''.join(c.lower() for c in line if c.isalnum() or c=="'" or c==" " or c == "\t" or c=="\n" or c=="\r")
    new_list = new_string.replace("\t", " ").replace("\n", " ").replace("\r", " ").split(" ")
    for word in new_list:
        if len(word) > 0:
            if word in dictionary.keys():
                dictionary[word] = dictionary[word] + 1
            else:
                dictionary[word] = 1

sorted_dictionary_1 = sorted(dictionary.items())
sorted_dictionary_2 = sorted(sorted_dictionary_1, key=lambda c: c[1], reverse=True)

for item in sorted_dictionary_2:
    if len(item[0]) < 8:
        print(item[0] + "\t\t" + "#"*item[1])
    else:
        print(item[0] + "\t" + "#"*item[1])