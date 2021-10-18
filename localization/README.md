# MAC0318 Introdução à Programação de Robôs Móveis

## Atividade 11 - Estimação da pose relativa

Para esta atividade, você deve melhorar seu estimador de pose relativa com informação temporal usando um filtro de histograma 2D.

## Filtro Bayesiano

Como nas atividades anteriores, o estado representará a pose relativa do agente na pista:
```math
X = \begin{pmatrix} d \\ \alpha \end{pmatrix}
```
O modelo de transição $`p(x_{t+1}|x_{t}, u=(\omega,v))`$ é portanto fornecido pela equação
```math
\begin{bmatrix}
 d_{t+1} \\ \alpha_{t+1}
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
com $`\epsilon_l`$ e $`\epsilon_r`$ representando os erros aleatórios no movimento parametrizados por gaussianas independentes de média 0 e variância $`sigma`$. Essa variância é um parâmetro que deve ser escolhido a partir da sua experiência para modelar a imprecisão no movimento. Note que pela equação acima seu estado é bidimensional e portanto você deve implementar um filtro de histograma 2D.

Vamos assumir que a observação $`Y`$ é a saída da rede neural a partir de uma imagem de captura da câmera fronta. Dessa forma, o modelo do sensor $`p(y|x)`$ pode ser modelado por uma gaussiana cuja média é o valor real $x=6d+\alpha$ e a variância pode ser estimada a partir do conjunto de teste (usando a variância do erro dado pela difernça entre a saída da rede e o valor real).

