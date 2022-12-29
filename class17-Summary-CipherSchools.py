# LIST COMPREHENSION SUMMARY
# square = []
# for i in range(1,11):
#     square.append(i**2)

# square = [i**2 for i in range(1,11)]
# print(square)

# even_num = [i for i in range(1,11) if i%2==0]
# print(even_num)

# if else
# [1,2,3,4,5,6,7,8,9,10]
# [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]
# mixed = [i*2 if (i%2==0) else -i for i in range(1,11)]
# print(mixed)
nl = [[1,2,3], [1,2,3], [1,2,3]]
new_list = [[i for i in range(1,4)] for j in range(3)]
print(new_list)