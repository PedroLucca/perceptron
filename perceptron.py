import numpy as np

class Perceptron:
    def __init__(self, n, variaveis):
        self.n = n
        self.pesos = [-0.3, 0.5, 0.6]
        self.variaveis = variaveis

    def algoritmo(self):
        self.x_var = []
        self.y_var = []
        self.pesos = np.array(self.pesos)

        for i in range(0, self.n+2):
            for j in range(0, self.n+2):
                self.variaveis[i][j] = float(self.variaveis[i][j])

        passo = 0
        for k in range(0,200):
            self.x_var = self.variaveis[passo][:-1]
            self.y_var = self.variaveis[passo][-1]
            
            self.x_var = np.array(self.x_var)
            self.y_var = int(self.y_var)

            net = (self.x_var*self.pesos)
            net_aux = 0

            for i in net:
                net_aux += i

            if net_aux >= 0:
                net_aux = 1
            else:
                net_aux = 0
            
            erro = self.y_var - net_aux
            
            for i in range(0,self.n+1):
                self.pesos[i] = self.pesos[i] + 0.1*erro*self.x_var[i]

            passo = passo + 1

            if passo >= 4:
                passo = 0

            print("-------------\n")
            print("Entradas", self.x_var)
            print("Alvo", self.y_var)
            print("Net", net_aux)
            
        print("--- Finalizou ---\n Pesos:", self.pesos)
