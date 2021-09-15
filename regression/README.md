# MAC0318 Introdução à Programação de Robôs Móveis

## Atividade 8 - Seguidor de pista a partir de imagem

Nessa atividade você deve projetar e implementar um agente seguidor de pista a partir de imagens de sua câmera. Seu agente deve estender o controlador seguidor de pista da [Atividade 6](../pid-control/README.md) com um módulo de percepção, que estima a pose do agente em relação à pista a partir da imagem da câmera do robô.
A pose relativa robô é representada pela distância $d$ ao centro da faixa e pelo ângulo $\alpha$ de inclinação como mostrado na figura abaixo.

<figure style="text-align: center">
   <img src="img/lane_following2.png" width=400>
</figure>

Como anteriormente, vamos assumir que os dois valores são combinados conforme a equação abaixo:

```math
  y=6d+\alpha \, .
```
O arquivo [agent.py](./agent.py) contém um método `Agent.preprocess` que simula o sensoriamento (a captura da imagem); você deve modificá-lo para que ele processe a imagem de captura e devolva o valor $`y`$ correspondente.

## Estimação de pose na pista baseada em aprendizado supervisionado

Você deve construir uma rede neural como regressor para prever o valor $y$ a partir de uma imagem. De acordo com a metodologia de aprendizado supervisionado, você deve obter um conjunto de dados rotulados (nesse caso, de imagens anotadas com os valores de saída $y$ correspondentes) e segmentá-lo em partes de treino, validação e teste. Para sua conveniência, nós fornecemos um conjunto de dados rotulados de imagens de tamanho 200x150 pixels, pré-processadas para segmentar as cores das faixas intermitentes (amarelas) e contínuas (brancas), de maneira a simplificar o problema. Note que as imagens possuem um tamanho menor que as imagens capturadas pelo robô; isso reduz a sobrecarga computacional de processamento da rede neural sem afetar a acurácia do modelo. A função `Agent.preprocess` já contém os passos para segmentar as imagens tal qual foi usado para produzir os dados.

Você deve escolher uma arquitetura para a rede neural que seja suficientemente complexa para capturar a complexidade da tarefa, mas de tamanho reduzido para não introduzir muita latência no préprocessamento (nem consumir muitos recursos no aprendizado).

Sugerimos que antes de começar você se familiarize com os conceitos de [regressão](./Aprendizado\ supervisionado.ipynb) e [redes neurais](./Redes\ neurais.ipynb) por meio dos notebooks disponíveis.

