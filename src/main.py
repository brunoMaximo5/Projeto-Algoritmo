import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from grafo import carregar_grafo
from dijkstra import dijkstra_manual, encontrar_caminho

def mostrar_resultado(melhor_caminho, origem, destino):
    if melhor_caminho:
        resultado = f"O melhor caminho de {origem} até {destino} é: {melhor_caminho}"
    else:
        resultado = f"Não existe caminho de {origem} até {destino}"
    messagebox.showinfo("Resultado", resultado)

def visualizar_grafo(G, melhor_caminho):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    if melhor_caminho:
        path_edges = list(zip(melhor_caminho, melhor_caminho[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=melhor_caminho, node_color='red')
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.show()

def calcular_caminho():
    origem = int(entry_origem.get())
    destino = int(entry_destino.get())
    distancias, caminho = dijkstra_manual(G, origem)
    melhor_caminho = encontrar_caminho(caminho, origem, destino)
    mostrar_resultado(melhor_caminho, origem, destino)
    visualizar_grafo(G, melhor_caminho)

# Configurar a interface gráfica
root = tk.Tk()
root.title("Cálculo de Caminho Mais Curto")

label_origem = tk.Label(root, text="Digite o nó de origem:")
label_origem.pack()
entry_origem = tk.Entry(root)
entry_origem.pack()

label_destino = tk.Label(root, text="Digite o nó de destino:")
label_destino.pack()
entry_destino = tk.Entry(root)
entry_destino.pack()

botao_calcular = tk.Button(root, text="Calcular Caminho", command=calcular_caminho)
botao_calcular.pack()

# Carregar o grafo
banco_dados = "C:/Users/Maximo/Desktop/Projeto-Algoritmo/Projeto-Algoritmo/data/grafo.db"
G = carregar_grafo(banco_dados)

root.mainloop()
