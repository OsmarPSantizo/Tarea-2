import json
from xml.dom import minidom
import os
import csv

def cargar_datosjson(ruta):
    print('-------------Este es el archivo JSON-------------')
    with open(ruta)as contenido:
        grupos = json.load(contenido)
        for grupo in grupos:
            print('Nombre:' , grupo.get('Nombre',''))
            print('Debut:', grupo.get('Debut',''))
            print('Integrantes:' ,grupo.get('Integrantes',''))
            print('Ultimo álbum:',grupo.get('Ultimo album',''))
            print('---------------')


def cargar_datosxml(ruta0):
    print('-------------Este es el archivo XML-------------')
    docXml = minidom.parse(ruta0)
    fandoms = docXml.getElementsByTagName("Fandom")
    
    for fandom in fandoms:
        sid = fandom.getAttribute("ID")
        nombre = fandom.getElementsByTagName("Nombre")[0] 
        grupo = fandom.getElementsByTagName("Grupo")[0] 
        lema = fandom.getElementsByTagName("Lema")[0] 
        color = fandom.getElementsByTagName("Color")[0] 

        print("id:%s" %sid)
        print("Nombre:%s" %nombre.firstChild.data)
        print("Grupo:%s" %grupo.firstChild.data)
        print("Lema:%s" %lema.firstChild.data)
        print("Color:%s" %color.firstChild.data)
        print('---------------')

def cargar_datos(ruta1):
    print('-------------Este es el archivo CSV-------------')
    with open(ruta1) as f:
        reader = csv.reader(f)
        encabezado = next(reader)
        print(encabezado)
        
        for registro in reader:
            print(registro)
    




if __name__ == '__main__':
   
    ruta='registro.json'
    cargar_datosjson(ruta)  
    ruta0='registro.xml'
    cargar_datosxml(ruta0)
    ruta1='registro.csv'
    cargar_datos(ruta1)

    


