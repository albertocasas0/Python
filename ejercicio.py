from datetime import datetime
now = datetime.now()

def pedir_datos():
 nombre = input('Ingrese su Nombre: ');
 apellido = input('Ingrese su Apellido: ');
 anio = input('Ingrese su anio de nacimiento: ');
 edad = int(now.year)- int(anio);
 return nombre, apellido, edad;  

nombre, apellido, edad = pedir_datos()

if (edad >= 18):
    print(f'\nBienvenido {nombre + " " + apellido },\nUsted tiene {edad} anios de edad.\nTiene permitido el ingreso ');    
else:
    while edad < 18:
     print(f'\n{nombre + " "+ apellido}, Usted es menor de edad. \nLo sentimos, no puede ingresar, sin un mayor a cargo!');
     respuesta = input('Hay alguna persona mayor con usted?? Si o No\n');
   
     if((respuesta == "si") | (respuesta == "Si")):
         nombre, apellido, edad = pedir_datos()
         
         
     else:
         print("Sera la proxima. Nos veremos pronto.");
         break
    
     print("Pueden pasar.")
