def sum_tempo(hora_inicial: int, minutos_iniciales: int, minutos_a_agregar: int) -> str:
    ''' Funcion para sumar minutos a una hora inicial: 6\t:\t45 + 20 -> 7\t:\t15 '''
    
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
    if horas < 10 or minutos < 10: 
        if minutos < 10 and horas < 10:
            return f'0{horas}\t:\t0{minutos}'
        elif minutos < 10:
            return f'{horas}\t:\t0{minutos}'
        elif horas < 10:
            return f'0{horas}\t:\t{minutos}'
    else:
        return f'{horas}\t:\t{minutos}'

def rest_tempo(hora_inicial: int, minuto_inicial: int, hora_final: int, minuto_final: int) -> str:
    
    pass
def only_numbers(entrada: list) -> int:
    ''' Recibe una lista con cuatro numeros y devuelve dos numeros compuestos por pares de la lista: [1, 2, 3, 4] -> 12, 34 '''
    
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

def extraerNumeros(string: str) -> list[int]:
    ''' Recibe un string, y retorna una lista con todos los caracteres  compatibles con el formato integer '''
    
    lista = []
    for i in string:
        lista += i
    return only_numbers(lista)

def TODO(tempo: str) -> int:
    
    num1, num2 = extraerNumeros(tempo)
    return num1, num2

def escritor():
    
    
    hora_final = ['14:00']
    hora_inicio = int(input('Ingrese la hora de inicio: ')) # 6
    minuto_inicio = int(input('Ingrese el minuto inicial: ')) # 45
    programa_de_inicio = int(input('Ingrese el tiempo del programa de inicio: ')) # 20
    ajustes_iniciales = int(input('Ingrese el tiempo de los ajustes iniciales: ')) # 10
    inicio_produccion = int(input('Ingrese el tiempo del inicio de produccion: ')) # 190
    reponer_materia_prima = int(input('Ingrese el tiempo de la repocicion de materia prima: ')) # 70
    distribucion_productos = int(input('Ingrese el tiempo de la distribucion de productos: ')) # 55
    almacenamiento = int(input('Ingrese el tiempo de almacenamiento: ')) # 105

    tempo1 = sum_tempo(hora_inicio,minuto_inicio,programa_de_inicio)
    print(tempo1)
    hora1, minuto1 = TODO(tempo1)
    tempo2 = sum_tempo(hora1,minuto1,ajustes_iniciales)
    print(tempo2)
    hora2, minuto2 = TODO(tempo2)
    tempo3 = sum_tempo(hora2, minuto2, inicio_produccion)
    print(tempo3)
    hora3, minuto3 = TODO(tempo3)
    tempo4 = sum_tempo(hora3, minuto3, reponer_materia_prima)
    print(tempo4)
    hora4, minuto4 = TODO(tempo4)
    tempo5 = sum_tempo(hora4, minuto4, distribucion_productos)
    print(tempo5)
    hora5, minuto5 = TODO(tempo5)
    tempo6 = sum_tempo(hora5, minuto5, almacenamiento)
    print(tempo6)

escritor()
