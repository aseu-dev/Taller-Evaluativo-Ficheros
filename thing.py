def convertir_formato(horas: int, minutos:int) -> str:
    """ Agrega los ceros necesarios para simular un formato 24 horas, por ejemplo:
        "1\t:\t02" -> "01\t:\t02" """
    if horas < 10 or minutos < 10: 
        if minutos < 10 and horas < 10:
            return f'0{horas}\t:\t0{minutos}'
        elif minutos < 10:
            return f'{horas}\t:\t0{minutos}'
        elif horas < 10:
            return f'0{horas}\t:\t{minutos}'
    else:
        return f'{horas}\t:\t{minutos}'

def sum_tempo(hora_inicial: int, minutos_iniciales: int, minutos_a_agregar: int) -> str:
    ''' Funcion para sumar minutos a una hora inicial: 
        6\t:\t45 + 20 -> 7\t:\t15 '''
    
    horas = hora_inicial
    minutos = minutos_iniciales
    if (minutos_iniciales + minutos_a_agregar) == 60:
        horas += 1
        minutos = 0
    elif (minutos_iniciales + minutos_a_agregar) > 60:
        horas_acumuladas = 0
        minutos_restantes = minutos_a_agregar
        count = 1
        while True:
            if minutos_iniciales + minutos_restantes >= 60:
                if count == 1:
                    minutos_restantes = minutos_a_agregar + minutos_iniciales
                    count -= 1
                minutos_restantes -= 60
                horas_acumuladas += 1
                if minutos_restantes < 60:
                    minutos = minutos_restantes
                    horas += horas_acumuladas
                    break
            else:
                minutos = minutos_restantes
                horas += horas_acumuladas
                break
    else:
        horas = hora_inicial
        minutos += minutos_a_agregar
    return convertir_formato(horas, minutos)

def rest_tempo(hora_inicial: str, hora_final: str) -> str:
    """ Funcion que solicita dos entradas de tipo texto, con formato hora y devuelve la diferencia entre ellas, por ejemplo:
        "02\t:\t30" - "01\t:\t25"  -> "1\t:\t05" """
    hora1, minuto1 = extraccion(hora_inicial)
    hora2, minuto2 = extraccion(hora_final)

    pass
def only_numbers(entrada: list) -> int:
    ''' Recibe una lista con cuatro numeros y devuelve dos numeros compuestos por pares de la lista: 
        [1, 2, 3, 4] -> 12, 34 '''
    
    aux = []
    for i in entrada:
        try:
            int(i)
        except ValueError:
            pass
        else:
            aux += [int(i)]
    combinacion1, combinacion2 = int(f'{aux[0]}{aux[1]}'), int(f'{aux[2]}{aux[3]}')
    return combinacion1, combinacion2

def extraer_numeros(string: str) -> list[int]:
    ''' Recibe un string, y retorna una lista con todos los caracteres  compatibles con el formato integer, por ejemplo:
        "s1j2,3k4:5" -> [1, 2, 3, 4, 5]'''
    
    lista = []
    for i in string:
        lista += i
    return only_numbers(lista)

def extraccion(tempo: str) -> int:
    """ Toma una cadena de texto de formato hora y devuelve dos variables equivalentes a los numeros de la cadena: 
        "01\t:\t12" -> num1 = 1, num2 = 12"""

    num1, num2 = extraer_numeros(tempo)
    return num1, num2

def escritor(nombre_archivo: str, lista: list) -> None:
    """ Funcion que se encarga de escribir elementos de una lista dentro de un archivo de formato .txt """

    with open(f'./{nombre_archivo}', 'w') as file:
        for tempo in lista:
            file.write(f'{tempo}\n')

hora_final = '14:00'
hora_inicio = int(input('Ingrese la hora inicial: ')) # 6
minuto_inicio = int(input('Ingrese el minuto inicial: ')) # 45
programa_de_inicio = int(input('Ingrese el tiempo del programa de inicio: ')) # 20
ajustes_iniciales = int(input('Ingrese el tiempo de los ajustes iniciales: ')) # 10
inicio_produccion = int(input('Ingrese el tiempo del inicio de produccion: ')) # 190
reponer_materia_prima = int(input('Ingrese el tiempo de la repocicion de materia prima: ')) # 70
distribucion_productos = int(input('Ingrese el tiempo de la distribucion de productos: ')) # 55
almacenamiento = int(input('Ingrese el tiempo de almacenamiento: ')) # 105

tempo1 = sum_tempo(hora_inicio,minuto_inicio,programa_de_inicio)
hora1, minuto1 = extraccion(tempo1)
tempo2 = sum_tempo(hora1,minuto1,ajustes_iniciales)
hora2, minuto2 = extraccion(tempo2)
tempo3 = sum_tempo(hora2, minuto2, inicio_produccion)
hora3, minuto3 = extraccion(tempo3)
tempo4 = sum_tempo(hora3, minuto3, reponer_materia_prima)
hora4, minuto4 = extraccion(tempo4)
tempo5 = sum_tempo(hora4, minuto4, distribucion_productos)
hora5, minuto5 = extraccion(tempo5)
tempo6 = sum_tempo(hora5, minuto5, almacenamiento)

tempos = [
    
    (f'Programa de inicio\t \t{tempo1}'),
    (f'Ajustes iniciales\t \t{tempo2}'),
    (f'Inicio de produccion\t \t{tempo3}'),
    (f'Reponer Materia Prima\t \t{tempo4}'),
    (f'Distribucion de productos\t \t{tempo5}'),
    (f'Almacenamiento\t \t{tempo6}'),
    (),
    ()
]
escritor('resultados', tempos)
