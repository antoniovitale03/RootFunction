from Bisezione_FalsaPosizione import Bisezione_FalsaPosizione
from NR_Direzione_Costante import NR_Direzione_Costante
def main():
    response = int(input("Scegli quale algoritmo usare per calcolare la radice della funzione: \n"
                         "1)Bisezione\n"
                         "2)Falsa posizione\n"
                         "3)Netwon Raphson\n"
                         "4)Direzione Costante\n"))
    if response == 1:
        Obj = Bisezione_FalsaPosizione()
        Obj.bisezione(Obj.f, Obj.a, Obj.b, Obj.E, Obj.stop)
    elif response == 2:
        Obj = Bisezione_FalsaPosizione()
        Obj.falsa_posizione(Obj.f, Obj.a, Obj.b, Obj.E, Obj.stop)
    elif response == 3:
        Obj = NR_Direzione_Costante()
        Obj.nr(Obj.f_symb, Obj.x0, Obj.E, Obj.stop)
    elif response == 4:
        Obj = NR_Direzione_Costante()
        Obj.dr(Obj.f_symb, Obj.x0, Obj.E, Obj.stop)
    else:
        print("Input non valido. Riprova.")
        main()

if __name__ == "__main__":
    main()


