UMBRAL_MEDIO    = 2.5
UMBRAL_ALTO     = 5.0

print("Ingrese su nombre")
nombre = input()
print("ingrese su nombre de equipo")
equipo = input()

print("Ingrese el primer voltaje medido")
voltaje1 = float(input())
print("Ingrese el segundo voltaje medido")
voltaje2 = float(input())

PROMEDIO_VOLTAJE = (voltaje1 + voltaje2) / 2

print(f"Alumno: {nombre}, Equipo : {equipo}", f"lecturas: {voltaje1:.2f}", f"voltaje: {voltaje2:.2f}")
PROMEDIO_VOLTAJE = float(f"{PROMEDIO_VOLTAJE:.2f}")
try:
    if PROMEDIO_VOLTAJE < 2.5:
        print("El voltaje promedio es BAJO")
    elif UMBRAL_MEDIO < PROMEDIO_VOLTAJE < UMBRAL_ALTO:
        print("El voltaje promedio es MEDIO")
    else:
        print("El voltaje promedio es ALTO")
except ValueError:
    print("valores ingresados incorrectos")
    