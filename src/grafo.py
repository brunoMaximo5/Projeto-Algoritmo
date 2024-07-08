import sqlite3
import networkx as nx

def carregar_grafo(db_path):
    G = nx.Graph()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT origem, destino, peso FROM grafo")
    rows = cursor.fetchall()
    for row in rows:
        G.add_edge(row[0], row[1], weight=row[2])
    conn.close()
    return G
