import random

class Particula:
    def __init__(self, rango_x, rango_y):
        if rango_x[0] >= rango_x[1] or rango_y[0] >= rango_y[1]:
            raise ValueError("Los valores mínimos deben ser menores que los máximos para cada eje.")

        self.coordenadas = [
            random.randint(rango_x[0], rango_x[1]),
            random.randint(rango_y[0], rango_y[1])
        ]
        self.vel = [0.0, 0.0]
        self.evaluacion = None
        self.record = None

    def __repr__(self):
        return (f"Coordenadas: X={self.coordenadas[0]}, Y={self.coordenadas[1]} | "
                f"Velocidad: {self.vel} | Evaluación: {self.evaluacion} | Record: {self.record}")


class Enjambre:
    def __init__(self):
        self.elementos = []

    @classmethod
    def construir(cls, cantidad, rango_x, rango_y, mostrar=False):
        print("\nConfiguración de límites:")
        print(f"  Eje X -> {rango_x}")
        print(f"  Eje Y -> {rango_y}\n")

        grupo = cls()
        for idx in range(cantidad):
            if mostrar:
                print(f"Iniciando partícula {idx + 1}/{cantidad}...")
            p = Particula(rango_x, rango_y)
            if mostrar:
                print(p)
            grupo.agregar(p)
        return grupo

    def agregar(self, p):
        self.elementos.append(p)

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


# === EJECUCIÓN CON INPUT DEL USUARIO ===

print("=== Simulación de Enjambre de Partículas ===")
cantidad = pedir_entero("Ingrese la cantidad de partículas a generar: ")
rango_x = pedir_rango("X")
rango_y = pedir_rango("Y")

# Crear y mostrar el enjambre
grupo = Enjambre.construir(cantidad=cantidad, rango_x=rango_x, rango_y=rango_y, mostrar=True)
grupo.visualizar()
