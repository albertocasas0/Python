import sqlite3
from colorama import init, Fore, Back, Style

inventario = []
init(autoreset=True)

def conectar_db():
    return sqlite3.connect('Inventario.db')

def crear_base_de_datos_y_tablas():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Crear la tabla 'productos' si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nombre_Producto TEXT NOT NULL,
                        cantidad INTEGER NOT NULL,
                        precio REAL NOT NULL,
                        Categoria TEXT NOT NULL,
                        Descripcion TEXT NOT NULL)''')

    # Confirmar la creación de la tabla
    conexion.commit()   
    conexion.close()

def articulo_y_descripcion_existen(cursor, articulo, descripcion):
    cursor.execute("SELECT COUNT(*) FROM productos WHERE Nombre_Producto = ? AND Descripcion = ?", (articulo, descripcion))
    count = cursor.fetchone()[0]
    return count > 0

def cargar_producto():
    # Conectarse a la base de datos
    conexion = conectar_db()
    cursor = conexion.cursor()

    opcion = input(Fore.YELLOW + "\n¿Ingresás un artículo (S o N)?: "+Fore.WHITE).strip().lower()
    
    while opcion not in ['si', 's', 'no', 'n']:
        opcion = input("\nIngreso una opción NO válida. \n Ingresa 'S' por SI (si quieres ingresar un artículo) o 'N' por NO (en caso que no quieras ingresar un artículo): ").strip().lower()
    
    while opcion not in ['no', 'n']:
        articulo = input(Fore.LIGHTYELLOW_EX+"\nIngresa el nombre del artículo: "+Fore.WHITE).strip().lower()
        descripcion = input(Fore.LIGHTYELLOW_EX+"Ingresa una breve descripción del artículo: "+Fore.WHITE).strip().lower()

        if articulo_y_descripcion_existen(cursor, articulo, descripcion):
            print(Fore.RED+"\nEste artículo con esa descripción ya existe en el inventario. No puede duplicarlo.")
        else:
            cantidad = int( input(Fore.LIGHTYELLOW_EX+"Ingresa la cantidad del producto: "+Fore.WHITE))
            while cantidad <= 0:
                cantidad = int(input(Fore.RED+"La cantidad ingresada NO puede ser menor a 1.\nFavor de ingresar un Stock válido: "+Fore.WHITE))
            
            precio = float(input(Fore.LIGHTYELLOW_EX+"Ingresa el precio del producto: "+Fore.WHITE))
            while precio <= 0:
                precio = float(input(Fore.RED+"El precio ingresado NO puede ser menor o igual a 0.\nFavor de ingresar un precio válido: "+Fore.WHITE))

            categoria = input(Fore.LIGHTYELLOW_EX+"Ingresa la categoría del producto: "+Fore.WHITE).strip()

            try:
                cursor.execute("INSERT INTO productos (Nombre_Producto, cantidad, precio, Categoria, Descripcion) VALUES (?, ?, ?, ?, ?)", 
                               (articulo, cantidad, precio, categoria, descripcion))
                conexion.commit()  # Confirmar la transacción
                print(Fore.LIGHTGREEN_EX+"\nProducto agregado exitosamente.")
            except sqlite3.Error as e:
                print(Back.YELLOW+Fore.RED+f"Error al insertar el producto: {e}"+Back.RESET)

        # Preguntar si se desea ingresar otro producto
        opcion = input(Fore.YELLOW+"\n¿Ingresar otro artículo (S o N)?: "+Fore.WHITE).strip().lower()

    
    conexion.close()
   
def mostrar_articulos():
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    print(Fore.GREEN+"\nProductos ingresados al Local:")
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    
    for listado in productos:
        print(Fore.LIGHTMAGENTA_EX+"ID: "+Fore.WHITE+f"{listado[0]}," +Fore.LIGHTYELLOW_EX+" Artículo: "+Fore.WHITE+f"{listado[1]}," +Fore.LIGHTCYAN_EX+" Descripcion: "+Fore.WHITE+f"{listado[2]}," +Style.BRIGHT+Fore.LIGHTMAGENTA_EX+" Cantidad: "+Fore.WHITE+f"{listado[3]},"+Fore.LIGHTYELLOW_EX+" Precio: "+Fore.LIGHTGREEN_EX+"$"+Fore.WHITE+f"{listado[4]}," +Fore.LIGHTBLUE_EX+" Categoria: "+Fore.WHITE+f"{listado[5]}")
        
    volver = input(Fore.YELLOW+"\nVolver Al Menú Principal? (Si o No): "+Fore.WHITE).lower()
    
    if volver == 'no':
        mostrar_articulos()
    elif volver != "si":
        while volver not in ['si','no']:
            volver = input(Fore.RED+"\nOpcion NO valida. Indique SI para volver al menú o NO para volver a ver los productos ingresados: ").lower()
            if volver == 'no':
                mostrar_articulos()
    
    conexion.close()

def modificar_producto():
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    cambiar = input(Fore.YELLOW+"\n¿Quieres cambiar/modificar un artículo? (si/no): "+Fore.WHITE).strip().lower()
    
    if cambiar == 'si' or cambiar == 's':
        id = int(input(Fore.YELLOW+"\n¿Qué artículo quieres cambiar/actualizar?, indique su ID: "+Fore.WHITE))
        
        # Buscar si el artículo existe en la base de datos
        cursor.execute("SELECT * FROM productos WHERE ID = ?", (id,))
        producto = cursor.fetchone()
        
        if producto:
            print(Fore.LIGHTBLUE_EX+"\nArtículo encontrado:\n"+Fore.LIGHTMAGENTA_EX+"ID: "+Fore.WHITE+f"{producto[0]}," +Fore.LIGHTYELLOW_EX+" Artículo: "+Fore.WHITE+f"{producto[1]}," +Fore.LIGHTCYAN_EX+" Descripcion: "+Fore.WHITE+f"{producto[2]}," +Style.BRIGHT+Fore.LIGHTMAGENTA_EX+" Cantidad: "+Fore.WHITE+f"{producto[3]},"+Fore.LIGHTYELLOW_EX+" Precio: "+Fore.LIGHTGREEN_EX+"$"+Fore.WHITE+f"{producto[4]}," +Fore.LIGHTBLUE_EX+" Categoria: "+Fore.WHITE+f"{producto[5]}")
            nombre = producto[1]
            # Preguntar si desea cambiar el nombre del artículo
            nuevo_articulo = input(Fore.YELLOW+"\n¿Quieres cambiar el nombre del artículo? (si/no): "+Fore.WHITE).strip().lower()
            
            if nuevo_articulo == 'si':
                nuevo_nombre = input(Fore.LIGHTYELLOW_EX+"Ingresa el nuevo nombre del artículo: "+Fore.WHITE).strip().lower()
                cursor.execute("UPDATE productos SET Nombre_Producto = ? WHERE ID = ?", (nuevo_nombre, id))
                print(Fore.GREEN+"\nArtículo cambiado a: "+Fore.BLUE+ f"{nuevo_nombre}")
                nombre = nuevo_nombre
                
            # Preguntar qué desea modificar
            opcion_modificar = input(Fore.YELLOW+"\n¿Qué deseas modificar?\n"+Fore.LIGHTMAGENTA_EX+"1- Cantidad\n"+Fore.LIGHTYELLOW_EX+"2- Precio\n"+Fore.LIGHTGREEN_EX +"3- Ambos\n"+Fore.LIGHTRED_EX+"4- Nada\n"+Fore.YELLOW+"Elige una opción: "+Fore.WHITE).strip()

            if opcion_modificar == '1' or opcion_modificar == '3':
                nueva_cantidad = int(input(Fore.YELLOW+"\n*Ingresa la nueva cantidad: "+Fore.WHITE))
                while nueva_cantidad <= 0:
                    nueva_cantidad = int(input(Fore.RED+"La cantidad no puede ser menor a 1. Ingresa un valor válido: "+Fore.WHITE))
                cursor.execute("UPDATE productos SET cantidad = ? WHERE ID = ?", (nueva_cantidad, id))
                print(Fore.LIGHTYELLOW_EX+"Cantidad de "+Fore.BLUE+nombre +Fore.LIGHTYELLOW_EX+"actualizada a "+Fore.GREEN+f"{nueva_cantidad}.")

            if opcion_modificar == '2' or opcion_modificar == '3':
                nuevo_precio = float(input(Fore.YELLOW+"\n*Ingresa el nuevo precio: "+Fore.WHITE))
                while nuevo_precio <= 0:
                    nuevo_precio = float(input(Fore.RED+"El precio no puede ser menor o igual a 0. Ingresa un valor válido: ")+Fore.WHITE)
                cursor.execute("UPDATE productos SET precio = ? WHERE ID = ?", (nuevo_precio, id))
                print(Fore.LIGHTYELLOW_EX+"Precio de "+Fore.BLUE+ nombre +Fore.LIGHTYELLOW_EX+" actualizado a "+Fore.LIGHTGREEN_EX+"$"+Fore.GREEN+f"{nuevo_precio:.2f}.")

            conexion.commit()

        else:
            print(Fore.RED+f"\nEl artículo '{id}' no se encuentra en el inventario.")
    
    else:
        print(Fore.LIGHTRED_EX+"\nNo se ha realizado ninguna modificación.")
    
    conexion.close()

def dar_debaja_producto():
    conexion = conectar_db()
    cursor = conexion.cursor()

    articulo = input(Fore.YELLOW +"\n¿Qué ID o nombre daremos de baja? (Puedes ingresar el ID o el nombre del producto): "+Fore.WHITE).strip()
    
    # Comprobar si se ingresó un ID
    if articulo.isdigit():
        cursor.execute("SELECT * FROM productos WHERE ID = ?", (int(articulo),))
    else:
        # Si no es un número, buscar por nombre de producto
        cursor.execute("SELECT * FROM productos WHERE Nombre_Producto LIKE ?", ('%' + articulo + '%',))

    productos = cursor.fetchall()

    if productos:
        print(Fore.LIGHTBLUE_EX+"\nSe encontraron los siguientes productos con el ID/nombre "+Fore.MAGENTA+f"'{articulo}':")
        
        for i, producto in enumerate(productos, 1):
            print(Back.BLUE+Fore.WHITE+f"{i}- "+Back.RESET+Fore.LIGHTMAGENTA_EX+"ID: "+Fore.WHITE+f"{producto[0]}," +Fore.LIGHTYELLOW_EX+" Artículo: "+Fore.WHITE+f"{producto[1]}," +Fore.LIGHTCYAN_EX+" Descripcion: "+Fore.WHITE+f"{producto[2]}," +Style.BRIGHT+Fore.LIGHTMAGENTA_EX+" Cantidad: "+Fore.WHITE+f"{producto[3]},"+Fore.LIGHTYELLOW_EX+" Precio: "+Fore.LIGHTGREEN_EX+"$"+Fore.WHITE+f"{producto[4]}," +Fore.LIGHTBLUE_EX+" Categoria: "+Fore.WHITE+f"{producto[5]}")

        # Pedir al usuario seleccionar cuál producto desea eliminar
        try:
            seleccion = int(input(Fore.YELLOW +"\nSelecciona el número del producto que deseas eliminar o ingresa 0 para salir: "+Fore.WHITE))
            if seleccion == 0:
                print(Fore.RED+"\nOperación cancelada.")
            elif 1 <= seleccion <= len(productos):
                producto_seleccionado = productos[seleccion - 1]
                print(Fore.YELLOW +"\nProducto seleccionado: "+Fore.LIGHTMAGENTA_EX+"ID:"+Fore.WHITE+f"{producto_seleccionado[0]}, {producto_seleccionado[1]},"+Fore.LIGHTCYAN_EX+" obs:"+Fore.WHITE +f"{producto_seleccionado[2]},"+Fore.LIGHTMAGENTA_EX+" Cant: "+Fore.WHITE +f"{producto_seleccionado[3]},"+Fore.LIGHTYELLOW_EX+" precio: "+Fore.LIGHTGREEN_EX+"$"+Fore.WHITE +f"{producto_seleccionado[4]}," +Fore.LIGHTBLUE_EX+" Cat: "+Fore.WHITE +f"{producto_seleccionado[5]} ")
                
                # Confirmación para eliminar
                baja = input(Fore.RED+"¿Deseas eliminarlo? (SI o NO): "+Fore.WHITE).strip().lower()

                if baja == 'si' or baja == 's':
                    # Eliminar el producto seleccionado de la base de datos
                    baja_ID = int(producto_seleccionado[0])
                    cursor.execute("DELETE FROM productos WHERE ID = ?", (baja_ID,))
                    conexion.commit()
                    print(Fore.LIGHTMAGENTA_EX+"\nID:"+Fore.WHITE+f"{producto_seleccionado[0]}, {producto_seleccionado[1]}, {producto_seleccionado[2]},"+Back.GREEN+Fore.RED+" Se eliminó correctamente el producto de la base de datos.")
                else:
                    print(Back.RED+Fore.WHITE+"\nNo se eliminó el producto.")
            else:
                print(Back.YELLOW+Fore.RED+"\nSelección no válida.")
        except ValueError:
            print(Fore.RED+"\nPor favor, ingresa un número válido.")
    else:
        print(Back.RED+Fore.WHITE+f"\nEl artículo '{articulo}' no se encuentra en el inventario.")
    
    conexion.close()

def buscar_producto():
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    try:
        while True:
            articulo = input(Fore.YELLOW +"\n¿Qué ID, nombre o categoría de artículo deseas buscar? "+Fore.LIGHTBLUE_EX).strip()
            if articulo.isdigit():
                cursor.execute("SELECT * FROM productos WHERE ID = ?", (int(articulo),))
            else:
                cursor.execute("SELECT * FROM productos WHERE Nombre_Producto LIKE ? OR Categoria LIKE ?", ('%' + articulo + '%', '%' + articulo + '%'))

            productos = cursor.fetchall()
            
            if productos:
                print(Fore.YELLOW +f"\nSe encontró el siguiente productos: ")        
                for i, producto in enumerate(productos, 1):
                    print(f"{i}- "+Fore.LIGHTMAGENTA_EX+"ID: "+Fore.WHITE+f"{producto[0]}," +Fore.LIGHTYELLOW_EX+" Artículo: "+Fore.WHITE+f"{producto[1]}," +Fore.LIGHTCYAN_EX+" Descripcion: "+Fore.WHITE+f"{producto[2]}," +Style.BRIGHT+Fore.LIGHTMAGENTA_EX+" Cantidad: "+Fore.WHITE+f"{producto[3]},"+Fore.LIGHTYELLOW_EX+" Precio: "+Fore.LIGHTGREEN_EX+"$"+Fore.WHITE+f"{producto[4]}," +Fore.LIGHTBLUE_EX+" Categoria: "+Fore.WHITE+f"{producto[5]}")
            else:
                print(Fore.RED+"\nNo se encontraron productos con el término "+Fore.GREEN +f"'{articulo}'\n")
            
            while True:
                respuesta = input(Fore.YELLOW+"\n¿Quiere buscar otro artículo? (si/no): "+Fore.WHITE).strip().lower()
                if respuesta in ['si', 's']:
                    break
                elif respuesta in ['no', 'n']:
                    print(Fore.GREEN +"\nGracias por usar el sistema de búsqueda. ¡Hasta luego!")
                    return
                else:
                    print(Fore.RED+Back.YELLOW+"Por favor, ingresa 'si' o 'no'.")
    
    finally:
        conexion.close()
  
def listar_stock_bajo():
    # Stock mínimo
    stock_minimo = int(input(Fore.LIGHTYELLOW_EX+"El Stock menor a cuanto quiere buscar?: "+Fore.WHITE))

    conexion = conectar_db()
    cursor = conexion.cursor()

    # Consultar los productos cuyo stock es menor que el mínimo
    cursor.execute("SELECT * FROM productos WHERE cantidad < ?", (stock_minimo,))
    productos_bajo_stock = cursor.fetchall()

    # Mostrar los productos con stock bajo
    if productos_bajo_stock:
        print(Fore.YELLOW+"\nInforme de productos con stock bajo (menos de "+ Fore.RED+f"{stock_minimo}"+Fore.YELLOW+ " unidades):")
        for producto in productos_bajo_stock:
            print(Fore.LIGHTMAGENTA_EX+"ID: "+Fore.WHITE+f"{producto[0]}," +Fore.LIGHTYELLOW_EX+" Artículo: "+Fore.WHITE+f"{producto[1]}," +Fore.LIGHTCYAN_EX+" Descripcion: "+Fore.WHITE+f"{producto[2]}," +Style.BRIGHT+Fore.LIGHTMAGENTA_EX+" Cantidad: "+Fore.WHITE+f"{producto[3]},"+Fore.LIGHTYELLOW_EX+" Precio: "+Fore.LIGHTGREEN_EX+"$"+Fore.WHITE+f"{producto[4]}," +Fore.LIGHTBLUE_EX+" Categoria: "+Fore.WHITE+f"{producto[5]}")
    else:
        print(Fore.RED+"\nNo hay productos con stock bajo (menos de "+Back.LIGHTRED_EX +Fore.WHITE+f"{stock_minimo}"+Back.RESET+Fore.RED+ " unidades).")

    conexion.close()
   
def vender_producto():
    conexion = conectar_db()
    cursor = conexion.cursor()
    costo_de_venta=0
    
    print(Fore.LIGHTMAGENTA_EX +"\n|-----------------------------------------------¬\n|",Style.BRIGHT +Fore.BLUE+ Back.WHITE+ "MENÚ DE VENTAS".center(45," "),Fore.LIGHTMAGENTA_EX +"|\n|_______________________________________________|")
    
    try:
        while True:
            articulo = input(Fore.LIGHTYELLOW_EX+"\n¿Qué ID o artículo deseas Vender? "+Fore.WHITE).strip().lower()

            # buscar por ID
            if articulo.isdigit():
                cursor.execute("SELECT * FROM productos WHERE ID = ?", (int(articulo),))
            else:
                # Si no es un número, buscar por nombre y descripcion.
                descripcion_vendida = input(Fore.LIGHTYELLOW_EX+"¿Qué descripcion? "+Fore.WHITE).strip().lower()
                cursor.execute("SELECT * FROM productos WHERE Nombre_Producto LIKE ? AND descripcion LIKE ?", 
                               ('%' + articulo + '%', '%' + descripcion_vendida + '%'))

            productos = cursor.fetchall()

            # Si no se encontró ningún producto, imprimir mensaje
            if not productos:
                print(Fore.RED+"\nNo se encontró el artículo en el inventario.")
            else:
                try:
                    cantidad_vender = int(input(Fore.LIGHTYELLOW_EX + "¿Cuántos deseas vender?: " + Fore.WHITE).strip())
                    
                    # Verificar que la cantidad a vender sea positiva
                    if cantidad_vender <= 0:
                        print(Fore.RED+"\nLa cantidad a vender debe ser un número positivo.")
                        continue  # Volver a intentar si la cantidad no es válida

                except ValueError:
                    # Si la cantidad no es un número válido, pedir de nuevo
                    print(Fore.RED +"\nPor favor ingresa un número válido para la cantidad en Kg.")
                    continue 

                for producto in productos:
                    cantidad_actual = producto[3]

                    # Si la cantidad a vender es menor o igual al stock disponible
                    if cantidad_vender <= cantidad_actual:
                        nueva_cantidad = cantidad_actual - cantidad_vender
                        cursor.execute("UPDATE productos SET cantidad = ? WHERE ID = ?", (nueva_cantidad, producto[0]))
                        conexion.commit()
                        costo_de_venta = float(producto[4])*cantidad_vender
                        print(Fore.LIGHTGREEN_EX+"\nVenta exitosa.\nSe vendieron: $" +Back.BLUE+ f"{costo_de_venta:.2f}"+ Back.RESET) 
                        print(Fore.LIGHTGREEN_EX+"Quedan " +Back.BLUE+f"{nueva_cantidad}"+ Back.RESET + Fore.LIGHTGREEN_EX+" Kg de "+ Back.BLUE+f"{producto[1]} - {producto[2]}" + Back.RESET + Fore.LIGHTGREEN_EX+" en el inventario.")
                        break  # Si la venta es exitosa, salir del bucle
                    else:
                        # Si no hay suficiente stock, mostrar el mensaje correspondiente
                        print(Back.YELLOW+Fore.RED+f"\nNo hay suficiente stock de {producto[1]}. Solo quedan {cantidad_actual} Kg.")

            otra_venta = input(Fore.GREEN+"\n¿Deseas vender otro artículo? (si/no): "+Fore.WHITE).strip().lower()
            if otra_venta not in ['si', 's']:
                break  # Salir del bucle si no desea vender más productos
                
    finally:
        print(Fore.LIGHTMAGENTA_EX +"|_______________________________________________|")
        conexion.close() #cerrar BD

def mostrar_menu():
    print(Fore.LIGHTMAGENTA_EX +"\n|-----------------------------------------------¬\n|",Style.BRIGHT +Fore.BLUE+ Back.WHITE+ "MENÚ DE OPCIONES".center(45," "),Fore.LIGHTMAGENTA_EX +"|")
    print(Fore.LIGHTMAGENTA_EX +"|-----------------------------------------------¬\n|",Fore.GREEN+"1- Alta de productos Nuevos                  ",Fore.LIGHTMAGENTA_EX +"|")
    print(Fore.LIGHTMAGENTA_EX +"|",Fore.GREEN+"2- Consulta de datos de producto             ",Fore.LIGHTMAGENTA_EX +"|")
    print(Fore.LIGHTMAGENTA_EX +"|",Fore.GREEN+"3- Modificar                                 ",Fore.LIGHTMAGENTA_EX +"|")
    print(Fore.LIGHTMAGENTA_EX +"|",Fore.GREEN+"4- Dar de baja de producto                   ",Fore.LIGHTMAGENTA_EX +"|")
    print(Fore.LIGHTMAGENTA_EX +"|",Fore.GREEN+"5- Buscar articulo por ID                    ",Fore.LIGHTMAGENTA_EX +"|")
    print(Fore.LIGHTMAGENTA_EX +"|",Fore.GREEN+"6- Reporte de Bajo Stock                     ",Fore.LIGHTMAGENTA_EX +"|")
    print(Fore.LIGHTMAGENTA_EX +"|",Fore.GREEN+"7- Vender                                    ",Fore.LIGHTMAGENTA_EX +"|")
    print(Fore.LIGHTMAGENTA_EX +"|",Fore.GREEN+"8- Salir                                     ",Fore.LIGHTMAGENTA_EX +"|")
    print(Fore.LIGHTMAGENTA_EX +"|_______________________________________________|")
         