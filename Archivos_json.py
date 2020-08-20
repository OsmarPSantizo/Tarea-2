import json

if __name__ == '__main__':
   
    ruta='registro.json'
    print('-------------Este es el archivo JSON-------------')
    with open(ruta)as contenido:
        grupos = json.load(contenido)
        for grupo in grupos:
            print('Nombre:' , grupo.get('Nombre',''))
            print('Debut:', grupo.get('Debut',''))
            print('Integrantes:' ,grupo.get('Integrantes',''))
            print('Ultimo álbum:',grupo.get('Ultimo album',''))
            print('---------------')