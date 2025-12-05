try:
    f = open("filetest","r")
    name = f.readline()
    print(name)
    age = f.readline()
    print(age)
except FileNotFoundError: 
    print("no file")

