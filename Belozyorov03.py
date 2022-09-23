a = int(input('Выберите язык шифрования:\n1. Английский\n2. Русский\n\nВведите цифру соответствующую нужному языку: '))
b = ('Английском', 'Русском')
t = int(input('\nВыберите необходимое действие:\n1. Зашифровать\n2. Расшифровать\n\nВведите цифру соответствующую необходимому действию: '))
sl = input('\nВведите фразу или слово на ' + b[a-1] + ' языке: ')
x = ('25', '32')
step = int(input('\nВведите шаг шифрования в виде числа от 1 до ' + x[a-1] + ': '))
eng = str('abcdefghijklmnopqrstuvwxyz')
ENG = str('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ru = str('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
RU = str('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
slr = ''
if t == 1 and a == 1:
    for i in range(len(sl)):
        if sl[i] in eng:
            c = eng.find(sl[i]) + step
            if c >= 26:
                c -= 26
            slr += eng[c]
        elif sl[i] in ENG:
            c = ENG.find(sl[i]) + step
            if c >= 26:
                c -= 26
            slr += ENG[c]
        elif sl[i] == ' ':
            slr += ' '
elif t == 1 and a == 2:
    for i in range(len(sl)):
        if sl[i] in ru:
            c = ru.find(sl[i]) + step
            if c >= 33:
                c -= 33
            slr += ru[c]
        elif sl[i] in RU:
            c = RU.find(sl[i]) + step
            if c >= 33:
                c -= 33
            slr += RU[c]
        else:
            slr += sl[i]
if t == 2 and a == 1:
    for i in range(len(sl)):
        if sl[i] in eng:
            c = eng.find(sl[i]) - step
            if c < 0:
                c += 26
            slr += eng[c]
        elif sl[i] in ENG:
            c = ENG.find(sl[i]) - step
            if c < 0:
                c += 26
            slr += ENG[c]
        elif sl[i] == ' ':
            slr += ' '
elif t == 2 and a == 2:
    for i in range(len(sl)):
        if sl[i] in ru:
            c = ru.find(sl[i]) - step
            if c < 0:
                c += 33
            slr += ru[c]
        elif sl[i] in RU:
            c = RU.find(sl[i]) - step
            if c < 0:
                c += 33
            slr += RU[c]
        else:
            slr += sl[i]

print('\nПолученное преобразование: ' + slr)