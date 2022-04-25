def quebrarString(frs, line):
    frase_descripto = [frs[qbr*line:qbr*line + line:] for qbr in range(line)]

    return frase_descripto

def criptar(frs):
    frs_cripto = []
    frs = frs.ljust(caracteres, "*")
    
    for ltr in chave_ord:
        frs_cripto += [frs[chave.index(ltr)::tam_chave]]

    return ''.join(frs_cripto)


def descriptar(frs):
    frase_quebrada = quebrarString(frs, qtd_linhas)
    frs_descripto = []
    
    for col in range(qtd_linhas):
        for key in chave_ord:
            frs_descripto += frase_quebrada[chave.index(key)][col]

    return ''.join(frs_descripto)


if "__main__" == __name__:

    from math import ceil

    opcao = input("Criptar(c) ou Descriptar(d): ").lower()

    if(opcao not in ['c', 'd', 'criptar', 'descriptar']):
        exit(f"Opção não disponível: {opcao!r}")

    '''
    O Iftm É Um Bom Lugar Para Estudar
       L  dOmm rauf ogasrIÉBuPEatUmart*'''

    chave = list(input('Chave: ').lower())
    frase = input('Frase: ')

    chave_ord = chave[:]
    chave_ord.sort()

    # tamanho da chave e frase
    tam_chave, tam_frase = len(chave), len(frase)

    if(tam_chave > tam_frase):
        exit(f'Tamanho da chave deve ser menor que a frase')

    # qtd de linhas(arredondamento superior)
    qtd_linhas = ceil(tam_frase / tam_chave)

    # qtd de caracteres
    caracteres = tam_chave * qtd_linhas

    if(opcao == 'c' or opcao == 'criptar'):
        resultado = criptar(frase)

    else:
        resultado = descriptar(frase).replace('*', '')

    print(f'"{resultado}"')