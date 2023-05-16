from MasterMindFuncion import generar_codigo, limpiar_pantalla, comprobar, comprobar_repeticion, acabar



letra_encriptada = generar_codigo()

print("estas son tus letras J1: ", letra_encriptada)

limpiar_pantalla(3)

letra_respuesta = generar_codigo()

print("estas son tus letras J2: ", letra_respuesta)

limpiar_pantalla(2)

print("Comprobando...")

limpiar_pantalla(2)

print(letra_respuesta)
  
comprobar(letra_respuesta, letra_encriptada)

if letra_encriptada == letra_respuesta:
        print("!Has ganado, esta era las letras!",letra_encriptada )
        acabar()

else:
    acabar=input("Si quieres acabar el juego pon zzzz o pulsa cualquier letra para seguir: ")
    while letra_encriptada != letra_respuesta:
        
        if acabar=="zzzz":
            print("el juego ha acabado")
            break
        else:
            print("el juego sigue...")

            limpiar_pantalla(3)
            
            letra_repetida = generar_codigo()
            
            limpiar_pantalla(2)

            print("Comprobando...")

            limpiar_pantalla(2)
        
            print(letra_repetida)
            comprobar_repeticion(letra_repetida, letra_encriptada)

            if letra_encriptada == letra_repetida:
                print("!Has ganado, esta era las letras!",letra_encriptada ) 
                acabar=input("Si quieres acabar el juego pon zzzz: ")
                if acabar=="zzzz":
                    print("El juego ha acabado") 
                    break
            else:
                acabar=input("Si quieres acabar el juego pon zzzz o pulsa cualquier letra para seguir: ")
                if acabar=="zzzz":
                    print("El juego ha acabado")
                break