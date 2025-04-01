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
    
    Para cada caso de prueba, se muestra una tabla que contiene:
      - Índice del punto.
      - Coordenadas (x, y).
      - Penalización asociada.
      - Costo acumulado (dp) para alcanzar dicho punto.
    """
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return

    index = 0
    case_num = 1  # Contador para los casos de prueba
    
    # Procesar cada caso de prueba.
    while True:
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
        
        total_points = len(points)
        
        # Precalcular la suma acumulada de penalizaciones.
        cum_pen = [0] * total_points
        cum_pen[0] = penalties[0]
        for i in range(1, total_points):
            cum_pen[i] = cum_pen[i-1] + penalties[i]
        
        # Inicializar el arreglo dp.
        dp = [float('inf')] * total_points
        dp[0] = 0.0  # Costo en el inicio es 0.
        
        # Calcular dp[j] para cada punto j.
        for j in range(1, total_points):
            for i in range(j):
                # Penalización acumulada de los puntos omitidos entre i y j.
                penalty_sum = cum_pen[j-1] - cum_pen[i]
                cost = dp[i] + distance(points[i], points[j]) + 1 + penalty_sum
                dp[j] = min(dp[j], cost)
        
        # Imprimir la tabla para el caso de prueba actual.
        print(f"\nCaso {case_num}:")
        print(f"{'Índice':<8} {'Coordenadas':<15} {'Penalización':<15} {'Costo acumulado (dp)':<20}")
        print("-" * 60)
        for i in range(total_points):
            # Formatear las coordenadas para imprimirlas de forma legible.
            coord_str = f"({points[i][0]},{points[i][1]})"
            print(f"{i:<8} {coord_str:<15} {penalties[i]:<15} {dp[i]:<20.3f}")
        
        case_num += 1

if __name__ == '__main__':
    main()
