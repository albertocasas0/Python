Es un programa de gestion de articulos, en la base de Datos "Inventario.DB", se creo un inventario de una verduleria.
No se limita a ser solo Frutas y verduras, pero la idea principal si es mantener con solo una categoria y no varias.

En Main.py se  encuentra la estructura inicial del programa donde hace el llamado a las funciones para realizas difentes tareas.
La Primera funciona llama al menu que se muestra en pantalla con las opciones para el usuario:

1- Alta de productos Nuevos
2- Consulta de datos de producto 
3- Modificar      
4- Dar de baja de producto 
5- Buscar articulo por ID 
6- Reporte de Bajo Stock
7- Vender 
8- Salir

1 - Alta de Articulos Nuevos.
1.1 - El usuario tiene la posibilidad de ingresar un articulo nuevo S o N.
        Si es que NO (n), sale al menu de opciones nuevamente. En caso de ser Si (s), le solicitara los datos a ingresar. Tambien valida haber ingresado n, no, s o si.
1.2 - Primero ingresa el nombre del articulo y luego una breve descripcion. El programa hace una busque en la Base de Datos (BD), por nombre y descripcion para verificar NO duplicar el articulo.
1.3 - Luego solicita ingresdar la cantidad. El programa verifica que no ingrese 0 en cantidad. En caso de hacerlo solicitara ingresar un numero de stock valido.
1.4 - Pasando por tercer lugar solicita ingresar el precio del articulo. Tambien valida que el precion NO sea 0, solicitando un valor mayor hasta que lo ingrese.
1.5 - Por ultimo se debe ingresar la categoria del articulo. Acá NO hace validaciones.
1.6 - Finalizando la carga el programa lo almacena y guarda en la BD, e indica que se agrego con exito, Caso contrario informa un "Error".
1.7 - Por ultimo pregunta si quiere agregar otro articulo, comenzando el bucle nuevamente, o si vuelve al menu principal.

2- Consulta de datos de producto
2.1 Seleccionando esta opcion, el sistema arroja todos lo ingresado en la base de datos, includo su ID, el mismo es autoincrementable.
2.2 Una vez mostrado todos los resultados, el programa te pregunta si quieres volver al menu principal o quiere que arroje nuevamente toda la impresion. Tambien vlaida ingresar una opcion valida.

3- Modificar
3.1 - Lo primero que hace esta opcion es ver si de verdad quieres modificar un articulo o volver al menu principal, en caso de haber seleccionado la opcion por error.
3.2 - En caso de querer modificar un articulo, te solicitara su ID. 
3.2.1 - El programara buscara ese ID y mostrara en pantalla si ID, Nombre, descripcion, cantidad, precio y categoria.
3.3 - Te preguntara si quieres cambiar el nombre del articulo.
3.3.1 - Si quieres cambiar el nombre del articulo, el programa te solicitara su nombre nuevo.
3.3.2 - En caso contrario se despliega un menu para saber que es lo que se desea cambiar. (Cantidad, Precio, Ambos o Nada)
3.4 - De pendiendo la opcion seleccionada solicitara el/los dato a modificar.
3.4.1 - Una vez ingresado el/los dato/s nuevo/s. Se graba en la base de datos. Y se va imprimiendo por pantalla la carga exitosa.
3.5 - Habiendo realizado la/s carga/s correpondientes o NO, el sistema te devuelve al menú principal.

4- Dar de baja de producto
4.1 - Se puede dar de baja un aticulo por ID o nombre, a lo que el sistema te solicitara ingresar uno u otro.
4.2 - Si se ingresa un ID (numero), el sistema verifica haber ingresado un numero y lo busca en la base de datos
4.3 - Si ingreso un nombre, el sistema busca en la BD todos los articulos con ese nombre.
4.4 - Se imprime por pantalla todos los resultados obtenidos.
4.5 - Se debe acceder al elemento a eliminar por el numero de orden que se refleja en pantalla.
4.5.1 - Se imprime la opcion selencionada, mostrando el ID, Articulo, observacion, cantidad, precio y categoria.
4.6 - Pregunta si decea eliminarlo de la BD.
4.6.1- En caso de ser afirmativo, se elimina de la BD.
4.6.2 - En caso negativo informa no haber eliminado nada.
4.7 - El sistema simpre valida haber ingresado las opciones correctamente, o si el articulo existe en la base de datos.

5- Buscar articulo por ID
5.1 - El sistema puede buscar un articulo por ID, Nombre o Categoria.
5.2 - Dependiendo lo ingresado, valida si es un numero o una palabra.
5.3 - Busca en la BD el/los articulos que cuentan con lo solicitado por el usuario.
5.4 - Muestra por pantalla el/los ID, Articulo, observacion, cantidad, precio y categoria de lo encontrado.
5.5 - En caso de no haber nada en la based de datos arroja un cartel informando que no se encontraron productos.
5.6 - Pregunta si quiere buscar otro articulo.
6.7 - El sistema valida haber ingresado opcion valida.

6- Reporte de Bajo Stock
6.1 - Solicita un numero de strock minimo a filtrar.
6.2 - El sistema imprime por pantalla la leyenda "Informe de productos con stock bajo (menos de xxx unidades):"
6.2.1 - El programa busca en la base de datos por el criterio Stock < stock_minimo.
6.2.2 - Imprime por pantalla los resultados obtenidos.
6.2.3 - En caso de no haber un stock menor al solicitado. Imprime: "No hay productos con stock bajo (menos de xxx Unidades):"
6.3 - Habiendo mostrado por pantalla el/los resultado/s, vuelve al menu principal.
6.4 (queda pendiente la posibilidad de realizar una exportacion a Excel con el resultado obtenido)

-------------------------------o-------------------------------o-------------------------------o-------------------------------o-------------------------------o-------------------------------o-------------------------------o-------------------------------
Fuera de lo solicitado se realizo la insercion de un nuevo modulo:

7- Vender
7.1 - Se muestra MENU DE VENTAS
7.2 - Consulta que ID o articulo quiere vender
7.2.1 - Verifica haber ungresado un numero (ID) y lo busca.
7.2.2 - Si ingreso un nombre preguntara la descripcion.
7.3 - Busca en la BD la condicion buscada.
7.3.1 - Si esta en la BD te permite seguir preguntandote cuantas uniodades quieres vender.
7.4 - Venta exitosa.
7.4.1 - Muestra por pantalla la El precio final vedido.
7.4.2 - Muestra por pantalla El stock en Kg que queda de ese articulo.
7.5 - Si no hay Stock sufiente informa por pantalla que la venta no se peude realizar.
7.6 - Pregunta si decea vender otro articulo, caos contrario sale al menu principal.
-------------------------------o-------------------------------o-------------------------------o-------------------------------o-------------------------------o-------------------------------o-------------------------------o-------------------------------

8- Salir
8.1 - Finaliza el programa.
