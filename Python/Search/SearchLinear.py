def linear_search(lst, search_item):
    start = 0
    search_result = False

    while start < len(lst) and not search_result:
        if lst[start] == search_item:
            search_result = True
        else:
            start += 1
    return search_result


lst = [12, 34, 25, 15, 67, 23, 11, 5, 86]
value = 11
result = linear_search(lst, value)
if result:
    print("Элемент найден!")
else:
    print("Элемент не найден!")