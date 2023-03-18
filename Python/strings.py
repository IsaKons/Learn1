name = " ..My big string.."

print(name.title())
print(name.upper())
print(name.lower())

print("Privet stroka nomer1\nPrivet stroka N2\n\nStroka N3")
print("Messages:\n\tMessage1\n\tMessage2\n\tMessage3\nEND")
print("Lower name: " + name.lower())

print(name.rstrip())
print(name.lstrip())
print(name.strip())        # Udalenie probelov
print(name.strip("."))     # Udalenie to4ek

mylist = []
msg =""
while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish ")
    mylist.append(msg)
print(mylist)