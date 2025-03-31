import math
import sys

def distance(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    index = 0
    results = []
    while True:
        # Número de objetivos
        N = int(input_data[index])
        index += 1
        if N == 0:
            break

        # Inicializamos los puntos: inicio, objetivos, fin
        points = [(0,0)]
        penalties = [0]  # sin penalización en el inicio
        for _ in range(N):
            x = int(input_data[index]); y = int(input_data[index+1]); p = int(input_data[index+2])
            index += 3
            points.append((x,y))
            penalties.append(p)
        points.append((100,100))
        penalties.append(0)  # fin sin penalización

        # Número total de puntos
        total_points = len(points)  # N+2

        # Precalcular suma acumulada de penalizaciones:
        cum_pen = [0]*total_points
        cum_pen[0] = penalties[0]
        for i in range(1, total_points):
            cum_pen[i] = cum_pen[i-1] + penalties[i]

        # dp[i] = costo mínimo para llegar al punto i
        dp = [float('inf')] * total_points
        dp[0] = 0.0

        for j in range(1, total_points):
            for i in range(j):
                # Suma de penalizaciones de los puntos que se omiten: de i+1 a j-1
                # Si i+1 > j-1, la suma es 0.
                penalty_sum = cum_pen[j-1] - (cum_pen[i] if i >= 0 else 0)
                cost = dp[i] + distance(points[i], points[j]) + 1 + penalty_sum
                if cost < dp[j]:
                    dp[j] = cost

        results.append(f"{dp[total_points-1]:.3f}")

    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    main()
