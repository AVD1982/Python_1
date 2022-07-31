def change(lst):
    first = lst.pop()
    end = lst.pop(0)
    lst.insert(0, first)
    lst.append(end)
    return lst


print(change([1, 2, 3]))
print(change([9, 12, 33, 54, 105]))
print(change(['с', 'л', 'о', 'н']))
