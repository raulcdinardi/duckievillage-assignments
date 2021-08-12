# Atividade 0 - Direção manual

Nesta atividade, apresentaremos o básico do ambiente que usaremos durante a disciplina. Vamos usar
uma versão modificada do simulador [Duckietown](https://github.com/duckietown/gym-duckietown/), que
chamaremos de [Duckievillage](https://gitlab.uspdigital.usp.br/mac0318-2021/duckievillage). Como
uma tarefa introdutória, vamos construir um carrinho de controle remoto no Duckievillage.

Para rodar a atividade, você deve ter instalado o Duckievillage (preferencialmente pelo script
`install.sh`). Não se esqueça de ativar o ambiente do Anaconda:

```bash
conda activate duckietown
```

O arquivo `manual.py` deve conter o código que deve ser entregue pelo e-disciplinas, assim como seu
nome e número USP no cabeçalho. Para esta primeira tarefa, primeiro vamos incluir as bibliotecas
que usaremos.

```python
import sys
import pyglet
from pyglet.window import key
from duckievillage import create_env
```

Usaremos o [pyglet](http://pyglet.org/) para lidar com o input, como teclado ou mouse; e para lidar
com a parte gráfica. Por parte do simulador, vamos usar a função `create_env`, que constrói o
ambiente de simulação que usaremos durante o curso. Esta função retorna o simulador, que
guardaremos na variável `env`.

```python
env = create_env(
  ...
)
```

O arquivo `manual.py` comenta com mais detalhes o que cada trecho de código faz. A parte mais
importante da tarefa é a função `update`. Vamos implementar o comportamento do robô a partir desta
função. Em particular, note a subrotina `env.step`: ela é encarregada de tomar uma ação do robô, e
aplicar suas consequências no ambiente (de simulação). Esta função toma como argumentos dois
números reais no intervalo $`[-1,1]`$: a potência no motor esquerdo e direito no robô
respectivamente.

Para que você se familiarize com o ambiente, **escreva um carrinho de controle remoto usando o
teclado como input**.
