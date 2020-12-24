string = input("введите слова - ").split()
for i, word in enumerate(string, 1):
    print(f'{i} {word[:10]}')
