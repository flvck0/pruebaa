import json

def agregarcategoria(cat:str):
    with open("biblioteca.json",mode="r")as lecturaJson:
        archivoJson=json.load(lecturaJson)

        categoria_nueva={
              "CategoriaID":len(archivoJson["Categoria"])+1,
              "Nombre":cat
        }
        archivoJson["Categoria"].append(categoria_nueva)
    with open("biblioteca.json",mode="w")as escribirJson:
        json.dump(archivoJson,escribirJson,indent=4)



def editarcategoria(id:int,catt:str):
    with open("biblioteca.json",mode="r")as lecturaJson:
        archivoJson=json.load(lecturaJson)

        contador=1

        for i in archivoJson["Categoria"]:
            if i["CategoriaID"]==id:
                print("encontre la categoria que deseas editar")
                break
            contador+=1
            print(contador)

        archivoJson["Categoria"][contador]["Nombre"]=catt

    with open("biblioteca.json",mode="w")as escribirJson:
            json.dump(archivoJson,escribirJson,indent=4)

def eliminarProducto(idd:int):
    with open("biblioteca.json",mode="r")as lecturaJson:
        archivoJson=json.load(lecturaJson)

        archivoJson["Categoria"]=[categoria for categoria in archivoJson["Categoria"]if categoria["CategoriaID"]!=idd]

    with open("biblioteca.json",mode="w")as escribirJson:
        json.dump(archivoJson,escribirJson,indent=4)

def listarProducto():
    with open("biblioteca.json",mode="r")as lecturaJson:
        archivoJson=json.load(lecturaJson)
        print("CategoriaID         Nombre")
        for i in archivoJson["Categoria"]:
            print(i["CategoriaID"],"             ",i["Nombre"])

listarProducto()