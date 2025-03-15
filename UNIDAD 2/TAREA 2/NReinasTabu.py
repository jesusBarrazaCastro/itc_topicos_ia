import random
import time

class NReinasTabu:
    def __init__(self, n=8, max_iteraciones=500, tamano_tabu=10):
        self.n = n
        self.max_iteraciones = max_iteraciones
        self.tamano_tabu = tamano_tabu

    def generar_solucion_inicial(self):
        #generar solucion inicial aleatoria
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    def contar_conflictos(self, solucion):
        #contar el numero de conflictos en la solucion
        conflictos = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if solucion[i] == solucion[j] or abs(solucion[i] - solucion[j]) == abs(i - j):
                    conflictos += 1
        return conflictos

    def generar_vecinos(self, solucion):
        #generar soluciones vecinas intercambiando la posicion de una reina
        vecinos = []
        for columna in range(self.n):
            for fila in range(self.n):
                if solucion[columna] != fila:
                    nueva_solucion = solucion[:]
                    nueva_solucion[columna] = fila
                    vecinos.append(nueva_solucion)
        return vecinos

    def busqueda_tabu(self):
        #implementar la busqueda tabu con metricas de tiempo y movimientos
        tiempo_inicio = time.time()  
        movimientos_realizados = 0  

        solucion_actual = self.generar_solucion_inicial()
        mejor_solucion = solucion_actual[:]
        mejor_puntaje = self.contar_conflictos(mejor_solucion)
        lista_tabu = []
        iteracion = 0

        while iteracion < self.max_iteraciones and mejor_puntaje > 0:
            vecinos = self.generar_vecinos(solucion_actual)
            vecinos = sorted(vecinos, key=self.contar_conflictos)  # ordenar por menos conflictos

            for vecino in vecinos:
                if vecino not in lista_tabu:
                    solucion_actual = vecino
                    movimientos_realizados += 1  # sumar el movimiento realizado
                    break

            puntaje = self.contar_conflictos(solucion_actual)

            if puntaje < mejor_puntaje:
                mejor_solucion = solucion_actual[:]
                mejor_puntaje = puntaje

            lista_tabu.append(solucion_actual)
            if len(lista_tabu) > self.tamano_tabu:
                lista_tabu.pop(0)

            iteracion += 1

        tiempo_fin = time.time()  
        tiempo_ejecucion = tiempo_fin - tiempo_inicio

        return mejor_solucion, mejor_puntaje, movimientos_realizados, tiempo_ejecucion

# Ejecutar el algoritmo
solucionador = NReinasTabu(n=8)
solucion, conflictos, movimientos, tiempo = solucionador.busqueda_tabu()

# Imprimir resultados
print("Solucion encontrada:", solucion)
print("Conflictos restantes:", conflictos)
print("Movimientos realizados:", movimientos)
print(f"Tiempo de ejecucion: {tiempo:.4f} segundos")
