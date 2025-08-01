estudiantes = {}
print(".........Calculo de promedio de estudiantes.........")

cantidad = int(input("¿Cuántos estudiantes desea ingresar?: "))

for i in range(cantidad):
    print(f"\nEstudiante #{i + 1}:")

    nombre = input("Nombre completo del estudiante: ").strip()
    cantidad_notas = input("Ingrese la cantidad de notas que desea ingresar: ")

for j in range(cantidad_notas):
    print(f"\nNota #{i + 1}:"

    try:
        num1 = float(input("Ingresa el numerador: "))
        num2 = float(input("Ingresa el denominador: "))

        resultado = num1 / num2

        texto = "10"
        suma = resultado + texto

    except ValueError:
    print("Error: Debes ingresar números válidos.")

    except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

    except TypeError:
    print("Error: No puedes combinar diferentes tipos de datos (por ejemplo, número + texto).")

    except Exception as e:
    print("Se produjo un error inesperado:", e)

    else:
    print(f"Resultado de la división: {resultado}")
    print(f"Suma con texto (esto no debería ejecutarse): {suma}")

    finally:
    print("Fin del proceso.")