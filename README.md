Projeto de Algoritmos
=====================

Descrição
---------
Este projeto implementa o algoritmo de Dijkstra para calcular o menor caminho entre dois pontos em um grafo. Os dados do grafo são importados de um banco de dados real e a aplicação inclui uma interface gráfica para visualização e interação com o grafo.

Estrutura do Projeto
---------------------
data/: Contém o arquivo de banco de dados e o arquivo network.csv.
  - bio-celegans.mtx: Arquivo original no formato .mtx.
  - network.csv: Arquivo convertido no formato .csv.
  - grafo.db: Banco de dados SQLite com os dados do grafo.

src/: Contém os arquivos de código fonte.
  - mtx_to_csv.py: Converte arquivos .mtx para .csv.
  - csv_to_sqlite.py: Converte arquivos .csv para um banco de dados SQLite.
  - dijkstra.py: Implementa o algoritmo de Dijkstra.
  - grafo.py: Carrega o grafo do banco de dados.
  - main.py: Contém a aplicação GUI usando Tkinter.

Requisitos
----------
- Python 3.x
- Bibliotecas:
  - scipy
  - sqlite3
  - networkx
  - matplotlib
  - tkinter

Para instalar as dependências, execute:

```bash
pip install scipy networkx matplotlib

## Como Usar

1. **Converter o arquivo .mtx para .csv:**
   Execute o script `mtx_to_csv.py` para converter o arquivo .mtx para .csv.

2. **Converter o arquivo .csv para um banco de dados SQLite:**
   Execute o script `csv_to_sqlite.py` para criar e preencher o banco de dados SQLite.

3. **Executar a aplicação GUI:**
   Execute o script `main.py` para iniciar a aplicação GUI.
   Na interface gráfica, insira os nós de origem e destino para calcular o menor caminho usando o algoritmo de Dijkstra.

## Vídeo de Apresentação
[Link para o vídeo de apresentação](coloque aqui o link do seu vídeo)
