import os

caminho_original = os.getcwd()
arqvs_exists_diret = os.listdir()

for e in arqvs_exists_diret:
    novo_diret = e
    caminho_novo = os.path.join(caminho_original + "/" + e)
    if os.path.isdir(e):
        arqvs_exists_diret_e = os.listdir(caminho_novo)
        for a in arqvs_exists_diret_e:
            os.rename(caminho_novo + '/' + a, caminho_original + '/' + a)
        os.rmdir(e)

"""
caminho_original = os.getcwd()
lista_filt_past = [i for i in os.listdir(caminho_original) if os.path.isdir(i)]

for pasta in lista_filt_past:
    caminho = caminho_original + '/' + pasta
    arqvs = os.listdir(caminho)
    for arqv in arqvs:
        da_pasta = caminho + '/' + arqv
        para_pasta = caminho_original + '/' + arqv
        os.replace(da_pasta, para_pasta)
    os.rmdir(caminho)
"""