# [Caminho com Esforço Mínimo](https://leetcode.com/problems/path-with-minimum-effort/)

**Nível: Médio**

Você é um caminhante se preparando para uma caminhada. Você recebe uma matriz `heights` de tamanho `rows x columns`, onde `heights[row][col]` representa a altura da célula `(row, col)`. Você está localizado na célula superior esquerda, `(0, 0)`, e deseja viajar para a célula inferior direita, `(rows-1, columns-1)` (ou seja, indexado por 0). Você pode se mover para cima, para baixo, para a esquerda ou para a direita, e deseja encontrar uma rota que requer o mínimo esforço.

O esforço de uma rota é a diferença absoluta máxima nas alturas entre duas células consecutivas da rota.

Retorne o esforço mínimo necessário para viajar da célula superior esquerda para a célula inferior direita.

**Exemplo 1:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/10/04/ex1.png)

``` bash
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explicação: A rota [1,3,5,3,5] tem uma diferença absoluta máxima de 2 em células consecutivas.
Isso é melhor do que a rota [1,2,2,2,5], onde a diferença absoluta máxima é 3.
```

**Exemplo 2:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/10/04/ex2.png)

``` bash
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explicação: A rota [1,2,3,4,5] tem uma diferença absoluta máxima de 1 em células consecutivas, o que é melhor do que a rota [1,3,5,3,5].
```

**Exemplo 3:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/10/04/ex3.png)

``` bash
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explicação: Esta rota não requer nenhum esforço.
```

**Restrições**

- `rows == heights.length`
- `columns == heights[i].length`
- `1 <= rows, columns <= 100`
- `1 <= heights[i][j] <= 106`
