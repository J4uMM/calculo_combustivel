tipo_combustivel = input("Digite qual combustivel seu carro está usando: ").lower()

distancia = float(input("Digite quantos kms você pretende percorrer: "))

autonomia = float(input("Digite a autonomia de seu carro: "))

def obter_preco_combustivel(tipo_combustivel):
    if tipo_combustivel == "gasolina":
        preco_gasolina = float(input("Digite o preço da gasolina: "))
        return preco_gasolina
    elif tipo_combustivel == "etanol":
        preco_etanol = float(input("Digite o preço do etanol: "))
        return preco_etanol
    else:
        print("Tipo de combustível invalido.")
        return None

def consumo_medio(distancia, preco_combustivel, autonomia):
    if preco_combustivel is not None:
        custo_medio = (preco_combustivel / autonomia ) * distancia
        print(f"O custo médio para percorrer {distancia} km com {tipo_combustivel} é de R$ {custo_medio:.2f}")
    else:
        print("Não foi possível calcular o custo médio devido a um erro no tipo de combustível")

preco_combustivel = obter_preco_combustivel(tipo_combustivel)

consumo_medio(distancia, preco_combustivel, autonomia)



    



