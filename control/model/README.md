# Atividade 4 - Modelagem

Sua tarefa nesta atividade será construir um carrinho de controle remoto de forma similar à
primeira atividade. A diferença está nas ações dadas ao robô. Enquanto que na Atividade 1
construímos um agente que toma como ações a tensão nos motores esquerdo e direito, aqui iremos usar
como ações uma velocidade $`v`$ e um ângulo $`\omega`$. Para isso, faremos um exercício de
cinemática experimental. Relembremos as duas equações de transformação de velocidade e ângulo para
tensão:

```math
\begin{cases}
  V_l=\frac{2}{R}(K_m-K_t)(v-\omega L)\\
  V_r=\frac{2}{R}(K_m+K_t)(v+\omega L)
\end{cases}
```

onde $`V_l`$ e $`V_r`$ são as tensões desejadas do motor esquerdo e direito respectivamente a
partir da velocidade $`v`$ e ângulo $`\omega`$ dados. As constantes $`R`$ e $`L`$ indicam o raio da
roda e largura entre os eixos das rodas na construção do robô. As constantes $`K_m`$ e $`K_t`$ que
representam imperfeições nas rodas ou construção do robô. Note que tais constantes são as únicas
variáveis desconhecidas na equação. Tanto $`R`$ quanto $`L`$ são fácilmente mensuráveis no robô.
Nossa primeira tarefa será estimar $`K_m`$ e $`K_t`$ para que possamos usar a equação acima.

## Estimando constantes

O primeiro passo para estimar as constantes $`K_m`$ e $`K_t`$ é definir um experimento para
medirmos as imperfeições. Considere o seguinte experimento proposto:

> Fixamos uma velocidade retilínea arbitrária porém constante $`v`$ e velocidade angular
> $`\omega=0`$ por $`t`$ segundos. Note que $`v`$ é, a princípio, desconhecido porém definido pelas
> tensões dos motores $`V_l=V_r=c`$ para algum $`c`$ escolhido. Após $`t`$ segundos, o robô terá
> andado uma distância $`d`$ com desvio angular $`\theta`$, que representam exatamente as
> velocidades reais de $`v`$ e $`\omega`$. Com estas variáveis, acabamos com duas equações com duas
> variáveis desconhecidas $`K_m`$ e $`K_t`$ a partir da equação de transformação.

Execute o experimento acima e utilize o resultado para estimar as constantes a partir das medidas
$`d`$ e $`\theta`$. Imprima os valores estimados de $`K_m`$ e $`K_t`$, e use tais estimativas para
encontrar e imprimir as tensões dos motores para que o robô ande a distância $`d`$ sem nenhum
desvio angular.

**Dica:** use as fórmulas de Movimento Retilíneo Uniforme (MRU) para extrair as velocidades a
partir das distâncias.

## Velocidade e ângulo

Com as constantes estimadas, use a equação (antes incompleta) para traduzir velocidade e ângulo em
tensão para os motores. Construa um robô de controle remoto cujas ações são a velocidade e ângulo a
serem executados, ao invés das potências do motor. Implemente o método `power` que toma uma
velocidade $`v`$, velocidade angular $`w`$ e as constantes $`K_m`$ e $`K_t`$ e transforma nas
tensões dos motores.
