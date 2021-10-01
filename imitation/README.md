# MAC0318 Introdução à Programação de Robôs Móveis

## Atividade 10 - Aprendizado por imitação

Para esta atividade, você deve construir um agente que "imita" o comportamento de um especialista.
No nosso caso, nosso especialista será um híbrido entre um controlador automático PID e um
motorista humano (no nosso caso, você). O especialista tem como função gerar trajetórias de um comportamento (imagens e
rótulos de velocidades) para situações nas quais o controlador não está preparado (e não é trivial projetar um controlador). 
Nessa atividade, tais situações são dadas por outros veículos e objetos bloqueando a pista.

### Gerando os dados

Para que o agente possa aprender a desviar de obstáculos em seu caminho, precisamos que o especialista mostre, por meio de exemplos, o que deve ser feito ao se deparar com um obstáculo.

O agente `DataAgent` deve percorrer o circuito coletando os dados igual na atividade anterior.
Quando um objeto aparece no caminho, o especialista deve parar o agente e fazer uma ultrapassagem
de forma manual (ou seja, com o teclado). O método `DataAgent.send_commands` deve sobreescrever os
comandos que o controlador automático faria e salvaria nos dados, salvando os comandos dados por
você, ao invés.

É importante que você dê vários exemplos de ultrapassagem para o nosso modelo. Para re-aleatorizar
a pista, adicionando e removendo objetos da pista, aperte a tecla `R`. Para momentaneamente parar
de gravar as imagens e rótulos, tecle `P`.

**Dica:** você pode gerar vários datasets menores (não se esqueça de renomear os dados gerados para
não sobreescrevê-los) e concatená-los posteriormente. Desta forma, caso você gere um exemplo ruim,
não é preciso jogar fora todo o conjunto de dados.

**Dica:** você pode aproveitar para _corrigir_ o comportamento do controlador PID mesmo em casos sem obstáculo, como em curvas.

### Treinando seu modelo

Aprenda uma rede neural convolucional com os exemplos coletados. Certifique-se que você tenha
bastante exemplos tanto de ultrapassagens quanto de direção normal de faixa.

### Verificando a robustez

Avalie o seu modelo com o agente `EvaluationAgent`.

### Submissão

Submeta o arquivo `agent.py` via e-disciplinas. Coloque quaisquer recursos adicionais usados (rede neural) em repositório pessoal (google drive) e informe o link no cabeçalho do arquivo `agent.py`.
