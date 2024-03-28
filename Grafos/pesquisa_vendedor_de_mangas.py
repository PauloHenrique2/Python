from collections import deque

def pessoa_e_vendedor(nome):
 return nome[-1] == 'm'

grafo = {}
grafo["voce"] = ["alice","bob","claire"]
grafo["bob"] = ["anuj","peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom","jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []


def pesquisar(nome):
 fila_de_pesquisa = deque()
 fila_de_pesquisa += [nome]
 verificadas = set()  ## Aqui armazenamos as pessoas que já foram pesquisadas 

 while fila_de_pesquisa:
  pessoa = fila_de_pesquisa.popleft() 
   
  if pessoa in verificadas:  ## Pesquisa a pessoa informada apenas se ela não tiver sido pesquisada
    continue
  
  if pessoa_e_vendedor(pessoa):
    print (pessoa + " é um vendedor de manga!")
    return True
  fila_de_pesquisa += grafo[pessoa]
  verificadas.add(pessoa)  ## Marca a pessoa como verificada
 return False

pesquisar("voce")
