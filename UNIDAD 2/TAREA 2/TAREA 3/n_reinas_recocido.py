import random
import math
import time

class NReinasRecocido:
    def __init__(self, n=8, temperatura_inicial=5000, min_temperatura=0.1, k=0.1):
        self.n = n
        self.temperatura = temperatura_inicial
        self.min_temperatura = min_temperatura
        self.k = k 
        self.iteracion = 1 

    def generar_solucion_inicial(self):
        opcion = input("¿Deseas ingresar la solución inicial manualmente? (s/n): ").strip().lower()
        
        if opcion == 's':
            while True:
                try:
                    solucion = list(map(int, input(f"Ingrese {self.n} valores separados por espacios (0-{self.n-1}): ").split()))
                    if len(solucion) == self.n and all(0 <= x < self.n for x in solucion):
                        return solucion
                    else:
                        print(f"Por favor, ingrese {self.n} valores dentro del rango 0-{self.n-1}.")
                except ValueError:
                    print("Entrada inválida. Inténtalo de nuevo.")
        else:
            sol_in = [random.randint(0, self.n - 1) for _ in range(self.n)]
            print("Solucion inicial: " + str(sol_in))
            return sol_in

    def contar_conflictos(self, solucion):
        conflictos = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if solucion[i] == solucion[j] or abs(solucion[i] - solucion[j]) == abs(i - j):
                    conflictos += 1
        return conflictos

    def generar_vecino(self, solucion):
        vecino = solucion[:]
        if random.random() < 0.5:  # 50% de las veces hacemos swap normal
            a, b = random.sample(range(self.n), 2)
            vecino[a], vecino[b] = vecino[b], vecino[a]
        else:  # 50% de las veces cambiamos una reina a una nueva posición
            i = random.randint(0, self.n - 1)
            vecino[i] = random.randint(0, self.n - 1)
        return vecino


    def actualizar_temperatura(self):
        #self.temperatura = self.temperatura / (1 + self.k * math.log(1 + self.iteracion))
        self.temperatura *= 0.99
        self.iteracion += 1

    def recocido_simulado(self):
        tiempo_inicio = time.perf_counter()
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
                probabilidad = math.exp((puntaje_actual - puntaje_vecino) / (self.temperatura + 1e-10))
                if random.random() < probabilidad:
                    solucion_actual = vecino[:]
            
            self.actualizar_temperatura()
            iteraciones += 1

        tiempo_fin = time.perf_counter()
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
