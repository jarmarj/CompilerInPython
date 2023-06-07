#####################################################################
#####################################################################
##								  ###
##								  ###
##								  ###
##		DOCUMENTACION | DISEÑO DE COMPILADORES		  ###
##								  ###
##								  ###
##								  ###
#####################################################################
#####################################################################


-----------------DOCUMENTOS QUE COMPONEN EL PROGRAMA-----------------

Se requieren 5 documentos para ejecutar el programa correctamente:

1.sourceCode1.txt
El codigo fuente (el cual dentro del programa lo detecta como
'sourceCode1.txt' pero es editable dentro del mismo codigo.

2.lexico.py
El modulo lexico.py es donde se lleva el proceso de analisis de lexico
separando por tokens el codigo fuente. Para ver mas detalle se puede
ver el documento llamado KeywordsSymbols.txt donde se enlistan
los mismos.


3.mainLEXICO.py
Este no es mas que el metodo main donde se puede probar lo que se 
realiza directamente en el modulo lexico.py


4.sintax.py
el modulo sintax.py donde se analisa la tabla para revisar cada proceso
y poder sustituir las producciones por lo que corresponida en cada una.
Esto partiendo de la lista de tokens que obtubimos desde el analisis
de lexico.

5.sintaxClass.py
Es el main general de todo el programa. Aqui se manda a llamar
el metodo principal del lexico y se ejecuta el metodo parse() de 
la clase de lexico, que es donde se realiza la busqueda de producciones
y sustitucion de las mismas.

---------------------METODO DE IMPLEMENTACION------------------------

Para poder ejcutar el programa se requiere de tener una gramatica
inicial de la cual ya se deben haber obtenido los First y Follow.
Para entonces tener correcta la tabla de sintaxis, o parse table,
que es la que dictamina que produccion tiene que sustitucinoes.

La clase de Sintax necesita de 6 parametros para construirla y
funcionar correctamente:

1.Producciones: este sera un diccionario donde el lado izquierdo
de la produccion solo tendra un numero entero como llave. Estas
llaves incrementan de uno en uno segun la produccion. Los valores 
de cada producciones estan almacenados en una lista, cada elemento
de la lista es cada elemento terminal y no terminal de cada prod.

2.TERMINALES: todos los terminales que tenemos en nuestra gramatica,
los cuales deben estar ordenados segun aparezcan en nuestra parse table.

3.NO-TERMINALES: todos los no-terminales que tenemos en nuestra gramatica,
los cuales deben estar ordenados segun aparezcan en nuestra parse table.

4.PARSE-TABLE: la parse table unicamente tendra los datos de produccion
como un string de numeros enteros o string vacio. Numeros enteros
porque es la llave del diccionario donde tenemos almacenadas las
producciones.

-------------------------EJECUCION---------------------------------

Para ejecutar el programa una vez que se tengan los requisitos,
simplemente se manda a llamar el metodo parse() de la clase 
Sintax. Este metodo realizara el proceso de aceptar o no, la lista
de tokens obtenida del lexico, el cual, leyo primero el codigo fuente
'sourceCode1.txt.'
