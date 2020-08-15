class Polinomio:
    
    def __init__(self, expressao):
        if isinstance(expressao, list):
            self.__termos = expressao
        else:
            self.__termos = self.converte_para_lista(expressao)
        
    def grau(self):
        return len(self.__termos) - 1
    
    def tranforma_em_numero(self, elemento):
        if elemento == "":
            numero = 1
        elif elemento in "-+":
            numero = int(elemento+"1")
        else:
            numero = int(elemento)
        return numero

    def converte_para_lista(self, sp):
        cursor = 0
        lista = None
        while cursor < len(sp):
            i = cursor+1
            while i < len(sp) and sp[i] not in ['-', '+']:
                i += 1
            termo = sp[cursor:i]
            partes = termo.split('x')
            coeficiente = self.tranforma_em_numero(partes[0])
            # [ "", "3"]  ["4", "3"]    ["+", "2"]   ["-2", ""] 
            if len(partes) == 2:
                expoente = self.tranforma_em_numero(partes[1])
                # [ "", "3"]  ["4", "3"]    ["+", "2"]   ["-2", ""]
            else:
                expoente = 0
            if lista == None:
                #         ["-2"]
                lista = [0] * (expoente+1)
            lista[expoente] = coeficiente
            cursor = i
        return lista
        
    def soma(self, pol):       
        if len(self.__termos) > len(pol.__termos):
            soma = self.__termos[:]
            for i in range(len(pol.__termos)):
                soma[i] += pol.__termos[i]
        else:
            soma = pol.__termos[:]
            for i in range(len(self.__termos)):
                soma[i] += self.__termos[i]    
        return Polinomio(soma).__ajusta()

    def multiplica_por_escalar(self, valor):
        return Polinomio([termo * valor for termo in self.__termos])

    def subtrai(self, pol):
        return self.soma(pol.multiplica_por_escalar(-1))
    
    def __ajusta(self):
        while len(self.__termos) > 1 and self.__termos[-1] == 0:
            self.__termos.pop()
        return self
    
    def avalia(self, x):
        soma = 0
        for exp, cte in enumerate(self.__termos):
            soma += cte * x ** exp
        return soma
    
    def __str__(self):
        if self.__termos == [0]:
            return "0"

        str_pol = ""
        for exp, cte in enumerate(self.__termos):
            if cte > 0:
                cte = "+" + str(cte)
            if exp == 0 and cte != 0:
                str_pol = str(cte) + str_pol
            elif cte != 0:
                str_pol = str(cte) + "x" + str(exp) + str_pol

        if str_pol[0] == "+":
            str_pol = str_pol[1:]
        if str_pol[0:2] == "1x":
            str_pol = str_pol[1:]
        if str_pol[0:2] == "-1xa":
            str_pol = str_pol[2:]
        if str_pol[-2:] == "x1":
            str_pol = str_pol[:-1]
        return (
            str_pol
            .replace("+1x", "+x")
            .replace("-1x", "-x")
            .replace("x1+", "x+")
            .replace("x1-", "x-")
        )

    def get_termos(self):
        return self.__termos

# main
texto_p1 = "13x14-102x2+3x"
texto_p2 = "-7x4+2x2-3x"
operacao = "+"

# texto_p1 = input()
# texto_p2 = input()
# operacao = input()

p1 = Polinomio(texto_p1)
p2 = Polinomio(texto_p2)

if operacao == "+":
    p_resultado = p1.soma(p2)
elif operacao == "-":
    p_resultado = p1.subtrai(p2)

print(p_resultado.get_termos())
print(p_resultado.__str__())