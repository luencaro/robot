# Práctica de Algoritmos y Complejidad

Este repositorio contiene la solución al problema "Desafío de robots", desarrollado para la asignatura de Algoritmos y Complejidad, impartida por la profesora Esmeide A Leal Narváez, PhD.

## Descripción del Problema

En este problema se participa en un desafío de robots donde se dispone de un espacio de 100 m x 100 m y una serie de objetivos ubicados en puntos específicos del espacio. El robot debe:
- Comenzar en (0,0).
- Visitar los objetivos en orden (objetivo 1, objetivo 2, etc.), deteniéndose 1 segundo en cada uno.
- Terminar en (100,100) y detenerse 1 segundo.

Cada objetivo (excepto el inicio y la meta) tiene una penalización de tiempo si se omite. El robot puede omitir algunos objetivos incurriendo en la penalización correspondiente, buscando minimizar el tiempo total (tiempo de viaje, tiempos de detención y penalizaciones).

El puntaje final es la suma del tiempo en recorrer la trayectoria (a velocidad 1 m/s), las paradas de 1 segundo y las penalizaciones acumuladas de los objetivos omitidos. El objetivo es obtener el puntaje más bajo posible.

## Detalles de la Solución

Se resuelve el problema utilizando **programación dinámica**. La idea principal es la siguiente:

- **Definición de puntos:**  
  Se consideran todos los puntos importantes: el inicio (0,0), cada uno de los objetivos y la meta (100,100).

- **Recurrencia:**  
  Para cada punto \( j \) (objetivo o meta) se calcula el costo mínimo \( \text{dp}[j] \) para llegar desde el inicio hasta \( j \) considerando que se puede saltar algunos objetivos:
  
  $$
  \text{dp}[j] = \min_{0 \le i < j} { \text{dp}[i] + \text{dist}(P[i], P[j]) + 1 + \sum_{k=i+1}^{j-1} \text{penalty}[k] }
  $$
  
  Donde:
  - $\( P[i] \)$ es la posición del punto $\( i \)$.
  - $\( \text{dist}(P[i], P[j]) \)$ es la distancia Euclidiana entre $\( P[i] \)$ y $\( P[j] \)$.
  - El “1” representa el tiempo de parada en cada objetivo (incluyendo la meta).
  - La suma de penalizaciones corresponde a los objetivos omitidos entre $\( i \)$ y \( j \)$.

- **Optimización:**  
  Se utiliza una suma acumulada para calcular de forma eficiente la penalización total de los objetivos omitidos en cada salto.

## Cómo Usar el Programa

1. **Preparar la entrada:**

   El programa lee la entrada desde STDIN. La entrada debe seguir el siguiente formato:

   - Una línea con un número entero \( N \) (número de objetivos).
   - \( N \) líneas, cada una con tres enteros: `X Y P`, donde:
     - `X` y `Y` son las coordenadas del objetivo (valores entre 1 y 99).
     - `P` es la penalización por omitir ese objetivo.
   - Una línea que contenga solo `0` indica el fin de la entrada.

   2. **Ejecutar el programa:**

Puedes ejecutar el programa de la siguiente manera:

- **Desde la terminal (usando un archivo de entrada):**
  
  Guarda la entrada en un archivo, por ejemplo `entrada.txt`, y luego ejecuta:
  ```bash
  python tu_programa.py < entrada.txt
  ```
  
- **Entrada manual:**

  Ejecuta el programa y escribe la entrada directamente en la consola. Finaliza la entrada con `Ctrl+D` (en Linux/Mac) o `Ctrl+Z` (en Windows).

3. **Salida:**

El programa imprimirá en la consola el puntaje mínimo, redondeado a tres decimales, para cada caso de prueba. Cada resultado se imprimirá en una línea diferente, sin líneas en blanco intermedias.
