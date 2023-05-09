# [Encontrar as arestas críticas e pseudo-críticas na Árvore Geradora Mínima](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/)

**Nível: Difícil**

Dado um grafo não-direcionado e conectado com pesos, com `n` vértices numerados de `0` a `n-1`, e um array `edges` onde `edges[i] = [a_i, b_i, weight_i]` representa uma aresta bidirecional e ponderada entre os nós `a_i` e `b_i`. Uma árvore geradora mínima (MST) é um subconjunto das arestas do grafo que conecta todos os vértices sem ciclos e com o menor peso de aresta possível.

Encontre todas as arestas críticas e pseudo-críticas na árvore geradora mínima (MST) do grafo dado. Uma aresta da MST cuja exclusão do grafo aumentaria o peso da MST é chamada de aresta crítica. Por outro lado, uma aresta pseudo-crítica é aquela que pode aparecer em algumas MSTs, mas não em todas.

Observe que você pode retornar os índices das arestas em qualquer ordem.

**Exemplo 1:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/06/04/ex1.png)

``` bash
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explicação: A figura acima descreve o grafo. A figura a seguir mostra todas as possíveis Árvores Geradoras Mínimas (MSTs):
```
![App Screenshot](https://assets.leetcode.com/uploads/2020/06/04/msts.png)

``` bash 
Observe que as duas arestas 0 e 1 aparecem em todas as MSTs, portanto são arestas críticas e são retornadas na primeira lista de saída. 
As arestas 2, 3, 4 e 5 fazem parte apenas de algumas MSTs, portanto são consideradas arestas pseudo-críticas. Nós as adicionamos à segunda lista de saída.
```
**Exemplo 2:**
![App Screenshot](https://assets.leetcode.com/uploads/2020/06/04/ex2.png)

``` bash
Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explicação: Podemos observar que, uma vez que as 4 arestas têm peso igual, escolher qualquer 3 arestas das 4 fornecidas produzirá uma Árvore Geradora Mínima (MST). 
Portanto, todas as 4 arestas são pseudo-críticas.
```

**Restrições**
- `2 <= n <= 100`
- `1 <= edges.length <= min(200, n * (n - 1) / 2)`
- `edges[i].length == 3`
- `0 <= a_i < b_i < n`
- `1 <= weighti <= 1000`
- Todos os pares `(a_i, b_i)` são distintos.
