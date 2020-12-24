my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
new_number = int(input("ввод числа: "))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i, new_number)
print(my_list)
