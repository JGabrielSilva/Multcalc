c = '=====x====='
ps = 0
while True:
    c = int(input('Direita[] Esquerda[] '))
    if (c == 1) and (ps < 5):
        ps += 1
    else:
        ps -= 1
    print(ps)
print('fim')