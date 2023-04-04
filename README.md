# cube-rotato

Pedro Antônio Silva e Gustavo Lindenberg Pacheco

https://github.com/gustavolp1/cube-rotato

![](/rotation_demo.gif)

## Como instalar e executar

- Instale o Python (https://www.python.org/) em sua máquina. O programa foi desenvolvido especificamente para Windows, portanto não há garantia de que funcionará em outros sistemas operacionais.

- Instale algum editor de texto/código, como o Visual Studio Code (https://code.visualstudio.com/).

- Abra o Visual Studio Code, procure pela opção Clonar Repositório, e selecione Clonar da Internet. No campo, cole o seguinte link: https://github.com/gustavolp1/cube-rotato

- Escolha uma localização em sua máquina para salvar o repositório clonado.

- Abra o terminal e digite o comando a seguir:

> pip install -r "requirements.txt"

- No Visual Studio, abra o arquivo "cube-rotato.py" dentro do repositório clonado. Você poderá usá-lo para testar o programa.

## Como usar o programa

Para inicializar o cubo, apenas rode o arquivo "cube-rotato.py" na sua IDE de preferência. Uma vez com o programa aberto, você pode usar os seguintes comandos no teclado:

W/S - Gira o cubo no eixo X, em sentidos opostos dependendo do botão;
A/D - Gira o cubo no eixo Y, em sentidos opostos dependendo do botão;
Q/E - Gira o cubo no eixo Z, em sentidos opostos dependendo do botão;

I/O - Aumentam e diminuem a distância focal, respectivamente;
Roda do mouse - Aumenta ou diminui a distância focal;

Espaço - Aumenta o ângulo do cubo em todos os eixos simultaneamente enquanto é apertado.

## Modelo Matemático

Antes de começarmos a elaborar equações, precisamos antes definir como repesentaremos os pontos do nosso cubo, além de definir quais alterações serão necessárias para representá-lo em 2D e realizar rotações.

- ## Definindo os Pontos :
    - Primeiro definimos um cubo de dimensões arbitrárias. Para isso, criamos oito pontos (correspondentes aos vértices do cubo), com um valor x, y , z e 1, de forma que cada ponto têm sua distância aos três pontos adjacentes sendo igual, além de uma dimensão a mais para realizarmos calculos mais para frente, o que corresponde a um cubo.
    Isso nos dá uma matriz criada em NumPy, seguindo o seguinte modelo:
        $$
                
        pontos =
        \begin{bmatrix}

        1, 1, 1, 1  \\

        1, 1, -1, 1 \\

        1, -1, 1, 1 \\

        1, -1, -1, 1 \\

        -1, 1, 1, 1 \\

        -1, 1, -1, 1 \\

        -1, -1, 1, 1 \\

        -1, -1, -1, 1 \\

        \end{bmatrix}
        $$

    Nosso objetivo será criar uma matriz generalizada T que faz todas as transformações necessárias nos pontos ao realizarmos uma multiplicação matricial. Isso será feito a seguir.


- ## Definindo a transformação :
    ### Note que :
    Assumimos a distribuição dos eixos de pontos no seguinte formato para as matrizes de transformação :
    $$
        P = \begin{bmatrix}
        X \\
        Y \\
        Z \\
        W
        \end{bmatrix}
    $$
    Com W não sendo considerado como um eixo e usado apenas para o calculo final.
    
    - Rotação :

        O primeiro componente de nossa matriz T será o componente de rotação, constituido de três matrizes que representam uma rotação de $\theta$ graus nos eixos x,y,z.

        Todas foram previamente adaptadas para rotacionar vetores de três dimensões e comportar uma dimensão a mais, que guarda uma variável de ajuste comumente usada para representação de objetos 3d (mais detalhes na explicação da matriz T).

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
        \end{bmatrix}\\
        \hspace{0.5in}\\

        R_z = \begin{bmatrix}
        \cos(\theta) & - \sin(\theta) & 0 & 0 \\
        \sin(\theta) & \cos(\theta) & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        0 & 0 & 0 & 1
        \end{bmatrix}
        $$
        Por fim, as multiplicamos entre si para obtermos uma única matriz de rotação para todas as dimensões envolvidas :
        $$
        R = R_xR_yR_z
        $$

    - Translação em Z - Profundidade :

        O segundo componente será uma matriz comum de translação em Z, que definirá a distância aparente do cubo em relação a tela do computador, visto que Z será nosso eixo de profundidade :
        $$
        T =

        \begin{bmatrix}

        1 & 0 & 0 & 0 \\

        0 & 1 & 0 & 0 \\

        0 & 0 & 1 & D_z \\

        0 & 0 & 0 & 1

        \end{bmatrix}
        $$
        - Com Dz representando o deslocamento no eixo z por iteração do código/comando.
        Este componente estará multiplicando a matriz de Rotação diretamente, visto que altera a visualização 3D emulada dos pontos.

    - Transformação :
    
    - Traslação em x e y :
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

    Com todas as matrizes anteriores, obtemos uma matriz de transformação T na quando as multiplicamos na ordem correta. Ou seja:
    $$
    T = T_xyPT_zR
    $$


Referência : Notebook 4 de Algebra Linear, explicação e exemplo elaborados pelo Professor Tiago, 2023.