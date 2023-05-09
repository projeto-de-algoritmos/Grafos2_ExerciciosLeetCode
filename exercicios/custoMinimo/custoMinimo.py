import itertools
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Calcular a distância manhattan para cada par de pontos
        dist = {(i, j): abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                for i, j in itertools.combinations(range(len(points)), 2)}

        # Criar um grafo não-direcionado completo com as distâncias manhattan como pesos das arestas
        graph = [(i, j, dist[i, j]) for i, j in dist]
        graph.sort(key=lambda x: x[2])

        # Inicializar o vetor de componentes
        components = {i: i for i in range(len(points))}
        cost = 0

        # Executar o algoritmo de Kruskal
        for u, v, w in graph:
            if components[u] != components[v]:
                cost += w
                old_comp, new_comp = components[u], components[v]
                for i in range(len(points)):
                    if components[i] == old_comp:
                        components[i] = new_comp

        return cost