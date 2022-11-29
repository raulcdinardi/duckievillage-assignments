# MAC0318 Introdução à Programação de Robôs Móveis

## Projeto Final - Desafio Pato Wheels

Depois da crise de entregas de 2021 na Patolândia, ocasionada pelo aumento das compras
virtuais em epocas de pandemia, os patinhos finalmente estao prontos para recomecar
seu mais antigo costume: o **desafio *Pato Wheels***.

Por conta do distanciamento social, essa milenar cerimonia havia sido suspensa na
cidade dos patos nos ultimos anos. Agora, patos dos mais diferentes paises estao
viajando para a Patolândia em busca de assistir e participar desse historico
campeonato, que somente ocorre de 4 em 4 anos. Mas temos um problema, diversas
pistas de corrida nao conseguiram ser finalizadas a tempo e o numero de participantes
desse ano superou todos os recordes. Por isso, o prefeito e engenheiros da cidade
improvisaram pistas usando as proprias ruas e avenidas da cidade.

Aqui entra o seu papel, como umx novx competidxr pela Taca dos Patos, seu objetivo
nao deve ser somente pilotar mais rapido que os outros e respeitando as restricoes
de cada pista, voce tambem deve se atentar aos diversos patos espectados que estarao
assistindo o evento, desviando deles ou de outros corredores caso necessario.

### Sua missão

A missão é simples: **ganhar o campeonato sem ferir outros patinhos**.

Usando o Patobô, que possue apenas dois motores para cada roda e uma câmera frontal,
vocês devem percorrer as diferentes pistas da competicao, completando uma volta em
cada uma delas. Para isso, vocês terão acesso aos seguintes tipos de informação:

1. Sua posição e ângulo atual;
2. Imagens instantaneas obtidas por meio da sua câmera frontal; e
3. Se o seu carrinho fugiu para fora da pista ou colidiu contra um objeto.

Para não causar mais caos nas cidades, o Presidente Paulo Pato ressaltou enfaticamente
que vocês devem seguir as três regras da pato-robótica:

1. O Patobô não deve machucar nenhum pato;
2. O Patobô não deve causar danos materiais à cidade;
3. O Patobô deve permanecer dentro dos limites da rua; e
4. Sua velocidade deve ser igual ou superior a 0.2m/s (podendo ser reduzida somente
em desvios ou realização de curvas).

Para cumprir sua missão, vocês podem usar quaisquer técnicas, vistas em aula ou 
não, desde que vocês obedeçam as três regras acima e apenas utilizem as informações
dadas. O uso de informações adicionais é proibido.

O seu código deve ser implementado a partir do arquivo [agent.py](./agent.py), que
contém o código para o agente do Patobô. Como existem imperfeicoes nas ruas da
Patolandia, assume-se um erro nas rodas e portanto temos as constantes usuais para
o cálculo da modelagem `Agent.get_pwm_control`. O método `Agent.send_commands` é 
encarregado de computar as ações do agente. Vocês opcionalmente podem usar, assim
como nas tarefas anteriores, o método `Agent.preprocess` para organizar o seu código
em diferentes módulos de percepção e controle.

**Importante:** todo o código deve ser implementado no arquivo `agent.py`, que será 
o único arquivo código-fonte a ser entregue no e-disciplinas. No entanto, a execução
da tarefa deve ser feita através de [challenge.py](./challenge.py) por meio do comando:

```bash
python3 assignments/challenge/challenge.py assignments/challenge/examples/challenge_n
```

Onde o `n` acima é quaisquer um dos possíveis arquivos `challenge_*` no diretório de
exemplos para execução.

### Navegando a pato-cidade

Seu Patobô deve também executar a rota por meio de um seguidor de pistas, como vocês
irão navegar a cidade está a cargo de vocês. Todas as técnicas vistas em aula (ou não)
são permitidas desde que não precisem de mais informação que o estabelecido. Além disso,
seu seguidor de pista deve obedecer as regras de trânsito e as regras da pato-robótica.
Ou seja, colisões com pato-pedestres, outros Patobôs, prédios, casas, cones de trânsito
ou qualquer outro objeto acarretará numa infração adicionada ao relatório do Patobô.
Infrações também serão dadas caso o Patobô saia dos limites da pista.

Patos são notoriamente péssimos motoristas, o que torna Patolândia a capital dos
acidentes automobilísticos. É possível que algum acidente ocorra na cidade, o que faz
com que um trajeto acabe completamente obstruído. Neste caso, o seu Patobô deve
identificar que o acidente impossibilita uma ultrapassagem segura e ficar parado. 

### Verificando seu relatório de infrações

O relatório de infrações é salvo em `/tmp/output.txt` quando o simulador é encerrado 
pela tecla `ESC`. A escala de penalidade não é 1-para-1 com a nota final do projeto. 
Aplicaremos uma constante a cada tipo de penalidade dependendo da dificuldade de
resolução de cada uma delas. Um agente que percorre toda a pista e termina no ponto
inicial sem nenhuma infração a princípio deve receber 10 na nota final (a menos que
informações não permitidas tenham sido utilizadas).

### Entrega

A data maxima de entrega é **19/12/2022*, vocês devem entregar:

1. Seu código `agent.py`;
2. Quaisquer materiais, dados, redes neurais, etc. que são necessários para executar
o código;

Em **20/12/2022** e **21/21/2022**, executaremos os diferentes codigos nas aulas
de terca e quarta. Exemplificando a performance dos diferentes competidores em
variados percursos.

**Nota:** Não se esqueça de comentar eventuais mudanças de rotas devido a acidentes!
Explique como foi feita a identificação do acidente, a atualização no planejamento 
para desviar desse objeto.

### Bônus

Além das infrações, o relatório do Patobô também contém uma medição do tempo de
execucao usado pelo competidor para finalizar a pista. O time de Patobô que for
mais rapido em cada desafio um bônus na nota do projeto!

### Comunicação entre grupos

Os grupos não devem compartilhar informações de suas soluções. Porém, é permitido
compartilhar os vídeos de execução dos seus agentes entre grupos. Para gravar videos,
vocês podem utilizar a gravação automática do simulador por meio da variável de
construção `video_path` na criação do ambiente em [challenge.py](./challenge.py).

**Boa sorte e bom trabalho! Patolândia conta com vocês!**
