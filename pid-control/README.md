# Atividade 6 - Controle PID

Para esta atividade, você deve construir um controle PID seguidor de faixa implementando as partes
Proporcional, Integral e Derivada. Para tanto, você deve assumir que temos um sensor que, a partir
da pose do robô, retorna um sinal que indica se o robô está andando corretamente na faixa.

## Sensoriamento

O sensoriamento do robô seguidor de faixa, que para esta atividade pode ser considerado como dado,
tem como base o seguidor de ponto. Considere a imagem abaixo de um seguidor de ponto:

<figure>
  <div style="text-align: center">
  <img src="img/point_following.png" alt="Seguidor de ponto" width="500px">
  </div>
</figure>

Podemos modelar um seguidor de faixa reduzindo o problema ao de um seguidor de ponto em que $`G`$
segue a curva da faixa.

<figure>
  <div style="text-align: center">
  <img src="img/lane_following.png" alt="Seguidor de faixa" width="500px">
  </div>
</figure>

Neste contexto, as únicas variáveis que importam são $`d`$, a distância do robô em relação a faixa,
e $`\alpha`$ o ângulo entre a posição do robô e a tangente da curva definida pela faixa. Podemos
sintetizar estas duas variáveis em uma única função $`t`$

```math
  t(d, \alpha)=6d+\alpha.
```

Em termos de código, $`t`$ é dada como a função `Agent.preprocess`, que faz o cálculo para
encontrar $`d`$ e $`\alpha`$ a partir da função `lf_target` e retorna a linearização das duas
variáveis.

## Controle PID

Implemente as três partes (proporção, integral e derivada) do controlador PID no método
`Agent.send_commands` usando $`t`$ como sinal de entrada.
