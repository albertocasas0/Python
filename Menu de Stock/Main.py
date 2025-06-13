import os
from funciones_menu import *

def clear_terminal():
    #Para windows
    if os.name == "nt":
        os.system("cls")

clear_terminal()

#menú de opciones
       
def main():
    
 opcion=0
 opcion2=9
 
 while opcion != 8:
            
    mostrar_menu()
  
    
    if opcion2 < 9:
        opcion = opcion2
        opcion2 = 9
    else:
        opcion = int(input("| Seleccione una opcion: "))
        print(Fore.LIGHTMAGENTA_EX +"|_______________________________________________|")
    
    if opcion > 8:
        while (opcion > 8 and opcion2 > 8 ):
            opcion2 = int(input(Fore.RED+"\nA ingresado una opcion NO valida.\nPor favor ingrese una opcion del menú\n(INGRESE 0 si no recuerda las opciones): ")+Fore.WHITE)
    else:
        
        if opcion == 1:
        #Alta de productos
         cargar_producto()
        
        elif opcion == 2:
        #mostrar productos, cantidades y precios ingresados
         mostrar_articulos()
        
        elif opcion == 3:
        #Modificar la cantidad de stock de un producto
         modificar_producto()
            
        elif opcion == 4:
        #Dar de baja de producto
            dar_debaja_producto()
        
        elif opcion == 5:
            # Búsqueda de productos:
            buscar_producto()

        elif opcion == 6:
            #Lista de productos con cantidad bajo minimo "50"
            listar_stock_bajo()
        elif opcion == 7:
            #VENDER
            vender_producto()
        elif opcion == 8:
            #Exit
            print(Fore.LIGHTGREEN_EX+"\nGracias! hasta Pronto.\n")
            break    

 print(Fore.RED+"\nFin")

crear_base_de_datos_y_tablas() 
main()