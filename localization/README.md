# MAC0318 Introdução à Programação de Robôs Móveis

## Atividade 11 - Estimação da pose relativa

Para esta atividade, você deve melhorar seu estimador de pose relativa com informação temporal usando um filtro de histograma 2D.

## Filtro Bayesiano

Como nas atividades anteriores, o estado representará a pose relativa do agente na pista:
```math
X = \begin{pmatrix} d \\ \alpha \end{pmatrix}
```
O modelo de transição $`p(x_{t+\Delta t}|x_{t}, u=(\omega,v))`$ é portanto fornecido pela equação
```math
\begin{bmatrix}
 d_{t+\Delta t} \\ \alpha_{t+\Delta t}
\end{bmatrix}
=
\begin{bmatrix}
 d_t \\ \alpha_t
\end{bmatrix}
+
\Delta t 
\begin{bmatrix}
 v \sin \alpha_t \\
 \omega_t
\end{bmatrix}
+
\Delta t 
\begin{bmatrix}
 v (\epsilon_l + \epsilon_r)/2 \\
 \omega_t (\epsilon_l - \epsilon_r)/2
\end{bmatrix} .
```
com $`\epsilon_l`$ e $`\epsilon_r`$ representando os erros aleatórios no movimento parametrizados por gaussianas independentes de média 0 e variância $`\sigma`$. Essa variância é um parâmetro que deve ser escolhido a partir da sua experiência para modelar a imprecisão no movimento. Note que pela equação acima seu estado é bidimensional e portanto você deve implementar um filtro de histograma 2D.

Vamos assumir que a observação $`Y`$ é a saída da rede neural a partir de uma imagem de captura da câmera fronta. Dessa forma, o modelo do sensor $`p(y|x)`$ pode ser modelado por uma gaussiana cuja média é o valor real $`x=6d+\alpha`$ e a variância pode ser estimada a partir do conjunto de teste (usando a variância do erro dado pela difernça entre a saída da rede e o valor real).

Você deve usar a moda da crença $`p(X_t)`$ como sinal para o controlador.

**Nota:** Como o controlador usa apenas o valor agregado $`y=6d + \alpha`$, que é a mesmo quantidade estimada pelo sensor, alternativamente é possível implementar um filtro 1D assumindo que o estado é também $`x=6d + \alpha`$. A distribuição de transição $`p(6d_{t+1} + \alpha_{t+1}|6d_t + \alpha_t)`$ pode ser obtida a partir da matriz de transição para os centróides 2D como $`p(x=6d+\alpha)=\sum_{d,\alpha} p(x|d,\alpha)p(d,\alpha)`$ onde a soma é realizada sobre os valores dos centróides $`d`$ e $`\alpha`$ e $`p(d,\alpha)`$ são os valores em 2D. 

Recomendamos que você leia o Jupyter Notebook sobre [Filtro Bayesiano](https://gitlab.uspdigital.usp.br/mac0318-2021/assignments/-/blob/master/localization/Filtro%20Bayesiano.ipynb) primeiro. Usando a notação do notebook, note que nosso estado é dado por $`X=(d,\alpha)`$ (que equivale à pose do robô), e as observações $`Y`$ são as saídas da rede dadas as imagens frontais. Você deve implementar as funções $`correct`$ e $`predict`$ de forma similar ao Notebook. No esqueleto são dadas as discretizações em células de $`6d+\alpha`$ a partir do conjunto de dados de treino, assim como a estimação das gaussianas para cada célula. Use os vetores `cells` e `gaussians` para computar

```math
\tilde{\text{bel}}_{t+1}(x)=p(Y|X=x)\text{bel}_t(x)
```

na função `correct` e

```math
\text{bel}_{t+1}(x') = \sum_x p(X_{t+1}=x' | X_t=x, u, \Delta t) \text{bel}_t(x)
```

na função `predict` assumindo que $`p(Y|X=x)`$ é dado por uma gaussiana de $`6d+\alpha`$ centrada na
célula dada por $`x`$ (estimada em `gaussians`), e $`p(X_{t+1}=x'|X_t=x,u,\Delta t)`$ é uma gaussiana
centrada em $`x`$ após aplicada a ação $`u`$ em um intervalo de tempo $`\Delta t`$ (e portanto a
nova pose relativa se assumirmos nenhum erro) e com variância fixa.
