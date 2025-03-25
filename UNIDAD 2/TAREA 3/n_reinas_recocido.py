import random
import math
import time

class NReinasRecocido:
    def __init__(self, n=8, temperatura_inicial=1000, min_temperatura=1, k=0.1):
        self.n = n
        self.temperatura = temperatura_inicial
        self.min_temperatura = min_temperatura
        self.k = k  # Constante de Boltzmann
        self.iteracion = 1  # Contador de iteraciones

    def generar_solucion_inicial(self):
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    def contar_conflictos(self, solucion):
        conflictos = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if solucion[i] == solucion[j] or abs(solucion[i] - solucion[j]) == abs(i - j):
                    conflictos += 1
        return conflictos

    def generar_vecino(self, solucion):
        # Genera un vecino intercambiando dos posiciones aleatorias
        vecino = solucion[:]
        a, b = random.sample(range(self.n), 2)  # Elegimos dos columnas distintas
        vecino[a], vecino[b] = vecino[b], vecino[a]  # Intercambio
        return vecino

    def actualizar_temperatura(self):
        # Secuencia de enfriamiento logarítmica de Boltzmann
        self.temperatura = self.temperatura / (1 + self.k * math.log(1 + self.iteracion))
        self.iteracion += 1

    def recocido_simulado(self):
        tiempo_inicio = time.time()
        solucion_actual = self.generar_solucion_inicial()
        mejor_solucion = solucion_actual[:]
        mejor_puntaje = self.contar_conflictos(mejor_solucion)
        iteraciones = 0

        while self.temperatura > self.min_temperatura and mejor_puntaje > 0:
            vecino = self.generar_vecino(solucion_actual)
            puntaje_actual = self.contar_conflictos(solucion_actual)
            puntaje_vecino = self.contar_conflictos(vecino)
            
            if puntaje_vecino < puntaje_actual:
                solucion_actual = vecino[:]
                if puntaje_vecino < mejor_puntaje:
                    mejor_solucion = vecino[:]
                    mejor_puntaje = puntaje_vecino
            else:
                probabilidad = math.exp((puntaje_actual - puntaje_vecino) / self.temperatura)
                if random.random() < probabilidad:
                    solucion_actual = vecino[:]
            
            self.actualizar_temperatura()
            iteraciones += 1

        tiempo_fin = time.time()
        tiempo_ejecucion = tiempo_fin - tiempo_inicio
        return mejor_solucion, mejor_puntaje, iteraciones, tiempo_ejecucion

# Ejecutar el algoritmo
solucionador = NReinasRecocido(n=8)
solucion, conflictos, iteraciones, tiempo = solucionador.recocido_simulado()

# Imprimir resultados
print("Solucion encontrada:", solucion)
print("Conflictos restantes:", conflictos)
print("Iteraciones realizadas:", iteraciones)
print(f"Tiempo de ejecucion: {tiempo:.4f} segundos")
