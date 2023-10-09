# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o caro custa R$ 60,00 por dia e R$ 0,15 por KM rodado

quilometragem = float(input("Digite a quantidade de quilômetros percorridos: "))
dias = float(input("Digite a quantidade de dias que o veículo foi alugado: "))

preco_pagar = (dias * 60) + (quilometragem * 0.15)

print(f"O preço a pagar pelo aluguel é R${preco_pagar}.")
