def word_count(s):
    # Your code here
    dictionary = {}
    ignored_characters = ''.join(c for c in s if (not c.isalnum()) and c!="'")
    # replace = '":;,.-+=/\\|[]{}()*^&'
    if len(ignored_characters) > 0:
        # print(''.join(c.lower() for c in s if c.isalnum() or c=="'" or c==" "))
        # print(''.join(dictionary[c.lower()] for c in s if c.isalnum() or c=="'" or c==" "))
        
        # new_string = s
        # for c in replace:
        #     new_string = new_string.replace(c, "")
        
        new_string = ''.join(c.lower() for c in s if c.isalnum() or c=="'" or c==" " or c == "\t" or c=="\n" or c=="\r")
        # print(new_string)
        new_list = new_string.replace("\t", " ").replace("\n", " ").replace("\r", " ").split(" ")
        # print(new_list)
        for word in new_list:
            if len(word) > 0:
                if word in dictionary.keys():
                    dictionary[word] = dictionary[word] + 1
                else:
                    dictionary[word] = 1
    return dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))