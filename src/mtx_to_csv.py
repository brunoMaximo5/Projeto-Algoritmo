from scipy.io import mmread
import csv

# Caminho para o arquivo MTX
mtx_file_path = 'C:\\Users\\Maximo\\Desktop\\Projeto-Algoritmo\\Projeto-Algoritmo\\data\\bio-celegans.mtx'

# Caminho para o arquivo CSV de saída
csv_file_path = 'data\\network.csv'

def converter_mtx_para_csv(mtx_file_path, csv_file_path):
    # Ler o arquivo MTX
    mtx_data = mmread(mtx_file_path)
    
    # Abrir um arquivo CSV para escrita
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        
        # Escrever cabeçalho
        writer.writerow(['Origem', 'Destino', 'Peso'])
        
        # Escrever os dados linha por linha
        for i, j, v in zip(mtx_data.row, mtx_data.col, mtx_data.data):
            writer.writerow([i + 1, j + 1, v])  # +1 para converter índices baseados em zero para baseados em um (se necessário)

if __name__ == "__main__":
    converter_mtx_para_csv(mtx_file_path, csv_file_path)
