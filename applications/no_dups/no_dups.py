def no_dups(s):
    # Your code here
    cache = {}
    o = ""
    n = s.split()
    length = len(n)
    counter = 0
    for word in n:
        counter += 1
        if word in cache.keys():
            cache[word] += 1
        else:
            cache[word] = 1
            if counter > 1:
                o += " "
            o += word

    return o

            



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))