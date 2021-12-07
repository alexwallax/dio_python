from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('\n%d/%m/%Y\n'))
    print(data_atual.strftime('%H/%M/%S\n'))
    print(data_atual.strftime('\n%d/%m/%Y %H/%M/%S\n'))    
    print(data_atual.strftime('\n%c\n'))    
    print(data_atual.day)  
    print(data_atual.year)  
    print(data_atual.hour)  
    print(data_atual.minute)  
    print(data_atual.date()) 
    print(data_atual.weekday())   
    tupla = ('seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 11, 25, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    data_string = '01/01/2022'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    print(data_convertida.day)

    nova_data = data_convertida - timedelta(days=364)
    print(nova_data)


def trabalhando_com_date():
    data_atual = date.today() # variavel com a data de hoje

    data_atual_str = data_atual.strftime('%A %B %Y')

    print(type(data_atual))
    print(type(data_atual_str))

    print(data_atual.strftime('%d - %m - %Y'))

    print(data_atual.strftime('%A - %B - %Y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)

    print(type(horario))
    print(horario)
    
    horario_str = horario.strftime('%H:%M:%S')

    print(type(horario_str))
    print(horario_str)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()