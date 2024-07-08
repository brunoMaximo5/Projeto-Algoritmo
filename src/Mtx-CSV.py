import csv
import random

# Caminho para o arquivo Matrix Market
matrix_market_file_path = 'C:/Users/Maximo/Desktop/Projeto-Algoritmo/Projeto-Algoritmo/1138_bus/1138_bus.mtx'
# Caminho para o arquivo CSV de saída
csv_file_path = 'C:/Users/Maximo/Desktop/Projeto-Algoritmo/Projeto-Algoritmo/network.csv'

# Função para ler o arquivo Matrix Market e converter para CSV
def converter_matrix_market_para_csv(matrix_market_file_path, csv_file_path):
    with open(matrix_market_file_path, 'r') as infile:
        lines = infile.readlines()
    
    # Ignorar os comentários e cabeçalhos do Matrix Market
    data_lines = [line for line in lines if not line.startswith('%')]

    # Extraia o número de linhas, colunas e não zeros
    nrows, ncols, nnz = map(int, data_lines[0].split())
    
    edges = []
    for line in data_lines[1:]:
        try:
            origem, destino = map(int, line.split())
            if origem != destino:  # Ignorar auto-loops
                peso = random.uniform(1.0, 10.0)  # Adiciona um peso aleatório entre 1.0 e 10.0
                edges.append((origem, destino, peso))
                edges.append((destino, origem, peso))  # Para grafos não direcionados
        except ValueError:
            print(f"Ignorando linha inválida: {line.strip()}")
            continue
    
    # Escrever os dados no formato CSV
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['origem', 'destino', 'peso'])
        for edge in edges:
            csv_writer.writerow(edge)

# Executar a função de conversão
converter_matrix_market_para_csv(matrix_market_file_path, csv_file_path)
