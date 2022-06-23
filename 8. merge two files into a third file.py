with open("text.txt","r") as file1, open("text1.txt","r") as file2, open("text3.txt","w") as file:
    file.write(file1.read())
    file.write('\n')
    file.write(file2.read())