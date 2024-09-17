from sympy import *

class NR_Direzione_Costante():
    def __init__(self):
        [self.f_symb, self.x0, self.E, self.stop] = self.set_data()
    def set_data(self):
        f_symb = self.set_function() # setto la funzione g di iterazione funzionale
        x0 = float(input("Inserisci il valore iniziale x0: "))
        stop = self.get_stop()
        if stop != 2:
            E = float(input("Inserisci la precisione desiderata: "))  # setto la precisione
        else:
            E = 0 #uso il secondo criterio di stop, quindi non uso la E
        return f_symb, x0, E, stop
    def set_function(self):
        x = symbols("x")
        return sympify(input("Inserisci la funzione: "))  # converte la stringa in funzione simbolica
    def get_stop(self): #restituisce il criterio di stop da usare
        stop = int(input("Scegli quale criterio di stop usare: \n"
                         "1)|g(x) - x| < E\n"
                         "2)k > itmax\n"))
        if stop not in [1, 2]:
            print("Input non valido. Riprova.")
            self.get_stop()
        return stop
    def set_b(self, a): #controlla che b != a
        b = float(input("Estremo destro dell'intervallo: "))
        if b == a or b < a:
            print("L'estremo b è uguale all'estremo a. Riprova.")
            self.set_b(a)
        return b
    def check_interval_values(self, a, b): #controllo che a o b siano diversi da 0 nel metodo di Falsa Posizione
        if a == 0 or b == 0:
            print("Uno dei due estremi è uguale a 0! Riprova.")
            a = float(input("Estremo sinistro dell'intervallo: "))
            b = self.set_b(a)
            self.check_interval_values(a, b)
        return true

    def get_M(self, f_symb, a, b, n):  # n rappresenta il grado della derivata
        v = []
        x = symbols("x")
        devf = lambdify(x, diff(f_symb, x, n))
        v.append(abs(devf(a)))
        v.append(abs(devf(b)))
        return max(v)

    def newthon_raphson(self, f_symb, x0, E):
        #calcolo la funzione di iterazione funzionale g(x)
        x = symbols("x")
        g_symb = x - (f_symb/diff(f_symb)) #funzione g simbolica
        g = lambdify(x, g_symb) #funzione g matematica
        k = 0
        x1 = g(x0)
        while abs(x1 - x0) > E:
            x0 = x1
            x1 = g(x0)
            k += 1
        c = x1
        print(f"radice della funzione: {c} con {k} iterazioni")

    def get_g_newthon_raphson(self, f_symb):#calcolo la funzione di iterazione funzionale g(x)
        x = symbols("x")
        g_symb = x - (f_symb/diff(f_symb))  # funzione g simbolica
        return lambdify(x, g_symb)  # funzione g matematica
    def get_g_direzione_costante(self, f_symb, M):
        x = symbols("x")
        g_symb = x - (f_symb/M)  # funzione g simbolica
        return lambdify(x, g_symb)  # funzione g matematica

    def nr_stop1(self, f_symb, x0, E): #newthon raphson con criterio di stop 1
        g = self.get_g_newthon_raphson(f_symb)
        k = 0
        x1 = g(x0)
        while abs(x1 - x0) > E:
            x0 = x1
            x1 = g(x0)
            k += 1
        c = x1
        print(f"radice della funzione: {c} con {k} iterazioni")

    def nr_stop2(self, f_symb, x0): #newthon raphson con criterio di stop 2
        g = self.get_g_newthon_raphson(f_symb)
        itmax = int(input("Inserisci il numero di iterazioni massime: "))
        k = 0
        x1 = g(x0)
        while k < itmax:
            x0 = x1
            x1 = g(x0)
            k += 1
        c = x1
        print(f"radice della funzione: {c} con {k} iterazioni")

    def dr_stop1(self, f_symb, x0, E, M): #metodo della direzione costante con criterio di stop 1
        g = self.get_g_direzione_costante(f_symb, M)
        k = 0
        x1 = g(x0)
        while abs(x1 - x0) > E:
            x0 = x1
            x1 = g(x0)
            k += 1
        c = x1
        print(f"radice della funzione: {c} con {k} iterazioni")

    def dr_stop2(self, f_symb, x0, M): #metodo della direzione costante con criterio di stop 2
        g = self.get_g_direzione_costante(f_symb, M)
        itmax = int(input("Inserisci il numero massimo di iterazioni: "))
        k = 0
        x1 = g(x0)
        while k < itmax:
            x0 = x1
            x1 = g(x0)
            k += 1
        c = x1
        print(f"radice della funzione: {c} con {k} iterazioni")
    def nr(self, f_symb, x0, E, stop):
        if stop == 1:
            self.nr_stop1(f_symb, x0, E)
        elif stop == 2:
            self.nr_stop2(f_symb, x0)
    def dr(self, f_symb, x0, E, stop):
        #devo usare l'intervallo [a, b] per calcolare M
        a = float(input("Inserisci l'estremo sinistro: "))
        b = self.set_b(a)
        self.check_interval_values(a, b)
        M = self.get_M(f_symb, a, b, 1)
        if stop == 1:
            self.dr_stop1(f_symb, x0, E, M)
        elif stop == 2:
            self.dr_stop2(f_symb, x0, M)