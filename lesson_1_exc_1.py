name = input('Введите Ваши имя:\n')
fam = input('Теперь фамилию:\n')

def format(x):
    x = x.strip()
    x = x.capitalize()
    return x

name = format(name)
fam = format(fam)


print('Привет тебе, ' + name + ' ' + fam + '!')
