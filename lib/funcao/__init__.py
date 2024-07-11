def corrente(p):
    v = 380
    i = p/v
    im = round(i, 2)
    return im


def fator_serviço(corren):
    fs = corren * 1.25
    fator = round(fs, 2)
    return fator
