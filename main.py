from Bisezione_FalsaPosizione import Bisezione_FalsaPosizione
from Newthon_Raphson import Newthon_Raphson

def main():
    response = int(input("Scegli quale algoritmo usare per calcolare la radice della funzione: \n"
                         "1)Bisezione\n"
                         "2)Falsa posizione\n"
                         "3)Netwon Raphson\n"))
    if response == 1:
        Obj = Bisezione_FalsaPosizione()
        Obj.bisezione(Obj.f, Obj.a, Obj.b, Obj.E, Obj.stop)
    elif response == 2:
        Obj = Bisezione_FalsaPosizione()
        Obj.falsa_posizione(Obj.f, Obj.a, Obj.b, Obj.E, Obj.stop)
    elif response == 3:
        Obj = Newthon_Raphson()
        [radice, k] = Obj.NR(Obj.g, Obj.x0, Obj.E)
        print(f"radice della funzione: {radice} con {k} iterazioni")
    else:
        print("Input non valido. Riprova.")
        main()

if __name__ == "__main__":
    main()


