file = open("data1.txt","w")
file.write("Welcome to SKP")
file = open("data1.txt", "r")
for line in file:
    print(line)
file.close()


