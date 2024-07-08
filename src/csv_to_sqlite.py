import sqlite3
import csv
import os

# Caminho para o arquivo CSV gerado
csv_file_path = 'C:/Users/Maximo/Desktop/Projeto-Algoritmo/Projeto-Algoritmo/data/network.csv'
# Caminho para o banco de dados SQLite
db_file_path = 'C:/Users/Maximo/Desktop/Projeto-Algoritmo/Projeto-Algoritmo/data/grafo.db'

# Certifique-se de que o diretório para o banco de dados existe
os.makedirs(os.path.dirname(db_file_path), exist_ok=True)

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# Criar a tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS grafo (
    origem INTEGER,
    destino INTEGER,
    peso REAL
)
''')

# Ler o arquivo CSV e inserir os dados na tabela
with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Pular o cabeçalho
    for row in csv_reader:
        cursor.execute('INSERT INTO grafo (origem, destino, peso) VALUES (?, ?, ?)', (int(row[0]), int(row[1]), float(row[2])))

conn.commit()
conn.close()
