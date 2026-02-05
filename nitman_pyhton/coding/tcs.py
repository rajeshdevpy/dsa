def func(x, y=[]):
    y.append(x)
    return y
#  [1, 2, 1, 2]
 
result1 = func(1)
result2 = func(2)
 
 
print(result1 + result2)


x = [1, 2, 3]
y = x + [4, 5] 
# --> [1, 2, 3, 4, 5]
z = x.extend([4, 5]) 
# --> [1, 2, 3, 4, 5]
print(x, y, z) 
[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], None


x = [1, 2, 3]
y = x
x += [4, 5]
print(y)
[1, 2, 3, 4, 5]

range(1, 5, 0.5)