# 1 задача
print((lambda x, y, z: x * y * z)(2, 5, 5))

# 2 задача

text = [{'name': 'Jennifr', 'final': 95},
        {'name': 'David', 'final': 92},
        {'name': 'Nikolas', 'final': 98}]

name = sorted(text, key=lambda item: item['name'])
ball = sorted(text, key=lambda item: item['final'], reverse=True)
print(name)
print(ball)
#  3 задача

text1 = [{'name': 'Jennifr', 'final': 95},
         {'name': 'David', 'final': 92},
         {'name': 'Nikolas', 'final': 98}]

ball_max = max(text, key=lambda item: item['final'], )
ball_min = min(text, key=lambda item: item['final'], )

print(ball_max)
print(ball_min)

#  4 задача


nums = [3, 5, 7, 3, 9, 5, 7, 2]

print(list(map(lambda t: t ** 2, nums)))
print(list(map(lambda t: t ** 3, nums)))
