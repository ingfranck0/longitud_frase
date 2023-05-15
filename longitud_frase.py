#definicion de la palabra
palabra = input("Ingresa una palabra: ")
#definiendo parametros 
if len(palabra) < 4:
    print("Hacen falta letras. Solo tiene", len(palabra), "letras")
elif len(palabra) > 8:
    print("Sobran letras. Tiene", len(palabra), "letras")
else:
    print("La palabra es correcta")
