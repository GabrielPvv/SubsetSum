from audioop import reverse
import random
import json

def gera_lista():
    linha = []

    tamanhoLista = random.randint(100,100000)

    for c2 in range(0, tamanhoLista):
         valor = random.randint(0,50)
         linha.append(valor)

    with open("teo.json", "w") as wfile:
        json.dump(linha, wfile)

    return linha

def get_lista():
    f = open('teo.json')
    data = json.load(f)
    return data


def get_TrocaPosicao(lista,k):

    i = 0
    temp = 0
    tamanho_lista = len(lista)
  
    while(i<tamanho_lista):
        if(k + i < tamanho_lista):
            temp =  lista[i]
            lista[i] = lista[k+i]
            lista[k+i] = temp
        i = i+1

    return lista
    
def get_GreedyFofo(lista, tamanho_lista, alvo):
    peso = 0
    contador = 0
    temp = 0
    opt = []
    lista_greedy = [] # lista temporaria pra nao fazer alteracoes na lista original 
    cont = 0
    while(cont<tamanho_lista):
        lista_greedy.append(lista[cont])
        cont = cont+1


    somatorio = alvo
    j = 0

    if(sum(lista) < alvo ): # verificando se o valor alvo pode ser atingido
        print("impossivel obter o valor alvo")
        return opt
    

    while((sum(opt)< alvo)):
        while contador < tamanho_lista: 
            if  (((sum(opt) + (lista_greedy[contador])) <= alvo) and (lista_greedy[contador] > 0)):
                temp = lista_greedy[contador] #salvo o valor em uma temporaria 
                lista_greedy[contador] = 0 #zero o valor que eu estou tirando da lista pra nao repetir ele depois
                opt.append(temp) #adiciono a temporaria no vetor opt
            contador = contador + 1 #intero o contador 
        
        if((sum(lista_greedy) == 0)): #percorri a lista toda, zerei tudo e cheguei ao final
            print(" valor alvo impossivel de ser encontrado com o guloso")
            return opt

    return opt 

def get_descentS(lista,otimo,l):
    tamanho_lista = len(lista)
    descent = []
    i = 0
    j = 0
    opt = []
    
    while(i<tamanho_lista):
        descent.append(lista[i])
        i = i+1

    while(j<len(otimo)):
        opt.append(otimo[j])
        j = j+1

    #descent.sort(reverse = True)
    #opt.sort(reverse = True)
    cont = 0
    cont2 = 0
    while(cont < len(opt) and cont2 + l < len(descent)):

        while(cont2 < len(descent) and cont2 + l < len(descent) ):

            if(opt[cont] == descent[cont2]):
                temp = descent[cont2+l] 
                descent[cont2+l] = opt[cont]
                descent[cont2] = temp
                cont =  cont+1
                if(cont == len(opt)):
                    break
            cont2 = cont2+1

        if(cont == len(opt)):
                    break

 
    return descent


def get_Vizinhos_Otimizadinhos(opt,lista,alvo):
  troca = [] 
  new_Lista = []
  new_list = lista
  new_lista = list(new_list)
  # p.append(new_lista)
  tamanho_opt = len(opt)
  tamanho_new_lista = len(new_lista)

  i = 0
  j = 0
  k = 1
  tempositiva = 0
  sair = 0
  continho = 0
  while(sair < 1 ):
    while(i < tamanho_new_lista):
      print("To aqui no loop heim")
      if((new_lista[i] == opt[j])):
          continho = i+k
          if(continho> 0 and new_lista[continho]>0 ):
            tempositiva = new_lista[continho]
            new_lista[continho] = new_lista[i+k] # trocando os valores de lugar no vetor
            new_lista[i] = tempositiva           # trocando os valores de lugar no vetor
            
            print("i = ", i)
            print("k = ", k)
            print("tempositiva recebeu = ", tempositiva)
            if(((tempositiva+sum(troca)) < alvo)): # protegendo pro valor total da troca nao passar do alvo
              troca.append(tempositiva)
              tempositiva = 0
            j=j+1

            if((j+1)==(len(opt))): # protegendo pra nao acessar valor inválido do opt
                j = 0
    
      i = i+1

    if((sum(troca) >= sum(opt)) and (len(troca) >= len(opt))): # aqui será se acharmos uma soma melhor
        print("realizou a troca com o k = ", k ) 
        return troca
    i = 0
    k = k+1
    if(k <=  5 ): # aqui será se percorremos toda a vizinhança e nao acharmos uma combinação melhor
        i = 0
        continho = 0
        k = k+1
        print("percorreu até o k = ", k)
        print("aqui acabou")
    if(k > 6):
        return troca 



def get_SubsetSum(lista, tamanho_lista, alvo):
    # Casos Bases
    if (alvo == 0):
        return True
    if (tamanho_lista == 0 and alvo != 0):
        return False
    #Se o ultimo elemento for maior que o alvo, ignora
    if (lista[tamanho_lista - 1] > alvo):
        return get_SubsetSum(lista, tamanho_lista - 1, alvo);

    #Senão, verificar se a soma pode ser obtida incluindo ou não o último elemento
    return get_SubsetSum(
        lista, tamanho_lista - 1, alvo) or get_SubsetSum(
        lista, tamanho_lista - 1, alvo - lista[tamanho_lista - 1])


if __name__ == "__main__":
    ### Caso 1 - Gerando lista e setando o alvo
    gera_lista()
    lista = get_lista()
    alvo = 100
    tamanho_lista = len(lista)

    otimo = []

    otimo = get_GreedyFofo(lista,tamanho_lista,alvo) # primeira interacao do guloso,

    troca = []
    k = 1
    l = 2
    f = 0
    vetoraux = []

    descent = get_descentS(lista,otimo,l)
    
    while(l<(tamanho_lista-1)):# o codigo aguenta valores maiores que isso, porem demora e nao muda nada (aqui e onde eu faço o switch de l posicoes no vetor)

        descent = get_descentS(lista,otimo,l)
        while(f < len(descent)):
            vetoraux.append(descent[f])
            f = f + 1 

        l = l + 1
        vetoraux = get_GreedyFofo(descent,tamanho_lista,alvo)
        if(len(vetoraux) > len(otimo)):
            break

        
# fim while com o incremento no l, objetivo é switar as posiçoes da primeira soluçao ate achar uma melhor
    


    while(k<20): #podemos aumentar ou diminuir o k livremente
        if(sum(lista)< alvo): # protecao pra ver se a lista chega no valor alvo
            break
        lista = get_TrocaPosicao(lista,k) #funcao pra trocar a posicao com um raio de tamanho k na lista
        k = k+1 # aumento o raio da vizinhança
        troca = get_GreedyFofo(lista,tamanho_lista,alvo) # agora vou interagir o guloso com as posicoes trocadas do vetor em um raio de k
        if(len(troca) > len(otimo)): # vendo se achei um vetor melhor que na primeira interacao do guloso ( otimo )
            break
    #troca = get_GreedyFofo(lista,tamanho_lista,alvo)
    # troca  = get_Vizinhos_Otimizadinhos(otimo,lista,alvo)


    
    print("otimo = ", otimo)
    print("troca = ", troca)
    print("descend swap vector : ", vetoraux)
    print("soma do guloso = ",sum(otimo))
    print("soma da troca = ",sum(troca)) # o ideal é que aqui resulte em um TAMANHO maior que o  do ótimo com a mesma soma
    print("soma do vetor com a troca de pos = ", sum(vetoraux))
    print("tamanho do vetor com a troca de pos = " , len(vetoraux))
    print("tamanho do guloso = ", len(otimo))
    print("tamanho da troca = ", len(troca))
    print("tamanho da lista = ", tamanho_lista)
    print("alvo = ", alvo)
    print("numero de trocas de posicoes ate encontrar uma solução melhor = ", l)
    print("k-swaps feitos para o vetor de troca ser melhor que o guloso =", k-1)

    # print("lista sorteada", lista)
    ## Caso 2 - Lista pré definida e alvo pré definido
    # lista = [4, 8, 3, 2]
    # alvo = 16
    # tamanho_lista = len(lista)
    
    #if (get_SubsetSum(lista, tamanho_lista, alvo) == True):
        #print("Foi encontrado um subconjunto com o alvo dado",)
    #else:
        #print("Não encontrado um subconjunto com o alvo dado")