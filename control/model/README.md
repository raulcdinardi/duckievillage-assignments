# Atividade 4 - Modelagem

Sua tarefa nesta atividade será realizar experimentos a fim de determinar as constantes de ganho $`K_m`$ e corte $`K_t`$ que relacionam os valores de tensão elética enviadas $`V_l`$ e $`V_r`$ ao motores esquerdo e direito, respetivamente, à velocidades linear $`v`$ e taxa de rotação $`\omega`$ do robô, como visto em sala de aula:

```math
\begin{cases}
  V_l=\frac{1}{R}(K_m-K_t)(v-\omega L)\\
  V_r=\frac{1}{R}(K_m+K_t)(v+\omega L).
\end{cases}
```
A conversão entre os valores de velocidade para valores de sinais de controle acima já está implementada no método `get_pwm_control` no arquivo [agent.py](./agent.py).
As constantes $`R`$ e $`L`$ indicam o raio da roda e a distância entre o centro do robô e a roda, respectivamente. 
No robô real, tais constanes seriam medidas. Adote os valores $`R=0.0318`$ e $`2L=0.102`$ [m] que são próximos dos valores nominais de construção do Duckiebot. O simulador usa valores próximos a esses, com algum erro aleatório para gerar o efeito de medições imprecisas.
Em um robô ideal, as rodas e motores são idênticos e possuem a mesma constante $`K_m`$ relacionando tensão elétrica e torque. 
No robô real, no entanto, as rodas e motores possuem discrepâncias que fazem com que essa relação seja distinta para cada roda.
A constante $`K_t`$ provê um grau de liberdade adicional para corrigir tais discrepâncias.

## Estimando constantes

Com a função de dinâmica inversa implementada, você deve realizar os seguintes experimentos empíricos (no simulador) a fim de determinar as constantes $`K_m`$ e $`K_t`$.

1. Com um valor arbitrário de $`K_m`$ fixo, encontre $`K_t`$ comandando valores de tensão elétrica idênticos em ambos os motores ($`V_l=V_r=c`$) por um dado intervalo de tempo e calculando as velocidades a partir das poses inicial e final. Note que o arquivo [agent.py](./agent.py) já contém um exemplo de código para obter a diferença entre tais poses.

2. Com a constante $`K_t`$ fixa, encontre o valor de $`K_m`$ fazendo com que o robô ande em linha reta por um determinado intervalo de tempo observando a distância percorrida.

Assegure-se que os valores encontrados para as constantes estão corretos realizando o movimento como girar ao redor do seu eixo (ou seja, sem sair do lugar).

Note que o simulador espera valores para $`V_l`$ e $`V_r`$ no intervalo $`[-1,1]`$.  Usar valores altos para as constantes pode fazer com que os respectivos valores de tensão sejam limitados a tal intervalo (parecendo que o robô não responde aos comandos dados).

## Submissão

Submeta o seu código `agent.py` pelo e-disciplinas.
