from random import randint

di = 0
do = 0
m = 0
f = 0
hi = 0
ho = 0
variables = ["di", "do", "m", "f", "hi", "ho"]
pr_type_lst = [123, 124, 125, 126, 134, 135, 136, 145, 146, 156, 234, 235, 236, 245, 246, 256, 345, 346, 356, 456, 1234, 1235, 1236, 1245, 1246, 1256, 1345, 1346, 1356, 1456, 2345, 2346, 2356, 2456, 3456, 12345, 12346, 12356, 12456, 13456, 23456]
type = pr_type_lst[randint(0, 41)]
i = 0
num_list = []
while i < len(str(type)):
    num_list.append(str(type)[i])
    i += 1
print(num_list)
j = 0
while j < len(num_list):
    print(variables[(int(num_list[j])-1)])
    j += 1
# m = -di/do = hi/ho
# 1/f = 1/di + 1/do
