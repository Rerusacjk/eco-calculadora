import matplotlib.pyplot as plt

# 1. Calculadora de huella de carbono
def calcular_huella(km_auto, consumo_energia, carne_semanal):
    CO2_auto = km_auto * 0.21
    CO2_energia = consumo_energia * 0.4
    CO2_carne = carne_semanal * 7 * 2.5
    total = CO2_auto + CO2_energia + CO2_carne
    return total

# 2. Conversor de energía a renovable estimada
def conversion_renovable(kwh_total, porcentaje_renovable):
    kwh_renovable = kwh_total * (porcentaje_renovable / 100)
    kwh_fosil = kwh_total - kwh_renovable
    return kwh_renovable, kwh_fosil

# 3. Visualizador de emisiones por país (datos ficticios)
def visualizar_emisiones():
    paises = ['EE.UU.', 'China', 'India', 'Alemania', 'Brasil']
    emisiones = [5000, 10000, 3000, 2000, 1500]  # en millones de toneladas

    plt.bar(paises, emisiones, color='green')
    plt.title("🌎 Emisiones de CO2 por país (estimadas)")
    plt.ylabel("Emisiones (millones de toneladas)")
    plt.xlabel("País")
    plt.show()

# 4. Sugerencias según la huella
def sugerencias(huella):
    print("\n📊 Huella anual estimada:", round(huella, 2), "kg de CO2")
    if huella > 10000:
        print("🔴 Alta huella. Considera:")
        print("- Cambiar a transporte público.")
        print("- Reducir carne roja.")
        print("- Usar energía renovable.")
    elif huella > 5000:
        print("🟠 Huella media. Puedes mejorar:")
        print("- Apagar dispositivos.")
        print("- Comer menos carne.")
    else:
        print("🟢 Huella baja. ¡Buen trabajo!")

# Menú principal
def menu():
    while True:
        print("\n🌿 MULTI-TOOL CLIMÁTICO")
        print("1. Calcular huella de carbono")
        print("2. Convertir energía a renovable")
        print("3. Visualizar emisiones por país")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            km = float(input("Km en auto por semana: ")) * 52
            energia = float(input("kWh de energía mensual: ")) * 12
            carne = int(input("Días a la semana que comes carne: "))
            huella = calcular_huella(km, energia, carne)
            sugerencias(huella)
        elif opcion == "2":
            total = float(input("Total de kWh consumidos al mes: "))
            renovable = float(input("Porcentaje que proviene de fuentes renovables: "))
            ren, fosil = conversion_renovable(total, renovable)
            print(f"🔋 Renovable: {ren} kWh, Fósil: {fosil} kWh")
        elif opcion == "3":
            visualizar_emisiones()
        elif opcion == "4":
            print("Gracias por usar la herramienta climática 🌍")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
menu()