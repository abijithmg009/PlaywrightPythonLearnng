file = open("readwrite.txt")
#read all contents
#file.read()
#print(file.read(5)) #read n number of values

#read one single line
#print(file.readline())
#print(file.readline())
#print(file.readline())

#print line by line using readline method
#line = file.readline()
#while line!="":
#    print(line)
#    line = file.readline()

for line in file.readlines():
    print(line)

file.close()