goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('для выхода из программы Q, для продолжения enter:').upper()=='Q':
        app
    num += 1
    for f in features.keys():
        pro = input(f'введите значение свойства "{f}": ')
        features[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        analytics[f].append(features[f])
    goods.append((num, features))
    print(f"\nСтруктура товаров\n{goods}")
    print(f'\n текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print("*" * 30)

