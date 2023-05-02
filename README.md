# **PacMan**

## **-Explicación del código**
En resumen, el código crea un tablero de juego con un tamaño específico que ingresa el usuario y coloca aleatoriamente comidas y fantasmas en el tablero. Luego, PacMan se mueve por el tablero recogiendo comidas y evitando fantasmas. El juego termina cuando PacMan encuentra un fantasma o ha recorrido todo el tablero. Se muestra el tablero y el puntaje final al finalizar el juego.

## **-Estos son los pasos que sigue el algoritmo**
1.Se muestran las reglas del juego al usuario.

2. Se solicita al usuario que ingrese el tamaño del tablero.
3. Se crea una matriz vacía para representar el tablero del juego.
4. Se llena la matriz con espacios vacíos, comidas (representadas por "O") y fantasmas (representados por "A").
5. Se inicializan las variables para almacenar el puntaje y el estado del juego.
6. Se inicia un bucle que representa el movimiento de PacMan en el tablero.
7. Se recorre el tablero por filas.
8. Si el número de fila es par, se recorre la fila de izquierda a derecha y se verifica si se encuentra una comida ("O") o un fantasma ("A"). En caso de encontrar una comida, se incrementa el puntaje. Si se encuentra un 9. 9. fantasma, se establece el estado del juego en "False" para finalizar el juego.
10. Si el número de fila es impar, se recorre la fila de derecha a izquierda y se realizan las mismas verificaciones.
11. Después de cada movimiento de PacMan, se imprime el tablero y el puntaje actual.
12. Una vez que el juego ha terminado, se muestra un mensaje de "GAME OVER".
