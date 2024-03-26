def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade Grau I"
    elif imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

def main():
    peso = float(input("Digite seu peso em quilogramas: "))
    altura = float(input("Digite sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    print("Seu IMC é:", imc)

    classificacao = classificar_imc(imc)
    print("Classificação do IMC:", classificacao)

if __name__ == "__main__":
    main()
