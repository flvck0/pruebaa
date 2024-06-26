import os
import comandos
opc1=[
    "[1]-mantenedor de categorias",
    "[2]-reportes",
    "[3]-salir"
]

opc2=[
    "[1]-agregar categoria",
    "[2]-editar categoria",
    "[3]-eliminar categoria",
    "[4]-buscar categoria"
    "[5]-volver"
]
print("""***********************
******mundo libro******
***********************""")                          
while True:
    for i in opc1:
        print(i)
    respuesta1=int(input("ingrese una opcion:"))

    if respuesta1==1:
        print("mantenedor de categorias...")
        while True:
            for i in opc2:
                print(i)
            respuesta2=int(input("ingrese una opcion:"))
            if respuesta2==1:
                print("agregar categoria")
                nombre=input("ingrese la nueva categoria:")
                comandos.agregarcategoria(nombre)
            if respuesta2==2:
                print("editar producto")
                ID=int(input("ingrese el ID de la categoria que desea editar"))
                nom=input("agrega la categoria editada")
                comandos.editarcategoria(ID,nom)
            if respuesta2==3:
                print("eliminar producto")
                Id=int(input("ingrese la categoria de la ID que desea borrar"))
                comandos.eliminarProducto(Id)
            if respuesta2==4:
                print("listar categorias")
                comandos.listarProducto()
            if respuesta2==5:
                break


        
