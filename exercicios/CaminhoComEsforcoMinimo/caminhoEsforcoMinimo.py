from typing import List
import heapq
import math

class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        num_rows, num_cols = len(heights), len(heights[0])
        heap = []
        distances = [[math.inf] * num_cols for _ in range(num_rows)]
        distances[0][0] = 0
        heapq.heappush(heap, (0, 0, 0))
        
        while heap:
            distance, row, col = heapq.heappop(heap)
            if row == num_rows - 1 and col == num_cols - 1:
                return distance
            for dx, dy in self.directions:
                new_row, new_col = row + dx, col + dy
                if not (0 <= new_row < num_rows and 0 <= new_col < num_cols):
                    continue
                new_distance = max(distance, abs(heights[new_row][new_col] - heights[row][col]))
                if new_distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = new_distance
                    heapq.heappush(heap, (new_distance, new_row, new_col))
        
        return 0
    
"""
O algoritmo usa um heap para armazenar os próximos nós a 
serem explorados. Ele começa com o nó (0,0) e inicializa a 
distância para chegar a este nó como zero e a distância 
para chegar a todos os outros nós como infinito. Em 
seguida, ele explora cada nó adjacente, atualizando a 
distância para alcançar cada nó com a maior diferença de 
altura encontrada até agora. Se a nova distância for menor 
do que a distância atual, ela é atualizada e o nó é 
adicionado à heap. O algoritmo termina quando o nó de destino 
é alcançado e retorna a distância total percorrida.

Em resumo, este é um algoritmo eficiente e elegante para 
encontrar o caminho de menor esforço em uma matriz retangular 
de alturas.
"""