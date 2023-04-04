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

Antes de começarmos a elaborar equações, precisamos definir algumas matrizes :
    - Assumindo que teremos uma matriz base 4x8 que repesenta as posições,

- ## Definindo os Pontos :
    - primeiro definimos um cubro de dimensões arbitrárias,

- ## Definindo a transformação :
    - Rotação :
        $$
                
        R =
        \begin{bmatrix}

        cos(speed), -np.sin(speed), 0 \\

        np.sin(speed), np.cos(speed), 0 \\

        0, 0,1

        \end{bmatrix}
        $$

    - Translação em Z - Profundidade :
    - Transformação :
    - Traslação em x e y :
        $$
        T =

        \begin{bmatrix}

        1, 0, H/2 \\

        0, 1, W/2 \\

        0, 0 , 1

        \end{bmatrix}
        $$

Referência : Notebook 4 de Algebra Linear, explicação e exemplo elaborados pelo Professor Tiago, 2023.