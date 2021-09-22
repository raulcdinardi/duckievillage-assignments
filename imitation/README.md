# MAC0318 Introdução à Programação de Robôs Móveis

## Atividade 10 - Aprendizado por imitação

Para esta atividade, você deve construir um agente que "imita" o comportamento de um especialista.
No nosso caso, nosso especialista será um híbrido entre um controlador automático PID e um
interventor humano (no nosso caso, você). O especialista tem como função gerar os dados (imagens e
rótulos) para que o agente possa aprender e andar de forma independente e autônoma.

### Gerando os dados

Nas atividades anteriores, a tarefa de seguir a pista era sempre dada por uma situação ideal: a
pista é sempre visível e não há obstáculos. Aqui, vamos considerar o último, ou seja, o caso em que
há objetos obstruindo o caminho do agente. Para que o agente possa aprender que atropelar patinhos
não é desejável, precisamos que o especialista mostre, por meio de exemplos, o que deve ser feito
ao se deparar com um obstáculo.

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

### Treinando seu modelo

Aprenda uma rede neural convolucional com os exemplos coletados. Certifique-se que você tenha
bastante exemplos tanto de ultrapassagens quanto de direção normal de faixa.

### Verificando a robustez

Avalie o seu modelo com o agente `EvaluationAgent`.
