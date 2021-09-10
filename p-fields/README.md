# Atividade 7 - Campos Potenciais

Nesta atividade, você irá projetar um planejador de movimento reativo baseado na técnica de Campos Potenciais para perseguir um alvo móvel evitando colisões com obstáculos. Nosso alvo será o pato meliante da figura abaixo e os obstáculos serão casas, ônibus e outros patos imóveis.

<figure>
  <div style="text-align:center;">
  <img src="img/mr_duck.png" alt="O infrator em questão." width="400px">
  </div>
</figure>

## Planejador

Seu agente possui conhecimento da sua localização no referencial fixo (posição $`x`$ e $`y`$ e orientação $`\theta`$), das localizações do alvo móvel e dos obstáculos no referencial fixo. Os obstáculos são representados como obstáculos e espeficacods como uma lista de vértices e o alvo é representado como um ponto.
Sugerimos dividir o problema em duas tarefas:

1. Planejador de trajetória
2. Seguidor de trajetória

A tarefa 1 pode ser realizada por um planejador de trajetória baseado em Campos Potenciais que fornece, a cada instante, uma posição (ponto) alvo a ser atingido (seguido). Assumindo a especificação das funções de forças de atração ao alvo $`F_{att}(q)`$ e repulsão dos obstásculos $`F_{rep}(q)`$, o ponto alvo 
```math
q_{t+1} = \begin{bmatrix} x_{t+1} & y_{t+1} \end{bmatrix}^t
```  
é obtido pela equação
```math
q_{t+1} = q_t + \alpha ( F_{att}(q_t) + F_{rep}(q_t) )\, ,
```
onde $`q_t = \begin{bmatrix} x_t & y_t \end{bmatrix}^t`$ é a posição atual do agente e $\alpha$ é um parâmetro da otimimzação chamado de tamanho do passo. 

Você deve implementar a função `preprocess` para que elea devolva o ponto $`q_{t+1}`$.


## Controlador

O ponto $`q_{t+1}`$ pode então ser usado para projetar sinais de controle de velocidade linear $`v`$ e angular $`\omega`$ para o agente.
Nessa proposta, o ponto alvo nunca é de fato alcançado (visto que o alvo é móvel).
Você deve implementar na função `send_commands` um controlador proporcional de velocidade do robô para seguir o ponto $`q_{t+1}`$ devolvido pela função  `preprocess` a cada instante de decisão.

