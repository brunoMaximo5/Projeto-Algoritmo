# main.py

import tkinter as tk
from tkinter import simpledialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt
import sqlite3
from grafo import carregar_grafo
from dijkstra import dijkstra_manual, encontrar_caminho

def main():
    # Definir o caminho para o banco de dados
    db_path = 'data/grafo.db'
    
    # Carregar o grafo a partir do banco de dados
    G = carregar_grafo(db_path)
    
    # Função para calcular o caminho usando Dijkstra
    def calcular_caminho():
        origem = int(simpledialog.askstring("Origem", "Digite o nó de origem:"))
        destino = int(simpledialog.askstring("Destino", "Digite o nó de destino:"))

        try:
            distancias, caminho = dijkstra_manual(G, origem)
            caminho_final = encontrar_caminho(distancias, caminho, origem, destino)  # Ajustado para quatro argumentos
            if caminho_final is not None:
                caminho_str = ' -> '.join(map(str, caminho_final))
                messagebox.showinfo("Resultado", f"Menor caminho: {caminho_str}\nDistância: {distancias[destino]}")
            else:
                messagebox.showwarning("Caminho não encontrado", "Não há caminho entre os nós selecionados.")
        except nx.NetworkXError as e:
            messagebox.showerror("Erro", str(e))

    # Interface gráfica simples
    root = tk.Tk()
    root.title("Calculadora de Caminho Mínimo")
    
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    button_calcular = tk.Button(frame, text="Calcular Caminho", command=calcular_caminho)
    button_calcular.pack(side=tk.LEFT)

    button_sair = tk.Button(frame, text="Sair", command=root.destroy)
    button_sair.pack(side=tk.RIGHT)

    root.mainloop()

if __name__ == "__main__":
    main()