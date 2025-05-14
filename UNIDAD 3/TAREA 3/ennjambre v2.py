import random
import math

def funcion_objetivo(coords):
    return math.sqrt(coords[0] ** 2 + coords[1] ** 2) ## distancia al origen

class Particula:
    def __init__(self, rango_x, rango_y, funcion_objetivo):
        if rango_x[0] >= rango_x[1] or rango_y[0] >= rango_y[1]:
            raise ValueError("Los valores mínimos deben ser menores que los máximos para cada eje.")

        self.coordenadas = [
            random.randint(rango_x[0], rango_x[1]),
            random.randint(rango_y[0], rango_y[1])
        ]
        self.vel = [0.0, 0.0]
        self.funcion_objetivo = funcion_objetivo
        self.evaluacion = self.funcion_objetivo(self.coordenadas)
        self.mejor_posicion = self.coordenadas[:]
        self.mejor_valor = self.evaluacion

    def evaluar(self):
        self.evaluacion = self.funcion_objetivo(self.coordenadas)
        return self.evaluacion

    def mover(self, inercia, c1, c2, mejor_global):
        for i in range(2):  
            r1 = random.random()
            r2 = random.random()
            cognitive = c1 * r1 * (self.mejor_posicion[i] - self.coordenadas[i])
            social = c2 * r2 * (mejor_global[i] - self.coordenadas[i])
            
            # Actualización de la velocidad
            self.vel[i] = inercia * self.vel[i] + cognitive + social
            
            # Limitar la velocidad a un rango máximo
            velocidad_maxima = 10  # Ajusta el valor según sea necesario
            self.vel[i] = max(-velocidad_maxima, min(self.vel[i], velocidad_maxima))
            
            self.coordenadas[i] += int(round(self.vel[i]))
            self.coordenadas[i] = max(0, min(self.coordenadas[i], 100))

        # Evaluar la nueva posición
        nueva_eval = self.evaluar()
        
        # Actualizar el mejor valor y posición si es necesario
        if nueva_eval < self.mejor_valor:
            self.mejor_valor = nueva_eval
            self.mejor_posicion = self.coordenadas[:]

    def __repr__(self):
        return (f"Coordenadas: X={self.coordenadas[0]}, Y={self.coordenadas[1]} | "
                f"Velocidad: {self.vel} | Evaluación: {self.evaluacion} | "
                f"Mejor Posición: {self.mejor_posicion} | Mejor Valor: {self.mejor_valor}")

class Enjambre:
    def __init__(self):
        self.elementos = []
        self.mejor_global = None
        self.mejor_valor = float('inf')

    @classmethod
    def construir(cls, cantidad, rango_x, rango_y, funcion_objetivo, mostrar=False):
        print("\nConfiguración de límites:")
        print(f"  Eje X -> {rango_x}")
        print(f"  Eje Y -> {rango_y}\n")

        grupo = cls()
        for idx in range(cantidad):
            if mostrar:
                print(f"Iniciando partícula {idx + 1}/{cantidad}...")
            p = Particula(rango_x, rango_y, funcion_objetivo)
            if p.evaluacion < grupo.mejor_valor:
                grupo.mejor_valor = p.evaluacion
                grupo.mejor_global = p.coordenadas[:]
            if mostrar:
                print(p)
            grupo.agregar(p)
        return grupo

    def agregar(self, p):
        self.elementos.append(p)

    def mover_enjambre(self, inercia, c1, c2):
        for p in self.elementos:
            p.mover(inercia, c1, c2, self.mejor_global)
            if p.evaluacion < self.mejor_valor:
                self.mejor_valor = p.evaluacion
                self.mejor_global = p.coordenadas[:]

    def visualizar(self):
        print("\nResumen del Enjambre:")
        for i, p in enumerate(self.elementos, 1):
            print(f"Partícula #{i} -> {p}")

def pedir_rango(eje):
    while True:
        try:
            min_val = int(input(f"Ingrese el valor mínimo para el eje {eje}: "))
            max_val = int(input(f"Ingrese el valor máximo para el eje {eje}: "))
            if min_val >= max_val:
                print("❌ El valor mínimo debe ser menor que el máximo. Intente de nuevo.")
                continue
            return (min_val, max_val)
        except ValueError:
            print("❌ Entrada inválida. Ingrese números enteros.")

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("❌ El número debe ser mayor a cero.")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida. Ingrese un número entero.")

if __name__ == "__main__":
    print("=== Simulación de Enjambre de Partículas ===")
    cantidad = pedir_entero("Ingrese la cantidad de partículas a generar: ")
    rango_x = pedir_rango("X")
    rango_y = pedir_rango("Y")
    iteraciones = pedir_entero("Ingrese el número de iteraciones: ")

    # Crear y mostrar el enjambre
    grupo = Enjambre.construir(
        cantidad=cantidad,
        rango_x=rango_x,
        rango_y=rango_y,
        funcion_objetivo=funcion_objetivo,
        mostrar=True
    )

    # Parámetros del movimiento
    inercia = 0.7
    c1 = 1.5
    c2 = 1.5

    for i in range(iteraciones):
        print(f"\n--- Iteración {i + 1} ---")
        grupo.mover_enjambre(inercia, c1, c2)
        grupo.visualizar()

    print(f"\n✅ Mejor valor encontrado: {grupo.mejor_valor}")
    print(f"📍 Mejor posición encontrada: {grupo.mejor_global}")
