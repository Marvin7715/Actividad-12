def pedir_entero_positivo(prompt):
    while True:
        entrada = input(prompt).strip()
        try:
            valor = int(entrada)
            if valor <= 0:
                print("  Error: Debes ingresar un número entero mayor que cero.")
                continue
        except ValueError:
            print("  Error: Entrada no es un número entero válido. Intenta de nuevo.")
        else:
            return valor

def pedir_flotante(prompt):
    while True:
        entrada = input(prompt).strip()
        try:
            valor = float(entrada)
        except ValueError:
            print("    Error: Debes ingresar un número válido. Intenta de nuevo.")
        else:
            return valor

print(".........Cálculo de promedio de estudiantes.........")
estudiantes = {}

try:
    cantidad = pedir_entero_positivo("¿Cuántos estudiantes desea ingresar?: ")

    for i in range(1, cantidad + 1):
        print(f"\nEstudiante #{i}:")
        nombre = input("Nombre completo del estudiante: ").strip()
        if not nombre:
            nombre = f"Estudiante_{i}"
            print(f"  Nombre vacío, se asignó '{nombre}'.")

        try:
            cantidad_notas = pedir_entero_positivo("Ingrese la cantidad de notas que desea ingresar: ")

            notas = []
            for k in range(1, cantidad_notas + 1):
                nota = pedir_flotante(f"  Nota #{k}: ")
                notas.append(nota)

            try:
                promedio = sum(notas) / len(notas)
            except ZeroDivisionError:
                print("  Error: No se puede calcular el promedio con cero notas.")
                promedio = 0.0
            except TypeError:
                print("  Error: Tipo de dato inválido al calcular el promedio.")
                promedio = 0.0
            else:
                print(f"Promedio de {nombre}: {promedio:.2f}")
            finally:
                estudiantes[nombre] = promedio
                print(f"Fin del registro de '{nombre}'.\n")

        except Exception as e:
            print(f"  Error inesperado al ingresar las notas de '{nombre}': {e}")
            estudiantes[nombre] = 0.0

except Exception as e:
    print(f"Error inesperado al iniciar el registro: {e}")

print("\n--- Resultados finales ---")
for nombre, promedio in estudiantes.items():
    print(f"{nombre}: {promedio:.2f}")