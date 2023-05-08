import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Criar dicionário de adjacência
        adj = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            adj[u].append((v, w))

        # Inicializar o vetor de distância com infinito
        dist = {i: float('inf') for i in range(1, n+1)}

        # Inicializar a heap com o nó de origem
        heap = [(0, k)]
        dist[k] = 0

        # Executar o algoritmo de Dijkstra
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))

        # Verificar se todos os nós receberam o sinal
        max_dist = max(dist.values())
        if max_dist == float('inf'):
            return -1
        else:
            return max_dist