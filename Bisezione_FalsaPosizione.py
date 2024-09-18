import math
import sys
from sympy import *
class Bisezione_FalsaPosizione():
    def __init__(self):
        [self.f, self.a, self.b, self.E, self.stop] = self.set_data()
    def set_b(self, a): #controlla che b != a
        b = float(input("Estremo destro dell'intervallo: "))
        if b == a or b < a:
            print("L'estremo b è uguale all'estremo a. Riprova.")
            self.set_b(a)
        return b
    def set_function(self):
        x = symbols("x")
        f_symb = sympify(input("Inserisci la funzione: "))  # converte la stringa in funzione simbolica
        f = lambdify(x, f_symb)  # trasforma la funzione simbolica in espressione matematica
        return f
    def get_stop(self): #restituisce il criterio di stop da usare
        stop = int(input("Scegli quale criterio di stop usare: \n"
                         "1)|f(c)| < E\n"
                         "2)k > itmax\n"
                         "3)b - a < E\n"
                         "4)(b - a)/min(|a|, |b|) < E\n"))
        if stop not in [1, 2, 3, 4]:
            print("Input non valido. Riprova.")
            self.get_stop()
        return stop
    def set_data(self):
        f = self.set_function() #setto la funzione
        a = float(input("Estremo sinistro dell'intervallo: "))   #setto l'estremo a
        b = self.set_b(a)  #setto l'estremo b (controllo se è diverso da a)
        stop = self.get_stop()
        if stop != 2:
            E = float(input("Inserisci la precisione desiderata: "))  # setto la precisione
        else:
            E = 0 #uso il secondo criterio di stop, quindi non uso la E
        return f, a, b, E, stop
    def check_interval_values(self, a, b): #controllo che a o b siano diversi da 0 nel metodo di Falsa Posizione
        if a == 0 or b == 0:
            print("Uno dei due estremi è uguale a 0! Riprova.")
            a = float(input("Estremo sinistro dell'intervallo: "))
            b = self.set_b(a)
            self.check_interval_values(a, b)
        return true
    def bisezione_comune(self, f, a, b): #istruzioni comuni del metodo di bisezione per tutti i criteri di stop
        c = 0
        if (f(a) * f(b)) > 0:
            print("Non esistono radici reali.")
            sys.exit(0)
        elif (f(a) * f(b)) < 0:
            c = (a+b)/2
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        return a, b, c

    def result(self, c, k):
        return f"radice della funzione: {round(c, 4)} con {k} iterazioni"
    def bisezione_stop1(self, f, a, b, E):
        k = 0
        c = 0
        while abs(f(c)) > E: #criterio 1
            [a, b, c] = self.bisezione_comune(f, a, b)
            k += 1
        self.result(c, k)
    def bisezione_stop2(self, f, a, b):
        k = 0
        c = 0
        itmax = int(input("Indica il numero massimo di iterazioni consentite: "))
        while k < itmax: #criterio 2
            [a, b, c] = self.bisezione_comune(f, a, b)
            k += 1
        self.result(c, k)
    def bisezione_stop3(self, f, a, b, E):
        k = 0
        c = 0
        while k < math.ceil(math.log2((b-a)/E)): #criterio 3
            [a, b, c] = self.bisezione_comune(f, a, b)
            k += 1
        self.result(c, k)
    def bisezione_stop4(self, f, a, b, E):
        k = 0
        c = 0
        while (b-a)/min(abs(a), abs(b)) > E:
            [a, b, c] = self.bisezione_comune(f, a, b)
            k += 1
        self.result(c, k)
    def bisezione(self, f, a, b, E, stop):
        if stop == 1:
            self.bisezione_stop1(f, a, b, E)
        elif stop == 2:
            self.bisezione_stop2(f, a, b)
        elif stop == 3:
            self.bisezione_stop3(f, a, b, E)
        elif stop == 4:
            self.bisezione_stop4(f, a, b, E)
    def falsa_posizione_comune(self, f, a, b):
        c = 0
        if (f(a) * f(b)) > 0:
            print("Non esistono radici reali.")
            sys.exit(0)
        elif f(a) * f(b) < 0:
            c = a - (f(a)*(b - a)/(f(b) - f(a)))
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        return a, b, c
    def falsa_posizione_stop1(self, f, a, b, E):
        k = 0
        c = 0
        while abs(f(c)) > E: #criterio 1
            [a, b, c] = self.falsa_posizione_comune(f, a, b)
            k += 1
        self.result(c, k)
    def falsa_posizione_stop2(self, f, a, b):
        k = 0
        c = 0
        itmax = int(input("Indica il numero massimo di iterazioni consentite: "))
        while k < itmax:  # criterio 2
            [a, b, c] = self.falsa_posizione_comune(f, a, b)
            k += 1
        self.result(c, k)
    def falsa_posizione_stop3(self, f, a, b, E):
        k = 0
        c = 0
        while k < math.ceil(math.log2((b-a)/E)):  # criterio 3
            [a, b, c] = self.falsa_posizione_comune(f, a, b)
            k += 1
        self.result(c, k)
    def falsa_posizione_stop4(self, f, a, b, E):
        k = 0
        c = 0
        while ((b - a)/min(abs(a), abs(b))) > E: #criterio 4
            [a, b, c] = self.falsa_posizione_comune(f, a, b)
            k += 1
        self.result(c, k)
    def falsa_posizione(self, f, a, b, E, stop):
        if self.check_interval_values(a, b):
            if stop == 1:
                self.falsa_posizione_stop1(f, a, b, E)
            elif stop == 2:
                self.falsa_posizione_stop2(f, a, b)
            elif stop == 3:
                self.falsa_posizione_stop3(f, a, b, E)
            elif stop == 4:
                self.falsa_posizione_stop4(f, a, b, E)


