
import heapq

def dijkstra_manual(G, origem):
    distancias = {no: float('inf') for no in G.nodes}
    distancias[origem] = 0
    caminho = {no: None for no in G.nodes}
    pq = [(0, origem)]
    
    while pq:
        distancia_atual, no_atual = heapq.heappop(pq)
        
        if distancia_atual > distancias[no_atual]:
            continue
        
        for vizinho in G.neighbors(no_atual):
            peso = G[no_atual][vizinho]['weight']
            distancia = distancia_atual + peso
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho[vizinho] = no_atual
                heapq.heappush(pq, (distancia, vizinho))
    
    return distancias, caminho

def encontrar_caminho(distancias, caminho, origem, destino):
    if distancias[destino] == float('inf'):
        return None
    
    caminho_final = []
    no_atual = destino
    while no_atual is not None:
        caminho_final.append(no_atual)
        no_atual = caminho[no_atual]
    
    caminho_final.reverse()
    return caminho_final

