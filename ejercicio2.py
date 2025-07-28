'''
Una persona promedio dice 2 palabras x segundo.

Perdirle al usuario que ingrese un texto y:
    1) Contabiliar el tiempo que demoraria en decirlo
    2) Cuantas palabras dijo?
    3) si tarda mas de un minuto, motrar en pantalla :
        "para flaco, no te pedi un testamento"
    4) Cuanto demoraria una persona que habla un 30% mas rapido?
'''

texto = input("Ingrese un texto: \n-");
palabras_separadas = texto.split(" ");
cantidad_de_palabras = len(palabras_separadas);
tiempo = (cantidad_de_palabras / 2);

if(tiempo >= 60):
    print("\n"+"-Para flaco, no te pedi un testamento" + "\n");
else:
    print("\n"+f"-Su tiempo en decir {cantidad_de_palabras} palabras, seria de {tiempo} Seg, "+ "\n");
    
rapido = 0.3;
texto_rapido = tiempo - (tiempo * rapido);
print("\n"+f"- Una persona que habla 30% mas rapido lo diria en {texto_rapido} Seg" + "\n");
