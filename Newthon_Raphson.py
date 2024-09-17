from sympy import *
class Newthon_Raphson():
    def __init__(self):
        [self.g, self.x0, self.E] = self.set_data()
    def set_data(self):
        g = self.set_function() # setto la funzione g di iterazione funzionale
        x0 = float(input("Inserisci il valore iniziale x0: "))
        E = float(input("Inserisci la precisione desiderata: "))
        return g, x0, E

    def set_function(self):
        x = symbols("x")
        f_symb = sympify(input("Inserisci la funzione: "))  # converte la stringa in funzione simbolica
        g_symb = x - (f_symb/diff(f_symb))
        g = lambdify(x, g_symb)
        return g

    def newthon_raphson(self, g, x0, E):
        k = 0
        x1 = g(x0)
        while abs(x1 - x0) > E:
            x0 = x1
            x1 = g(x0)
            k += 1
        c = x1
        print(f"radice della funzione: {c} con {k} iterazioni")
