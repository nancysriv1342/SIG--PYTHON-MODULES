list = ["abc", "def", "ghi,hju"]
textfile = open("list.txt", "w")
for element in list:
    textfile.write(element + "\n")
textfile.close()
