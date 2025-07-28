aula = ["alberto", "pedro", "juan", "sofia", "nahuel", "sabrina", "nehuel", "jazmin"];

zoo = ["león", "gorila", "liebre","cocodrilo", "serpiente", "iguana", "delfin", "mono"];



#for alumno,animal in zip(aula, zoo):
#    print("Alumno: ",alumno);
#    print("Animal: ", animal,"\n");

#numeros = [1,3,4,5,7,8,0,55];   
#for  num in enumerate(numeros):
#    posicion = num[0];
#    valor = num [1];
#    if valor == 4:
#        print(f"indice {posicion} y el valor es {valor}");
        
diccionario = {
     "nombre": "juan",
     "apellido" : "mortimer",
     "edad": 10,
     "estado civil": "casado"   
 };

#Solo muestra las llaves
for key in diccionario:
    print("la key es: ",key);

print("\n"); 

#muestra las claves y sus valores. repitiendose por cantidad de llaves que posea
for datos in diccionario:
    print(diccionario);

print("\n"); 

#Recorre y muestra cada clave y valor    
for key in diccionario.items():
    print("clave y valor:", key);    
    

print("\n"); 
    
# Asignamos las claves a una variable y sus valores a otra variable (vectores)   
for dato in diccionario.items():
    key = dato [0];
    value = dato [1];
    print(f"clave: {key},  valor: {value}");