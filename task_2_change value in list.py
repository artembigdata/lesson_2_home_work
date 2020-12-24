#my_list = list(input("Enter the numbers - "))
#for i in range(1, len(my_list), 2):
 #   my_list[i-1], my_list[i] = my_list[i], my_list[i - 1]
#print(my_list)

my_list = input("enter numbers: ").split()
print('list:', my_list)
idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1
my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
print(my_list)
