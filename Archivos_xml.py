
from xml.dom import minidom

if __name__ == '__main__':
    ruta0='registro.xml'
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