Calculadora de IMC

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Peso bajo"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)

    print(f"Su IMC es: {imc:.2f}")
    print(f"Su clasificación es: {clasificacion}")

if __name__ == "__main__":
    main()
