# Atividade 7 - Campo Potencial

Nesta atividade, você irá projetar um planejador baseado em Campo Potencial.

## Caça ao pato

Seu objetivo nesta atividade será caçar um pato foragido.

<figure>
  <div style="text-align:center;">
  <img src="img/mr_duck.png" alt="O infrator em questão." width="400px">
  </div>
</figure>

Seu agente deve usar campos potenciais para caminhar em direção ao pato, desviando de possíveis
obstáculos em seu caminho. Em outras palavras, objetos no cenário serão considerados como polígonos
que emitem uma força repelente, e a força atratora será dada pelo pato.

## Planejador

Para a parte do planejador, você deve implementar as funções de força (`F_att` para a força
atratora e `F_rep` para repelente) e a função `preprocess`, que computa a força/gradiente
resultante. Esta última função retornará o ponto $`P`$ que seu agente deve passar para o
controlador para que o robô ande de acordo com o plano.

## Controlador

Construa um controlador em `send_commands` que toma o ponto $`P`$ dado pelo planejador `preprocess`
e computa as velocidades linear e angular para que o agente siga $`P`$.

## Bônus: Controlador PID

Como bônus, implemente um controlador PID para o planejador de campos potenciais.
