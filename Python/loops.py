#for####
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

for x in range(100, 10, -2):
    print("Number x = " + str(x))

for x in range(1, 6):
    print(x)

mynumber_list = list(range(0, 10))
for x in mynumber_list:
    x = x * 2
    print(x)

all_cars = ['chrusler', 'dacia', 'bmw', 'KIA', 'vw', 'seat', 'skoda', 'lada', 'audi', 'ford', 'Chevrolett']
german_cars = ['bmw', 'vw', 'audi']


for xxxx in all_cars:
    if xxxx not in german_cars:
        print(xxxx + " is not German Car" + " index = " + str(all_cars.index(xxxx)))
        
#while####
while True:
    print(x)
    x = x + 1
    if x == 100:
        break
    
#if####
def bool_to_word(bool):
    return "Yes" if bool else "No"

age = 14
if (age <= 4):
    print("You are baby!")
elif (age > 4) and (age < 12):
    print("You age kid")
elif (age >= 12) and (age < 19):
    print("You age teenager")
else:
    print("You are old!")

