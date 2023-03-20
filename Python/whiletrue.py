import sys

filename = "/Users/isakonst/Learn1/Python/justfile.txt"

while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding="Latin-1")
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        print(sys.exc_info()[1])  #mmodule sys for that
        filename = input("ENter Correct file name! :")
    else:
        print("Indise ELSE")
        print(myfile.read())
        break


print("======================EOF================")