# [Tempo de Atraso da Rede](https://leetcode.com/problems/network-delay-time/)

**Nível: Médio**

Você recebe uma rede de `n` nós, rotulados de `1` a `n`. Você também recebe `times`, uma lista de tempos de viagem como arestas direcionadas `times[i] = (uᵢ, vᵢ, wᵢ)`, onde `uᵢ` é o nó de origem, `vᵢ` é o nó de destino e `wᵢ` é o tempo que leva para um sinal viajar da origem ao destino.

Enviaremos um sinal de um determinado nó `k`. Retorne o tempo **mínimo** que leva para todos os `n` nós receberem o sinal. Se for impossível para todos os `n` nós receberem o sinal, retorne `-1`.

**Exemplo 1:**

![App Screenshot](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

``` bash
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

**Exemplo 2:**

``` bash
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

**Exemplo 3:**

``` bash
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
```