from random import randint

def gerador_cpf():
    gerador = True

    while gerador == True:
        cpfgerado = str(randint(10000000000, 99999999999))
        cpf = cpfgerado
        x = []
        y = 10
        z = 0
        l = []
        s = 0

        for v in cpf:
            x.append(v)

        x.pop()
        x.pop()

        for y in range(10, 1, -1):
            a = int(x[z]) * y
            l.append(a)
            s = s + a
            y -= 1
            z += 1

        u1 = (11 - (int(s) % 11))

        if u1 > 9:
            u1 = 0
            x.append(str(u1))
        else:
            x.append(str(u1))

        s = 0
        y = 0
        z = 0

        for y in range(11, 1, -1):
            a = int(x[z]) * y
            l.append(a)
            s = s + a
            y -= 1
            z += 1

        u2 = (11 - (int(s) % 11))

        if u2 > 9:
            u2 = 0
            x.append(str(u2))
        else:
            x.append(str(u2))

        cpf2 = ''.join(x)

        if cpf2 == cpf:
            if cpfgerado == cpfgerado[1] * len(cpfgerado):
                return False
                gerador = True
            else:
                return cpfgerado
                gerador = False

        else:
            gerador = True

def valida_cpf(cpf_digitado):
    cpf = str(cpf_digitado)

    if not cpf or len(cpf) < 11:
        return False

    cpf = cpf.split('.')
    cpf = ''.join(cpf)
    cpf = cpf.split('-')
    cpf = ''.join(cpf)
    x = []
    y = 10
    z = 0
    l = []
    s = 0

    for v in cpf:
        x.append(v)

    x.pop()
    x.pop()

    for y in range(10, 1, -1):
        a = int(x[z]) * y
        l.append(a)
        s = s + a
        y -= 1
        z += 1

    u1 = (11 - (int(s) % 11))

    if u1 > 9:
        u1 = 0
        x.append(str(u1))
    else:
        x.append(str(u1))

    s = 0
    y = 0
    z = 0

    for y in range(11, 1, -1):
        a = int(x[z]) * y
        l.append(a)
        s = s + a
        y -= 1
        z += 1

    u2 = (11 - (int(s) % 11))

    if u2 > 9:
        u2 = 0
        x.append(str(u2))
    else:
        x.append(str(u2))

    cpf2 = ''.join(x)

    if cpf2 == cpf:
        return True

    else:
        return False