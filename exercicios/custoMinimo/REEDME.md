# [Custo Mínimo para Conectar Todos os Pontos](https://leetcode.com/problems/min-cost-to-connect-all-points/description/)

**Nível: Médio**

Você recebe um vetor `points` representando coordenadas inteiras de alguns pontos em um plano 2D, onde `points[i] = [xᵢ, yᵢ]`.

O custo de conectar dois pontos `[xᵢ, yᵢ]` e `[xⱼ, yⱼ]` é a **distância manhattan** entre eles: `|xᵢ - xⱼ| + |yᵢ - yⱼ|`, onde `|val|` denota o valor absoluto de `val`.

Retorne o *custo mínimo* para fazer todos os pontos conectados. Todos os pontos estão conectados se houver **exatamente um** caminho simples entre quaisquer dois pontos.

**Exemplo 1:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/08/26/d.png)

``` bash
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
```

**Exemplo 2:**

``` bash
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```