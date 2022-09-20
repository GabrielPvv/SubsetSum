from audioop import reverse
import random
import json
from timeit import default_timer as timer

def gera_lista():
    linha = []

    tamanhoLista = random.randint(2000000,4000000)#trabalhando com instâncias que tornam o problema NP-Dificil 

    for c2 in range(0, tamanhoLista):
         valor = random.randint(1,100)
         linha.append(valor)

    with open("teo.json", "w") as wfile:
        json.dump(linha, wfile)

    return linha

def get_lista():
    f = open('teo.json')
    data = json.load(f)
    return data


def get_TrocaPosicao(lista,k): # função para comparar a troca de posições no vetor inteiro ao invés da troca na solução (VND)

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
    


def get_GreedyFofo(lista, tamanho_lista, alvo):# Algoritmo guloso
    peso = 0
    contador = 0
    temp = 0
    opt = []
    lista_greedy = [] # lista temporaria pra nao fazer alteracoes na lista original 
    cont = 0
    lista_greedy = lista.copy()
    #print("lista greedy", lista_greedy)
    somatorio = alvo
    j = 0

    if(sum(lista) < alvo ): # verificando se o valor alvo pode ser atingido
        print("impossivel obter o valor alvo")
        return opt
    
    while((sum(opt)< alvo)):
        if(sum(opt) < alvo and contador == (tamanho_lista -1)):
            return opt
        while contador < tamanho_lista: 
            if(contador == (tamanho_lista - 1)):
                break

            if  (((sum(opt) + (lista_greedy[contador])) <= alvo) and (lista_greedy[contador] > 0)):
                temp = lista_greedy[contador] #salvo o valor em uma temporaria 
                lista_greedy[contador] = 0 #zero o valor que eu estou tirando da lista pra nao repetir ele depois
                opt.append(temp) #adiciono a temporaria no vetor opt
            contador = contador + 1 #intero o contador 
        
        if((sum(lista_greedy) == 0)): #percorri a lista toda, zerei tudo e cheguei ao final
            print(" valor alvo impossivel de ser encontrado com o guloso")
            return opt

    return opt 

def get_descentS(lista,otimo,l): # VND # IDEIA -> SALVAR A POSICAO  DA SOLUCAO PEGA ( AO RODAR O GREEDY ), E, AO INVES DE PERCORRER O VETOR
                                 # SO IR FAZENDO AS ALTERACOES NA POSICAO SALVA ( COM OS DEVIDOS INCREMENTOS)
    tamanho_lista = len(lista)
    descent = []
    i = 0
    j = 0
    opt = []
    
    descent = lista.copy()

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


def get_Vizinhos_Otimizadinhos(opt,lista,alvo): #Em construção.
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



def get_SubsetSum(lista, tamanho_lista, alvo):# Heuristica de Construção Inicial 
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


if __name__ == "__main__": # Main
    ### Caso 1 - Gerando lista e setando o alvo
    gera_lista() 
    lista = get_lista()
    alvo = 102 # alvo setado na mão para maior confiabilidade.
    tamanho_lista = len(lista)

    otimo = [] # vetor à ser armazenado a solução do guloso
    print("cheguei aqui, na main, vou rodar o greedy") #print para acompanhamento da evolução do algoritmo


    otimo = get_GreedyFofo(lista,tamanho_lista,alvo) # primeira interacao do guloso,
    vetorzinho = [] # vetor temporario
    troca = [] # vetor a ser armazenado a solução do k-swap
    k = 1 # variavel para os swaps de posicao na função de troca de posição
    l = 1 # variavel para a iteração do descent
    #f = 0 
    tempo = 0 # variavel para auxilio no controle do benchmark
    cont = 10 # variavel de parada do descent
    vetoraux = [] #vetor temporario
    vetor_temp = [] #vetor À ser armazenado a solução do descent
    
    print("iniciando o descent")
    start = timer() #iniciando o benchmark..

   
    while(l<cont):# rodo o greedy à cada iteração do VND e verifico se a solução é melhor, se for, é a nova solução.
        descent = get_descentS(lista,otimo,l)
        #while(f < len(descent)):
            #vetoraux.append(descent[f])
            #f = f + 1 
        print("Rodando o descent, iteracao : ", l )
        vetoraux = descent.copy()

        l = l + 1
        vetoraux = get_GreedyFofo(descent,tamanho_lista,alvo)
        if(len(vetor_temp) < len(vetoraux)): # local onde faço a verificação de tamanho dos dois vetores, buscando o maior vetor.
            vetor_temp = vetoraux.copy()

        if(len(vetor_temp) > len(otimo) and l+1 == cont):  
            break

    end = timer()
    print("tempo de execucao da funcao descent : " ,end - start)
    tempo = end - start   
    
# fim while com o incremento no l, objetivo é switar as posiçoes da primeira soluçao ate achar uma melhor
   
 
    trocador = []
    trocador = lista.copy()

    vectork = []
    print("iniciando o k swap")

   
    while(k<10): #podemos aumentar ou diminuir o cont livremente
        print("Rodando o k-swap, interacao : ", k )
        if(sum(lista)< alvo): # protecao pra ver se a lista chega no valor alvo
            break
        trocador = get_TrocaPosicao(trocador,k) #funcao pra trocar a posicao com um raio de tamanho k na lista
        k = k+1 # aumento o raio da vizinhança
        troca = get_GreedyFofo(trocador,tamanho_lista,alvo) # agora vou interagir o guloso com as posicoes trocadas do vetor em um raio de k
        
        if(len(vectork) < len(troca)): # vendo se achei um vetor melhor que na primeira interacao do guloso ( otimo )
            vectork = troca.copy()

    end = timer()
    print("tempo de execucao da funcao: k-swap" , (end - start) - tempo)   


    vetorzinho = lista.copy()
    vetorzinho.sort(reverse=True)
    #print("vetor original = ", lista)
    #print("vetor ordenado para melhor visualização = ", vetorzinho)

    if(sum(vectork) == alvo or sum(otimo) == alvo or sum(vetor_temp) == alvo):
        print("foi encontrado um subset correspondente ao alvo")
    else:
        print("nenhum subset foi encontrado")

    print("greedy = ", otimo)
    print("k-swap = ", vectork)
    print("Descent : ", vetor_temp)
    print("soma do Greedy = ",sum(otimo))
    print("soma do K-swap = ",sum(vectork)) 
    print("soma do Descent  = ", sum(vetor_temp))
    print("tamanho do Descent= " , len(vetor_temp))
    print("tamanho do Greedy = ", len(otimo))
    print("tamanho do K-swap = ", len(vectork))
    print("target = ", alvo)
    print("numero de trocas no Descent = ", l)
    print("tamanho da lista", tamanho_lista)
    print("numero de trocas no K-swap =", k)

   
    # print("lista sorteada", lista)
    ## Caso 2 - Lista pré definida e alvo pré definido
    # lista = [4, 8, 3, 2]
    # alvo = 16
    # tamanho_lista = len(lista)
    
    #if (get_SubsetSum(lista, tamanho_lista, alvo) == True):
        #print("Foi encontrado um subconjunto com o alvo dado",)
    #else:
        #print("Não encontrado um subconjunto com o alvo dado")