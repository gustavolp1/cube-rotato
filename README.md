# cube-rotato

`Pedro Antônio Silva e Gustavo Lindenberg Pacheco`

https://github.com/gustavolp1/cube-rotato

![](/rotation_demo.gif)

## Como instalar e executar

> git clone git@github.com:gustavolp1/cube-rotato.git

(Entre no diretório do repositório)

> pip install -r "requirements.txt"

> python cube-rotato.py

## Como usar o programa

Para inicializar o cubo, apenas rode o arquivo "cube-rotato.py" na sua IDE de preferência. Uma vez com o programa aberto, você pode usar os seguintes comandos no teclado:

`W/S` - Gira o cubo no eixo X, em sentidos opostos dependendo do botão;

`A/D` - Gira o cubo no eixo Y, em sentidos opostos dependendo do botão;

`Q/E` - Gira o cubo no eixo Z, em sentidos opostos dependendo do botão;

`I/O` - Aumentam e diminuem a distância focal, respectivamente;

`Roda do mouse` - Aumenta ou diminui a distância focal;

`Espaço` - Aumenta o ângulo do cubo em todos os eixos simultaneamente enquanto é apertado.

## Modelo Matemático

Antes de começarmos a elaborar equações, precisamos antes definir como repesentaremos os pontos do nosso cubo, além de definir quais alterações serão necessárias para representá-lo em 2D e realizar rotações.

- ## Definindo os Pontos:
Primeiro definimos um cubo de dimensões arbitrárias nos eixos `x`, `y` e `z`, além de uma dimensão adicional, `w` representada por uma linha de `1`s.

$$
\begin{bmatrix}
1 & 1 & 1 & 1 & -1 & -1 & -1 & -1 \\
1 & 1 & -1 & -1 & 1 & 1 & -1 & -1 \\
1 & -1 & 1 & -1 & 1 & -1 & 1 & -1 \\
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 
\end{bmatrix}
$$

Nosso objetivo será criar uma matriz generalizada `T` que faz todas as transformações necessárias nos pontos ao realizarmos uma multiplicação matricial. Isso será feito a seguir.


- ## Definindo a transformação
    ### Note que:
No formato de ponto:

$$
P = \begin{bmatrix}
x \\
y \\
z \\
w
\end{bmatrix}
$$

A dimensão `w` é usada somente para cálculos. Ela não representa uma coordenada em nosso plano. Seu uso é feito da seguinte forma:

<!-- elaborar o por que do W dividir no x e y -->

$$
P = \begin{bmatrix}
x/w \\
y/w \\
z \\
w
\end{bmatrix}
$$

A matriz `T` que será obtida até o final multiplicará com cada ponto.

$$
PontoFinal = TP
$$


    
- Rotação:

O primeiro componente de nossa matriz `T` será o componente de rotação, constituido de três matrizes que representam uma rotação de $\theta$ graus nos eixos `x`, `y` e `z`.

Todas foram previamente adaptadas para rotacionar vetores de três dimensões e comportar uma dimensão a mais, que guarda uma variável de ajuste comumente usada para representação de objetos tridimensionais (mais detalhes na explicação da matriz `T`).

O ângulo $\theta$ é configurado manualmente no código para cada uma dessas matrizes, permitindo rotação em qualquer eixo.

$$
R_x = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) & 0 \\
0 & \sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_y = \begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
-\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_z = \begin{bmatrix}
\cos(\theta) & - \sin(\theta) & 0 & 0 \\
\sin(\theta) & \cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Por fim, as multiplicamos entre si para obtermos uma única matriz de rotação para todas as dimensões envolvidas:

$$
R = R_xR_yR_z
$$

- Translação em Z (Profundidade):

O segundo componente será uma matriz comum de translação em Z, que definirá a distância aparente do cubo em relação à tela do computador, visto que Z será nosso eixo de profundidade:

$$
P = 
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & Dz \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Com Dz representando o deslocamento no eixo z por iteração do código/comando.
Este componente estará multiplicando a matriz de Rotação diretamente, visto que altera a visualização 3D emulada dos pontos.

- Projeção:
        
A matriz de projeção será a responsável em projetar nossos pontos tridimensionais em duas dimensões. Ela leva em consideração a distância focal em relação ao objeto, representada por `d`.

$$
P =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & -d \\
0 & 0 & -1/d & 0
\end{bmatrix}
$$

# Explain

- Traslação em x e y:
    
Depois de aplicada a projeção para o plano 2D, ou seja, a tela, basta trasladar nosso cubo para uma posição onde ele possa ser visualizado melhor, através de uma matriz de traslação comum redimensionada para 3 dimensões e com uma dimensão extra em padrão identidade.

$$
T =
\begin{bmatrix}
1 & 0 & 0 & H/2 \\
0 & 1 & 0 & W/2 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- Matriz T:

Com todas as matrizes anteriores, obtemos uma matriz de transformação `T` quando as multiplicamos na ordem correta. Ou seja:

$$
T = T_xPT_zR
$$

Que rotaciona, distância/aproxima e translada nosso cubo de uma vez!

Referência : Notebook 4 de Algebra Linear, explicação e exemplo elaborados pelo Professor Tiago, 2023.