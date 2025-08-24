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



# 6. Calcular el coeficiente de agrupamiento para nodos de interés.
print("\nCoeficiente de agrupamiento (Clustering):")
# Calculamos para el nodo 3 (uno de los más conectados) y los que sugeriste (4 y 7)
# Los resultados numéricos exactos dependerán de tu matriz de adyacencias.
clustering_3 = nx.clustering(G, 3)
clustering_4 = nx.clustering(G, 4)
clustering_7 = nx.clustering(G, 7)

print(f"  - Coeficiente del nodo 3: {clustering_3:.4f}")
print(f"  - Coeficiente del nodo 4: {clustering_4:.4f}")
print(f"  - Coeficiente del nodo 7: {clustering_7:.4f}")

# Comparar los coeficientes de los nodos 4 y 7
print("\n¿Cuál tiene un coeficiente mayor, el 4 o el 7?")
if clustering_4 > clustering_7:
    print("  -> El nodo 4 tiene un coeficiente de agrupamiento mayor.")
elif clustering_7 > clustering_4:
    print("  -> El nodo 7 tiene un coeficiente de agrupamiento mayor.")
else:
    print("  -> Los nodos 4 y 7 tienen el mismo coeficiente de agrupamiento.")

    # 7. Calcular la centralidad de intermediación (Betweenness Centrality).
print("\nCentralidad de Intermediación:")
# Esto calcula la centralidad para todos los nodos y la guarda en un diccionario.
centralidad = nx.betweenness_centrality(G)

# Mostramos la de los nodos de interés
print(f"  - Centralidad del nodo 4: {centralidad[4]:.4f}")
print(f"  - Centralidad del nodo 7: {centralidad[7]:.4f}")

# Comparamos cuál de los dos tiene más centralidad
print("\n¿Cuál de los dos tiene más centralidad, el 4 o el 7?")
if centralidad[4] > centralidad[7]:
    print("  -> El nodo 4 tiene una mayor centralidad de intermediación.")
elif centralidad[7] > centralidad[4]:
    print("  -> El nodo 7 tiene una mayor centralidad de intermediación.")
else:
    print("  -> Los nodos 4 y 7 tienen la misma centralidad de intermediación.")


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
