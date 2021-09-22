# MAC0318 Introdução à Programação de Robôs Móveis

## Atividade 9 - Seguidor de pista com redes neurais convolucionais

Nessa atividade, você deve implementar um agente seguidor de pista de forma similar ao da
[atividade anterior](../regression). Na tarefa anterior, você implementou um seguidor de pista
através de uma rede neural como módulo de percepção, usando dados já coletados préviamente para
predizer o sinal de controle $`y=C\cdot d+\alpha`$, onde $`d`$ é a distância do robô até a faixa a
ser seguida e $`\alpha`$ é a diferença entre o ângulo do carrinho e da faixa, a partir de uma
imagem. O sinal $`y`$ é então repassado ao controlador, que decide a velocidade linear e angular do
carrinho.

Nesta atividade, ao invés de separarmos o agente em módulo de percepção e controle, iremos usar um
modelo de rede neural convolucional para predizer as velocidades diretamente da imagem. Para isso,
precisaremos coletar os dados para predição.

### Coletando dados

Você usará duas classes de agente no arquivo [agent.py](./agent.py): `DataAgent` e
`EvaluationAgent`. O primeiro será utilizado para coletar os dados necessários para treinar nosso
modelo, enquanto que o outro avaliará a rede treinada. O agente `DataAgent` percorrerá o circuito
de forma automática (igual a atividade de [Controle PID](../pid-control)) e ao mesmo tempo
coletará as imagens vistas pelo robô e as ações/velocidades dadas pelo controlador, que agirão como
rótulos.

A princípio, `DataAgent` vem apenas com um controlador proporcional simples. Isso quer dizer que as
predições do nosso eventual modelo terão como base o comportamento de um controlador simples, que é
altamente oscilatório nas curvas. Para que nosso modelo prediga as trajetórias de forma mais suave,
precisamos usar um controlador PID. Use o seu controlador PID da atividade de
[Controle PID](../pid-control) para gerar os dados.

**Observação:** é importante que os dados contenham poses variadas, e não apenas aquelas vistas
pelo controlador em seu trajeto "ideal". Você pode manualmente guiar o robô para poses que o agente
não veria normalmente, mas não se esqueça de gravar apenas as ações que o controlador tomaria, e
não as ações manuais que levam o robô para fora do ideal.

O método `DataAgent.send_commands` redimensiona as imagens para $`80\times 60`$, rotulando cada
imagem com a velocidade linear e angular. A função `on_key_press` salva as imagens e rótulos com o
pressionar do botão `ESC`.

### Treinando seu modelo

Agora que temos os dados, podemos aprender nosso modelo. Treine uma rede neural convolucional que
toma como entrada imagens coloridas $`80\times 60`$ e retorna ambas as velocidades a serem atuadas no
agente. Use a classe `EvaluationAgent` para avaliar seu escore.

### Verificando a robustez

Com o modelo pronto, mude a seguinte linha do construtor da classe `EvaluationAgent`

```python
super().__init__(environment, randomize = False)
```

por

```python
super().__init__(environment, randomize = True)
```

Agora, execute novamente o seu modelo. Note que o modelo que funcionava anteriormente mal consegue
seguir uma reta. Isso acontece pois sua rede estava correlacionando a cor da grama com as
velocidades a serem seguidas. Porém, no nosso caso, a cor da grama é irrelevante para as ações do
agente.

<figure>
  <div style="text-align:center;">
  <img src="img/fire.jpg" alt="Incêndio na Califórnia." width="600px">
  <figcaption><b>Fonte:</b> Wikipedia</figcaption>
  </div>
</figure>

A invariância da cor em certos casos é importante para direção autônoma, afinal a performance de um
carro autônomo deveria se manter alta no caso de algum evento externo. Por exemplo, a imagem acima
mostra as ruas de uma cidade na Califórnia após os incêndios de 2020. É razoável (e especialmente
desejável) esperar que o carro continue funcionando durante o apocalipse.

Faça a mesma mudança no construtor da classe `DataAgent` e colete mais dados do ambiente desta vez
aleatorizado. Concatene os dados coletados antes da aleatorização com os coletados agora e retreine
o modelo. Avalie novamente em ambas as situações aleatorizadas (`randomize = True`) e normais
(`randomize = False`).
