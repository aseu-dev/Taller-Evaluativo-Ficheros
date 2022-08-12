def math_tempo(hora_inicial: int, minutos_iniciales: int, minutos_a_agregar: int) -> str:
    ''' Funcion para sumar tiempos '''
    
    hora_inicio = hora_inicial
    minuto_inicio = minutos_iniciales
    horas = hora_inicio
    minutos = minuto_inicio
    if (minuto_inicio + minutos_a_agregar) == 60:
        horas += hora_inicio+1
    elif (minuto_inicio + minutos_a_agregar) > 60:
        horas += hora_inicio+1
        minutos += max(minutos_iniciales,minutos_a_agregar) - min(minutos_a_agregar,minutos_iniciales)
    else:
        horas = hora_inicio
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
    
def only_numbers(entrada: list) -> int:
    ''' Recibe una lista y retorna otra lista basada en la inicial pero sin caracteres de tipo String y espacios '''
    
    aux1 = []
    aux2= []
    aux3= []
    for i in entrada:
        try:
            int(i)
        except ValueError:
            pass
        else:
            aux1 += i
    for j in aux1:
        if j != ' ':
            aux2 += [int(j)]
            
    combinacion1, combinacion2 = f'{aux2[0]}{aux2[1]}', f'{aux2[2]}{aux2[3]}'
    numero1 = [int(combinacion1)]
    numero2 = [int(combinacion2)]
    return numero1, numero2

def extraerNumeros(string: str) -> list[int]:
    ''' Recibe un string, y retorna una lista con todos los caracteres  compatibles con el formato integer '''
    
    lista = []
    for i in string:
        lista += i
    return only_numbers(lista)

# def escritor():
#     hora_final = '1400'
#     hora_inicio = int(input('Ingrese la hora de inicio: '))
#     minuto_inicio = int(input('Ingrese el minuto inicial: '))
#     programa_de_inicio = int(input('Ingrese el tiempo del programa de inicio: '))
#     ajustes_iniciales = int(input('Ingrese el tiempo de los ajustes iniciales: '))
#     inicio_produccion = int(input('Ingrese el tiempo del inicio de produccion: '))
#     reponer_materia_prima = int(input('Ingrese el tiempo de la repocicion de materia prima: '))
#     distribucion_productos = int(input('Ingrese el tiempo de la distribucion de productos: '))
#     almacenamiento = int(input('Ingrese el tiempo de almacenamiento: '))
#     time1 = math_tempo(hora_inicio,minuto_inicio,programa_de_inicio)
    
#     time2= math_tempo

print(math_tempo(1,20,20))
