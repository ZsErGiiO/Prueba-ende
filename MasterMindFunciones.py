def generar_codigo(): #Esta funcion hace que el jugador 1 y jugador 2 escriban sus respectivas letras
    letras = []
    while len(letras) < 4:
        letra = input("dime una letra: ").lower()
        if letra in letras or letra <"a" or letra >"i":
            print("Esta letra ya fue ingresada o no esta en el rango, dime otra letra")
        else:
            letras.append(letra)
    return letras
    
def limpiar_pantalla(seg): #Esta funcion simplemente limpia la pantalla
    import os
    import time
    time.sleep(seg)
    os.system('cls')
    
def comprobar(letra_respuesta, letra_encriptada): #Esta funcion compara las letras del jugador 1 y jugador 2 
                                                  #y te escribe si esta en otro lado, si esta  bien o si no esta
    resultado=""
    for x in range(4):
        if letra_respuesta[x] == letra_encriptada[x]:
            resultado += letra_encriptada[x]
        elif letra_respuesta[x] in letra_encriptada:
            resultado +="x"
        else:
            resultado+="0"
    print(resultado)

def comprobar_repeticion(letra_repetida, letra_encriptada): #Esta funcion compara las letras del jugador 1 con las letras del jugador 2 que 
                                                            #ha repetido porque ha fallado y hace lo mismo que la de comprobar normal
    resultado=""
    for x in range(4):
        if letra_repetida[x] == letra_encriptada[x]:
            resultado += letra_encriptada[x]
        elif letra_repetida[x] in letra_encriptada:
            resultado +="x"
        else:
            resultado+="0"
    print(resultado)

def acabar():#Esta funcion acaba el juego si pones zzzz
    acabar=input("Si quieres acabar el juego pon zzzz: ")
    while acabar:
        if acabar=="zzzz":
            print("El juego ha acabado")
        break

"Aqui la prueba de que estan conectados"