#read the line and store in a list
#reverse the list
#write back to file
with open("readwrite.txt", "r") as reader:
    content = reader.readlines()
    reversed(content)
    with open("readwrite.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)

