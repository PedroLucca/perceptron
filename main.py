from perceptron import Perceptron

variaveis = []
novo_array = []
entrada = open('entrada.txt', 'r')
for line in entrada:
    variaveis.append(line.rstrip("\n"))
for i in variaveis:
    novo_array.append(i.split(" "))
variaveis = novo_array

pc = Perceptron(2)
print(pc.n)
