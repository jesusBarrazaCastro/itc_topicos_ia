# 🐝 Simulación de Enjambre de Partículas

Este código implementa una **simulación básica de un enjambre de partículas (Swarm)**. Cada partícula tiene una posición aleatoria dentro de un rango definido por el usuario y puede tener atributos como velocidad, evaluación y un registro de su mejor posición. 
La simulación utiliza el algoritmo de **Optimización por Enjambre de Partículas (PSO)**, que busca minimizar una función objetivo. En este caso, la función objetivo es la distancia desde el origen de la matriz.



- **Posición**: Coordenadas en el espacio, definidas aleatoriamente dentro de un rango dado por el usuario.
- **Velocidad**: Vector que indica la dirección y magnitud del movimiento de la partícula en cada iteración.
- **Mejor posición**: La mejor posición alcanzada por la partícula a lo largo de su recorrido.
- **Evaluación**: El valor de la función objetivo para la posición actual.
