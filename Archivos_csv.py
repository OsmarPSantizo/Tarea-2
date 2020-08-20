import csv

if __name__ == '__main__':

    ruta1='registro.csv'
    print('-------------Este es el archivo CSV-------------')
    with open(ruta1) as f:
        reader = csv.reader(f)
        encabezado = next(reader)
        print(encabezado)
        
        for registro in reader:
            print(registro)

