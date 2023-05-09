from typing import List
import math

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Adiciona os índices originais das arestas na matriz de arestas
        edges = [[u, v, w, i] for i, [u, v, w] in enumerate(edges)]

        # Ordena as arestas por peso em ordem crescente
        edges.sort(key=lambda x: x[2])

        def kruskal(n, edges, bannedIdx, includeIdx):
            uf = UnionFind(n)
            totalWeight = 0

            # Se houver uma aresta de inclusão, a adiciona à árvore mínima
            if includeIdx != -1:
                u, v, w, _ = edges[includeIdx]
                uf.union(u, v)
                totalWeight += w
                n -= 1

            # Percorre as arestas e adiciona à árvore mínima se possível
            for i, (u, v, weight, _) in enumerate(edges):
                if i == bannedIdx:
                    continue
                if uf.union(u, v):
                    totalWeight += weight
                    n -= 1
                if n == 1:
                    break

            # Retorna o peso total da árvore mínima
            return math.inf if n > 1 else totalWeight

        criticalEdges = []
        mstWeight = kruskal(n, edges, -1, -1)

        # Encontra as arestas críticas
        for i in range(len(edges)):
            totalWeight = kruskal(n, edges, i, -1)
            if totalWeight > mstWeight:
                criticalEdges.append(edges[i][3])

        pseudoCriticalEdges = []

        # Encontra as arestas pseudo-críticas
        for i in range(len(edges)):
            if edges[i][3] in criticalEdges:
                continue

            totalWeight = kruskal(n, edges, -1, i)
            if totalWeight == mstWeight:
                pseudoCriticalEdges.append(edges[i][3])

        # Retorna as listas de arestas críticas e pseudo-críticas
        return [criticalEdges, pseudoCriticalEdges]


""""
Este código implementa a solução para o problema de 
encontrar as arestas críticas e pseudo-críticas em 
um grafo não direcionado ponderado. A solução utiliza 
o algoritmo de Kruskal para encontrar a árvore geradora 
mínima do grafo e, a partir dela, identifica as arestas 
que são críticas e as que são pseudo-críticas. O algoritmo 
de Kruskal é implementado utilizando a estrutura de dados 
Union-Find. A solução é implementada na classe Solution, 
que contém o método findCriticalAndPseudoCriticalEdges.
"""