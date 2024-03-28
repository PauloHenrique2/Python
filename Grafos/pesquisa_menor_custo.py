## Criação da primeira tabela hash map (grafo)

grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}


## Criação da segunda tabela hash map (custos)

infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

## Criação da terceira tabela hash map (pais)

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    
    for node in custos:  # Percorre todos os nós
        custo = custos[node]
        
        if custo < custo_mais_baixo and node not in processados: # Se é o menor custo até o momento e ainda não tiver sido processado
            custo_mais_baixo = custo  # Atribui o nó como o de menor custo
            nodo_custo_mais_baixo = node
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos)  ## Encontra o nó que ainda não foi processado

while nodo is not None:  ## Se você processou todos os nós, esse loop chegou ao fim 
 custo = custos[nodo]
 vizinhos = grafo[nodo]
 
 for n in vizinhos.keys():
  novo_custo = custo + vizinhos[n]

  if custos[n] > novo_custo:  ## Se é mais barato ir até esse vizinho através desse nó...
      custos[n] = novo_custo  ## Atualize o custo desse nó
      pais[n] = nodo    ## Esse nó se torna o novo pai para esse vizinho

 processados.append(nodo)  ## Marque o nó como processado
 nodo = ache_no_custo_mais_baixo(custos)  ## Encontre o próximo nó para processar e entre no loop.

print ("Custo do início até cada nó: ")
print (custos)