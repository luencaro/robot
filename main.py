import math
import sys

def distance(p1, p2):
    """
    Calcula la distancia Euclidiana entre dos puntos p1 y p2.
    
    Args:
        p1 (tuple): Coordenadas (x, y) del primer punto.
        p2 (tuple): Coordenadas (x, y) del segundo punto.
    
    Returns:
        float: La distancia entre p1 y p2.
    """
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def main():
    """
    Función principal que resuelve el problema del "Desafío de robots" usando programación dinámica.
    
    El programa realiza lo siguiente:
    
    1. Lee la entrada completa desde STDIN. La entrada debe contener varios casos de prueba.
       Cada caso comienza con un entero N (número de objetivos), seguido de N líneas con tres enteros
       (X, Y, P) que representan las coordenadas del objetivo y la penalización por omitirlo.
       Una línea con un solo 0 indica el final de la entrada.
    
    2. Se agrega el punto de inicio (0,0) y el punto de meta (100,100) (con penalización 0) a la lista de puntos.
    
    3. Se precomputan las sumas acumuladas de penalizaciones para calcular de manera eficiente la penalización
       total de los objetivos que se omiten en cada salto.
    
    4. Se utiliza programación dinámica para calcular el costo mínimo para llegar a cada punto. La recurrencia es:
    
       $$
       \text{dp}[j] = \min_{0 \le i < j} \\Big\\{ \text{dp}[i] + \text{dist}(P[i], P[j]) + 1 + \\sum_{k=i+1}^{j-1} \text{penalty}[k] \\Big\\}
       $$
       
       Donde:
       - \( P[i] \) es la posición del punto \( i \).
       - \( \text{dist}(P[i], P[j]) \) es la distancia entre \( P[i] \) y \( P[j] \) (a 1 m/s).
       - El “1” es el tiempo de detención en cada punto.
       - La suma de penalizaciones es para los objetivos omitidos entre \( i \) y \( j \).
    
    5. Se imprime el resultado para cada caso, redondeado a tres decimales.
    """
    # Leer toda la entrada y dividirla en tokens.
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return

    index = 0
    results = []
    
    # Procesar cada caso de prueba.
    while True:
        # Número de objetivos para el caso de prueba actual.
        N = int(input_data[index])
        index += 1
        
        # El valor 0 indica el final de la entrada.
        if N == 0:
            break

        # Inicializar la lista de puntos y penalizaciones.
        # Se añade el punto de inicio (0,0) sin penalización.
        points = [(0, 0)]
        penalties = [0]
        
        # Leer los N objetivos.
        for _ in range(N):
            x = int(input_data[index])
            y = int(input_data[index+1])
            p = int(input_data[index+2])
            index += 3
            points.append((x, y))
            penalties.append(p)
        
        # Añadir el punto de meta (100,100) sin penalización.
        points.append((100, 100))
        penalties.append(0)
        
        # Total de puntos (inicio + objetivos + meta)
        total_points = len(points)
        
        # Precalcular la suma acumulada de penalizaciones para poder calcular la penalización
        # de los puntos omitidos en un salto de forma eficiente.
        cum_pen = [0] * total_points
        cum_pen[0] = penalties[0]
        for i in range(1, total_points):
            cum_pen[i] = cum_pen[i-1] + penalties[i]
        
        # dp[i] almacenará el costo mínimo para llegar al punto i.
        dp = [float('inf')] * total_points
        dp[0] = 0.0  # Costo en el inicio es 0.
        
        # Calcular dp[j] para cada punto j (desde el primero hasta la meta).
        for j in range(1, total_points):
            # Se considera moverse desde cualquier punto i anterior hasta el punto j.
            for i in range(j):
                # Calcular la suma de penalizaciones de los objetivos omitidos entre i+1 y j-1.
                penalty_sum = cum_pen[j-1] - cum_pen[i]
                # Costo al ir de i a j:
                #   dp[i]: costo mínimo para llegar a i.
                #   distance(points[i], points[j]): tiempo de viaje (velocidad 1 m/s).
                #   1: tiempo de detención en j.
                #   penalty_sum: penalización acumulada por objetivos omitidos.
                cost = dp[i] + distance(points[i], points[j]) + 1 + penalty_sum
                # Actualizar dp[j] con el costo mínimo encontrado.
                dp[j] = min(dp[j], cost)
        
        # Guardar el resultado para este caso, redondeado a tres decimales.
        results.append(f"{dp[total_points-1]:.3f}")
    
    # Imprimir los resultados, cada uno en una línea.
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    main()