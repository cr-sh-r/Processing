f = open("filetest","w")
name = input("your name:")
age = input("your age:")
f.write(name)
f.write("\n")
f.write(age)
f.write("\n")
if age != 0:
    print("who cares")

