letras = [' ' ,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
cifra_cesar = [' ' ,"D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C"]
print("==== CONVERTEDOR DE CIFRA DE CESAR ====")
def converter(frase):
    for l in frase:
        for c in cifra_cesar:
            indice_l = letras.index(l)
            indice_c = cifra_cesar.index(c)
            if indice_c == indice_l:
                print(c, end="")

string = str(input("Informe um frase: ")).strip().upper()
converter(string)
input()
