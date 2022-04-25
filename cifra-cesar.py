'''
SITUAÇÕES:
    a -> 0
    d -> 5 --> index(a) + index(d)
    r = index(d)

---------------------------------------
0 -- 26 = 27

(letra + deslocamento) - 26

28
'''

# função de cifragem
def cifra(frs):
    min_ascii, max_ascii = 31, 1000
    nv_desl, calc = 0, 0


    for ltr in frs:
        calc = ord(ltr) + deslocamento

        # deslocamento positivo
        if calc > max_ascii:
            nv_desl = (calc-max_ascii)+min_ascii

        # deslocamento negativo
        elif calc <= min_ascii:
            nv_desl = (calc+max_ascii) - min_ascii

        # dentro do intervalo(31~126)
        else:
            nv_desl = calc

        print(chr(nv_desl), end='')

    print()


frase = input("Digite a palavra/frase: ")
deslocamento = int(input('Valor do Deslocamento(Diferente de 0(zero)): '))


# validacao do deslocamento
if deslocamento != 0:
    if deslocamento > 0:
        print('Cifrando: ', end='')
    else:
        print('Descifrando: ', end='')
    cifra(frase)
else:
    print('Valor tem que ser diferente de 0(zero)!!!')