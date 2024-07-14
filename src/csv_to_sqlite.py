import sqlite3
import csv

# Caminho para o arquivo CSV e banco de dados
csv_file_path = 'C:\\Users\\Maximo\\Desktop\\Projeto-Algoritmo\\Projeto-Algoritmo\\data\\network.csv'

db_file_path = 'C:\\Users\\Maximo\\Desktop\\Projeto-Algoritmo\\Projeto-Algoritmo\\data\\grafo.db'


def criar_banco_de_dados(db_file):
    conn = sqlite3.connect(db_fil:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Criar a tabela 'grafo' se não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS grafo (
                        origem INTEGER,
                        destino INTEGER,
                        peso REAL
                    )''')
    
    conn.commit()
    conn.close()

def inserir_dados_csv_no_banco(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Pule o cabeçalho se houver
        
        for row in csvreader:
            try:
                origem, destino, peso = map(float, row[0].split())
                cursor.execute("INSERT INTO grafo (origem, destino, peso) VALUES (?, ?, ?)", (origem, destino, peso))
            except ValueError:
                print(f"Linhas ignoradas devido a formato incorreto: {row}")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_banco_de_dados(db_file_path)
    inserir_dados_csv_no_banco(csv_file_path, db_file_path)
