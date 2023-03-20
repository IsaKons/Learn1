inputfile = "/Users/isakonst/Learn1/Python/justfile2.txt"
outputfile = "/Users/isakonst/Learn1/Python/justfile.txt"

password_tolookfor = "password"

myfile1 = open(inputfile, mode='r', encoding='latin_1')  # r - read, w- write, a - append, r+
myfile2 = open(outputfile, mode='a', encoding='latin_1')

for num, line in enumerate(myfile1, 1):
    if password_tolookfor in line:
        print("Line N: " + str(num) + " : " + line.strip())
        myfile2.write("Found password:" + line)

myfile1.close()
myfile2.close()
