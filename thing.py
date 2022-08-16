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
        minutos_restantes = minutos_a_agregar + minutos_iniciales
        while True:
            if minutos_iniciales + minutos_restantes >= 60:
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

def rest_tempo(hora_inicial: str, hora_final: str) -> int:
    """ Funcion que solicita dos entradas de tipo texto, con formato hora y devuelve la diferencia entre ellas, por ejemplo:
        "02\t:\t30" - "01\t:\t30"  ->  "60" """

    hora01, minuto01 = extraccion(hora_inicial)
    hora02, minuto02 = extraccion(hora_final)
    minutos_hora_inicial = minuto01
    minutos_hora_final = minuto02
    for _ in range(hora01):
        minutos_hora_inicial += 60
    for _ in range(hora02):
        minutos_hora_final += 60
    diferencia = max(minutos_hora_final,minutos_hora_inicial) - min(minutos_hora_inicial, minutos_hora_final)
    return diferencia

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

def mayor_diferencia(n1: str, n2: str, n3: str, n4: str, n5: str, n6: str) -> str:
    """ Recibe una secuencia de 6 cadenas de texto en formato hora militar y devuelve la hora a
        la que se finalizo el lapzo de tiempo mas largo  """
    diferencia1 = rest_tempo(n1,n2)
    diferencia2 = rest_tempo(n2,n3)
    diferencia3 = rest_tempo(n3,n4)
    diferencia4 = rest_tempo(n4,n5)
    diferencia5 = rest_tempo(n5,n6)
    mayor_diferencia_ = max(diferencia1,diferencia2,diferencia2,diferencia3,diferencia4,diferencia5)
    if mayor_diferencia_ == diferencia1:
        return n2
    elif mayor_diferencia_ == diferencia2:
        return n3
    elif mayor_diferencia_ == diferencia3:
        return n4
    elif mayor_diferencia_ == diferencia4:
        return n5
    else:
        return n6
    

def escritor(nombre_archivo: str, lista: list) -> None:
    """ Funcion que se encarga de escribir elementos de una lista dentro de un archivo de formato .txt """

    with open(f'./{nombre_archivo}.txt', 'w') as file:
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

mayor_diferencia_tempo = mayor_diferencia(tempo1,tempo2,tempo3,tempo4,tempo5,tempo6)
if rest_tempo(hora_final,tempo6) > 0:
    sobretiempo = rest_tempo(hora_final,tempo6)

tempos = [
    (f'Programa de inicio	 	         {tempo1}'),
    (f'Ajustes iniciales	 	         {tempo2}'),
    (f'Inicio de produccion             {tempo3}'),
    (f'Reponer Materia Prima            {tempo4}'),
    (f'Distribucion de productos        {tempo5}'),
    (f'Almacenamiento                   {tempo6}'),
    (f'Hora final con mayor tiempo      {mayor_diferencia_tempo}'),
    (f'Sobretiempo                      {sobretiempo} minutos')
]
escritor('resultados', tempos)
