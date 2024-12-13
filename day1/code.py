def calcDistance(caminhoArquivo):
    listaEsquerda = []
    listaDireita = []
    
    # Le o arquivo e separa as colunas em duas listas
    with open(caminhoArquivo) as arquivo:
        for linha in arquivo:
            numeros = linha.split()
            listaEsquerda.append(int(numeros[0]))
            listaDireita.append(int(numeros[1]))
    
    # Ordena as listas
    esquerdaOrdenada = sorted(listaEsquerda)
    direitaOrdenada = sorted(listaDireita)
    
    # Calcula a soma das distancias
    distanciaTotal = sum(abs(e - d) for e, d in zip(esquerdaOrdenada, direitaOrdenada))
    
    return distanciaTotal

print(calcDistance(r'C:\Users\x\Desktop\AoC\day1input.txt'))
