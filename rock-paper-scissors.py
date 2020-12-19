import random
cash = 10
B = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
C = ['камень', 'ножницы', 'бумага']
print('Фиксированная ставка -- одна монетка')
print(f'Ваш баланс: {str(cash)}')
while cash > 0:
    try:
        A = random.randint(0, 2)
        X = input('Камень, ножницы, бумага, я выбираю...')
        try:
            D = int(X) - 1
        except:
            X = X.strip().lower()
            D = C.index(X)
        cash = cash + B[D][A]
        if B[D][A] == 1:
            print('Победа! Противник выбрал ' + C[A] + '.')
        if B[D][A] == 0:
            print('Ничья! Противик выбрал ' + C[A] + '.')
        if B[D][A] == -1:
            print('Проигрыш! Противник выбрал ' + C[A] + '.')
        print('Ваш баланс: ' + str(cash))
    except:
        pass
print ('Приходи еще. Когда будут деньги...')