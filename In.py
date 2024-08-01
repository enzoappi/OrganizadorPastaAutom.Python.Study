import os

arqvs_exists_diret = os.listdir()

exts_existentes = []
for e in arqvs_exists_diret:
    temp = e.split('.')
    if temp[-1] not in exts_existentes and temp[-1]!='py':
        exts_existentes.append(temp[-1])

for e in exts_existentes:
    os.mkdir(e)
    for i in arqvs_exists_diret:
        temp = i.split('.')
        if temp[-1] == e:
            os.rename(i, e + '/' + i)

"""
caminho_original = os.getcwd()
lista_completa_arqvs = os.listdir(caminho_original)

lista_filt_arqvs = [i for i in lista_completa_arqvs if os.path.isfile(i) and '.py' not in i]
exts_arqvs = list(set([i.split('.')[1] for i in lista_filt_arqvs]))

for tipo_arqv in exts_arqvs:
    os.mkdir(tipo_arqv)

for arqv in lista_filt_arqvs:
    da_pasta = os.path.join(caminho_original, arqv)
    para_pasta = os.path.join(caminho_original, arqv.split('.')[-1], arqv)

    os.replace(da_pasta, para_pasta)
"""