file = open('test.txt')

#print(file.read(5))     # read all the contents of the file, read n number of char by passing parameters

#print(file.readline())  # read one single line at a time
#print(file.readline())

#file.close()

# print line by line using readLine method

line = file.readline()
while line != "":
    print(line)
    line = file.readline()


for line in file.readlines():    # through a list
    print(line)




file.close()


