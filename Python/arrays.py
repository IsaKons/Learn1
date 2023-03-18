cities = ['New York', 'Moscow', 'new dehli', 'Simferopol', 'Toronto']

print(len(cities))
print(cities[0])
print(cities[-3])
cities[2] = 'Tula'
cities.append('Kursk')
cities.insert(2, 'Feodosiya')
del cities[-1]
cities.remove('Tula')
cities.reverse()
print(cities[-4:-1])

deleted_city = cities.pop()
print("Deleted city is: " + deleted_city)
print(cities)

mynumber_list = list(range(0, 10))
print("Max number is: " + str(max(mynumber_list)))
print("Min number is: " + str(min(mynumber_list)))
print("Sum of list is: " + str(sum(mynumber_list)))

#dictionary
enemy = {
          'loc_x':  70,
          'loc_y':  50,
          'color':  'green',
          'health': 100,
          'name': 'lol',
}

print("Location X = " + str(enemy['loc_x']))
enemy['rank'] = 'Admiral'
del enemy['rank']
print(enemy.keys())
print(enemy.values())

all_enemies = []

for x in range(0, 10):
    all_enemies.append(enemy.copy())

all_enemies[5]['health'] = 30
all_enemies[8]['name'] = "Kozel"
all_enemies[2]['loc_x'] += 10