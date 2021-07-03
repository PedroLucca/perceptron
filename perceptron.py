import numpy as np

class Perceptron:
    def __init__(self, n, variaveis):
        self.n = n
        self.pesos = [0.5, 0.6, -0.4]
        self.variaveis = variaveis

    def algoritmo(self):
        self.x_var = []
        self.y_var = []
        self.pesos = np.array(self.pesos)

        for i in range(0, self.n+1):
            for j in range(0, self.n+1):
                self.variaveis[i][j] = float(self.variaveis[i][j])

        passo = 0
        for k in range(0,40):
            self.x_var = self.variaveis[passo][:-1]
            self.y_var = self.variaveis[passo][-1]
            
            self.x_var = np.array(self.x_var)
            self.y_var = int(self.y_var)


            print(self.x_var)
            print(self.pesos)
            net = (self.x_var*self.pesos)

            #print(net)

            if net.any() >= 0:
                net = 1
            else:
                net = 0
            

            #print(self.y_var)
            erro = self.y_var - net
            
            for i in range(0,self.n):
                self.pesos[i] = self.pesos[i] + 0.6*erro*self.x_var[i]

            print(self.x_var)
            passo = passo + 1

            if passo >= 3:
                passo = 0

            print("-------------\n")
            print("Entradas", self.x_var)
            print("Alvo", self.y_var)
            print("Net", net)
            
        print("--- Finalizou ---\n Pesos:", self.pesos)
