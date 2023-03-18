# import filename
# to hold all func in another file

def napeshatat_privetstvie(name):
    """Print Privetstrvie"""
    print("Congratulations " + name + " wish you all the best!")

def summa(x, y):
    return x+y

def factorial(x):
    """Calculate Factorial of number X"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet

def create_record(name, telephone, address):
    """Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record

def give_award(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print("Tovarish " + person.title() + " nagrajdaetsya medaliyu " + medal)

napeshatat_privetstvie("Vasya")

x = summa(33, 22)
print(x)

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))

user1 = create_record("Vasya", "+97123123123123123","Tinussiya")
print(user1)

give_award("Za Berlin", "vasya", "petya")
give_award("Za London", "petya", "alexander","valintin")