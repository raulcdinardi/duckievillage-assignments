# Atividade 5 - Controle em Malha Aberta

Nesta atividade, vamos usar as constantes $`K_m`$ e $`K_t`$ encontradas na Atividade 4 para
construir três agentes que executam as seguintes trajetórias:

1. Anda em um quadrado;
2. Anda em um círculo;
3. Faz uma ultrapassagem.

Para tanto, primeiro leia o Jupyter Notebook [../Modelagem.ipynb](../Modelagem.ipynb) que explica
os diferentes comportamentos no contexto de um robô com motor diferencial. Assim feito, vamos
implementar os agentes no simulador!

## Estimando as constantes

Para esta atividade, vamos usar o mesmo ambiente e mapa que usamos para a atividade passada.
Portanto, você pode usar as mesmas constantes encontradas na [Atividade 4](../model/) para esta
tarefa. Implemente o método `Agent.power` usando estas mesmas constantes.

## Implementando os agentes

O código [agents.py](./agents.py) usa uma classe base `Agent` contendo métodos comuns, como o
método `Agent.power`. A função de atualização do robô é dada pelo método `send_commands`, que tem
como argumento um `float` `dt`. Esta variável conta a diferença de tempo desde a sua última chamada
de função. Você pode usar isto para controlar o tempo de cada ação do agente.

Para cada agente (`SquareAgent`, `CircleAgent` e `OvertakeAgent`), implemente os métodos
`send_commands` para que eles executem os seus respectivos comportamentos. Você pode adicionar
variáveis e métodos nestas classes sem restrição.

**Dica:** use `start` para definir um tempo inicial para a primeira ação.

## Desenhando as trajetórias

Você pode salvar a trajetória executada pelo robô com a tecla `P`. Para mudar de agente, use as
teclas `,` e `.`. Suas trajetórias devem parecer com os seguintes exemplos:

<figure>
  <div style="text-align: center">
  <img src="../img/square.png" alt="Trajetória para o SquareAgent.">
  <img src="../img/circle.png" alt="Trajetória para o CircleAgent.">
  <img src="../img/overtake.png" alt="Trajetória para o OvertakeAgent.">
  </div>
</figure>

## Submissão

Submeta o seu código `agents.py` junto com os desenhos das trajetórias dos três agentes pelo
e-disciplinas.
