import sqlite3
import networkx as nx

def carregar_grafo(db_path):
    G = nx.Graph()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT origem, destino, peso FROM grafo")
        rows = cursor.fetchall()
        
        for row in rows:
            origem, destino, peso = row[0], row[1], row[2]
            G.add_edge(origem, destino, weight=peso)
    except sqlite3.Error as e:
        print(f"Erro ao carregar o grafo: {e}")
    finally:
        conn.close()
        
    print(f"Grafo carregado com nós: {G.nodes}, arestas: {G.edges}")
    return G
