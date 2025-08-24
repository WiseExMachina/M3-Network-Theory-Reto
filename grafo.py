import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Matriz de adyacencias como una lista de listas
adj_matrix_list = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
]

# Convertir la lista a un array de NumPy
adj_matrix = np.array(adj_matrix_list)

# Crear un grafo a partir de la matriz
G = nx.from_numpy_array(adj_matrix)

# --------------------------------------------------
## ANÁLISIS DE LA RED
# --------------------------------------------------

# 1. Calcular el grado de cada vértice.
grados_de_vertices = G.degree()
print("Grado de cada vértice (Nodo, Grado):")
print(list(grados_de_vertices))

# 2. Escribir la secuencia de grados.
secuencia_de_grados = sorted([d for n, d in grados_de_vertices], reverse=True)
print("\nSecuencia de grados (ordenada de mayor a menor):")
print(secuencia_de_grados)

# 3. Encontrar el diámetro de la red.
if nx.is_connected(G):
    diametro = nx.diameter(G)
    print(f"\nLa red está conectada.")
    print(f"El diámetro de la red es: {diametro}")
else:
    print("\nLa red no está conectada, por lo que no se puede calcular un único diámetro.")

# 4. Calcular y mostrar todas las distancias entre vértices.
print("\nDistancias entre todos los pares de nodos (caminos más cortos):")
distancias = dict(nx.all_pairs_shortest_path_length(G))
for nodo_origen, destinos in distancias.items():
    print(f"  Distancias desde el nodo {nodo_origen}: {destinos}")

print(f"\nBuscando los pares de nodos que definen el diámetro ({diametro}):")
for origen, destinos in distancias.items():
    for destino, distancia in destinos.items():
        if distancia == diametro and origen < destino:
            print(f"  - La distancia entre el nodo {origen} y el nodo {destino} es {diametro}.")

# 5. Encontrar la distribución de grados de la red.
print("\nDistribución de grados de la red:")
# nx.degree_histogram(G) crea una lista donde el índice es el grado y el valor es cuántos nodos tienen ese grado.
distribucion = nx.degree_histogram(G)
for grado, numero_de_nodos in enumerate(distribucion):
    # Imprimimos solo si hay al menos un nodo con ese grado.
    if numero_de_nodos > 0:
        print(f"  - Hay {numero_de_nodos} nodo(s) con grado {grado}.")


# --------------------------------------------------
## SECCIÓN DE DIBUJO DEL GRAFO
# --------------------------------------------------

# Generar las posiciones de los nodos
pos = nx.kamada_kawai_layout(G)

# Dibujar el grafo
plt.figure(figsize=(8, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='skyblue',
    node_size=1200,
    font_size=16,
    width=2,
    edge_color='gray'
)

# Guardar y mostrar el grafo
plt.title("Grafo con Layout Kamada-Kawai")
plt.savefig("graph_kamada_kawai.png")
plt.show()
