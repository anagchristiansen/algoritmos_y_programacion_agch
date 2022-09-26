v1 = [1,2,3]
v2 = [-1,0,2]
result = 0

for index in range(len(v1)):
    result += (v1[index]*v2[index])

print("The result is", result)