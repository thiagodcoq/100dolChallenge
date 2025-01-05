
participantes = ['Andre', 'Cadu', 'Igor', 'JP', 'Rafael', 'Thiago']
contagem_votos = [0,0,0,0,0,0] # Lista de votos cada posicao se refere ao participante de mesma posicao

def busca(atributo,lista):
    for pos, nome in enumerate(lista):
        if nome == atributo:
            return pos

def campeao(lista):
    maior = 0
    x = 0
    for pos,valor in enumerate(lista):
        if valor>maior:
            maior=valor
            x=pos
    return x
    
n=5 # Number of voters

for i in range(n):
    print("-----Insira seu Top3!-----")
    name = str(input("Primeiro lugar: "))
    posicao = busca(name,participantes)
    contagem_votos[posicao]+=4
    name2 = str(input("Segundo lugar: "))
    posicao = busca(name2,participantes)
    contagem_votos[posicao]+=2
    name1 = str(input("Segundo lugar: "))
    posicao = busca(name1,participantes)
    contagem_votos[posicao]+=1


print(contagem_votos)
index_campeao=campeao(contagem_votos)
print("===CAMPEAO===")
print(f'Parabens {participantes[index_campeao]}, voce é o vencedor da disputa!')

