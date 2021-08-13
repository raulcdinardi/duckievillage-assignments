# Atividade 1 - Direção manual

Nesta atividade, apresentaremos o básico do ambiente de simulação de robôs autônomos que usaremos durante a disciplina. 
Vamos usar uma versão modificada do simulador [Duckietown](https://github.com/duckietown/gym-duckietown/), que
chamaremos de [Duckievillage](https://gitlab.uspdigital.usp.br/mac0318-2021/duckievillage). 
Para familiarizar-se com a estrutura de um agente do simulador, você deverá construir um sistema de controle manual do robô a partir das teclas do seu teclado.

## Pré-requisito

Vamos assumir que você instalou o simulador e clonou o projeto de atividades executando o arquivo [install.sh](../../install.sh) do projeto [Duckievillage](https://gitlab.uspdigital.usp.br/mac0318-2021/duckievillage). Antes de cada atividade, lembre-se de ativar o ambiente do Anaconda:

```bash
conda activate duckietown
```

## Controle manual

O arquivo [manual.py](./manual.py) contém um código mínimo criando um ambiente de simulação e um agente móvel. 
Antes de continuar, preencha o cabeçalho do arquivo com seu nome e número USP (para que possamos identificar corretamente sua submissão no e-disciplinas).

O arquivo importa as seguintes bibliotecas.

```python
import sys
import pyglet
from pyglet.window import key
from duckievillage import create_env
```

A biblioteca [pyglet](http://pyglet.org/) serve para tratar as entradas do teclado, e a temporização da simulação. 
A biblioteca `duckievillage` contém o simulador; vamos usar a função `create_env`, que constrói o
ambiente de simulação que usaremos durante o curso. Esta função retorna uma instanciação do simulador na variável `env`:

```python
env = create_env(
  ...
)
```

O arquivo [manual.py](./manual.py) é comentado com os detalhes sobre o restante das operações necessárias para inciar o simulador. 
Você pode inspecionar o código, mas não será necessário entender o funcionamenteo do simulador para as atividades da disciplina (vamos focar apenas no funcionamento do robô). 
O comportamento do robô é implementado na função `update`. Vamos implementar o comportamento do robô a partir desta
função. Em particular, note a subrotina `env.step`: ela é encarregada de tomar uma ação do robô, e
aplicar suas consequências no ambiente (de simulação). Esta função toma como argumentos dois
números reais no intervalo $`[-1,1]`$: a potência no motor esquerdo e direito no robô
respectivamente.

Para que você se familiarize com o ambiente, **escreva um carrinho de controle remoto usando o
teclado como input**.
