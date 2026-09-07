#Programa de consumo de energia.
#Autor: Crystian

#Entrada de dados
nome = input ("Digite o nome do aparelho")
potencia = float (input ("Digite a potencia do aparelho em watts "))
tempo = float (input ("Digite o tempo medio de uso diario em horas "))

#Processamento
consumoMensal = (potencia *tempo *30) / 1000
valorKwh = 0.75
custoMensal = consumoMensal * valorKwh

#Saida
print(f"Aparelho: {nome}")
print(f"Consumo estimado: {consumoMensal:.2f} kWh/mes")
print(f"Custo estimado: R$ {custoMensal:.2f} por mes")