# Atividade 3 - Braitenberg Seguidor de Pista

Para esta atividade, vamos implementar um caso de uso mais realista para os veículos de
Braitenberg. Sua tarefa é conduzir um robô por uma pista contendo demarcações usuais de trânsito.

Para tanto, precisamos construir dois filtros: um para a demarcação de Linha de Fluxo Oposto (LFO),
que consiste na linha amarela tracejada; e outra para a Linha de Bordo (LBO), que aqui é definida
por uma linha branca contígua. A figura abaixo mostra a pista, demarcações da pista, e filtros para
cada demarcações internas e externas.

<figure>
  <div style="text-align: center">
  <img src="img/838.png" alt="Pista e filtros para ambos os tipos de demarcações.">
  </div>
</figure>

A ideia aqui é usar as demarcações para manter o robô percorrendo dentro da faixa de trânsito. O
seu robô deve utilizar o comportamento enamorado para permanecer a uma distância de tanto a LFO
quanto LBO. Usaremos o arquivo `lane_following.py` para construir nosso agente.

## Filtrando pontos de interesse

De forma parecida com a atividade anterior, precisamos identificar os pontos de atração e repulsão.
Para tanto, vamos construir dois filtros de cor para a LFO e LBO: em uma vamos identificar a cor
amarelada da LFO, usando o espaço HSV para tanto; na outra, como devemos identificar a cor branca,
usaremos o RGB para facilitar. O trecho de código no construtor de `Agent` define as fronteiras
para detecção de cor.

```python
self.inner_lower = np.array([20, 85, 20])
self.inner_upper = np.array([30, 255, 255])
self.outer_lower = np.array([180, 180, 180])
self.outer_upper = np.array([255, 255, 255])
```

No código, nos referimos como *inner* a marcação LFO e, como *outer*, a LBO. No método
`Agent.preprocess`, de forma similar à tarefa anterior, identificamos os pixels que estão dentro do
intervalo desejado e em seguida construímos a máscara: uma para cada marcação. O método retorna
tanto a máscara para LFO e LBO quanto a união das duas máscaras.

<figure>
  <div style="text-align: center">
  <img src="img/1352.png" alt="Curva na pista.">
  </div>
</figure>

A figura acima mostra a imagem original, a união das máscaras e cada uma das máscaras
individualmente.

## Ativação

A sua tarefa nesta atividade é construir as matrizes de ativação

```python
inner_left_motor_matrix  : np.ndarray
inner_right_motor_matrix : np.ndarray
outer_left_motor_matrix  : np.ndarray
outer_right_motor_matrix : np.ndarray
```

que definem o comportamento do motor esquerdo e direito para as máscaras LFO e LBO. Faça os ajustes
necessários das constantes regularizadoras no método `Agent.send_commands`. O comportamento
desejado é uma reação *enamorado* para cada uma das faixas. Submeta sua solução (o arquivo
`lane_following.py`) via e-disciplinas.

