
def checking_numbers(day, monht, year):
    result = [True]
    if monht < 1 or monht > 12:
        result.append(False)
    if monht in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            result.append(False)
    if monht in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            result.append(False)  
    if monht == 2:
        if year % 4 == 0:
            if day < 1 or day > 29:
                result.append(False) 
        else: 
            if day < 1 or day > 28:
                result.append(False)
    if False in result:
        return False

def checking_list_date(data):
    list_date = data[0] + data[1] + data[3] + data[4] + data[6] + data[7] + data[8] + data[9] 
    result = True
    for i in range(len(list_date)): 
        if list_date[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            pass
        else:
            result = False
            break
    return result

def getting_data():
    name = input('Введите название историческгого события или имя человека чей возраст хотите узнать: ')
    # name = 'kb'

    while True:
        data7 = list(input('Введите число рождения или начало интересующего временного интервала в формате ДД ММ ГГГГ:  '))
        if len(data7) < 10 or len(data7) > 10:
            print ("### ВЫ НЕ ПРАВИЛЬНО УКАЗАЛИ ДАТУ ПОВТОРИТЕ ВВОД! a ###")
        elif checking_list_date(data7) == False:    
            print ("### ВЫ НЕ ПРАВИЛЬНО УКАЗАЛИ ДАТУ ПОВТОРИТЕ ВВОД! s ###")
        else:
            date1 = int(data7[0] + data7[1])
            date2 = int(data7[3] + data7[4])
            date3 = int(data7[6] + data7[7] + data7[8] + data7[9])
            if checking_numbers(date1, date2, date3) == False:
                print ("### ВЫ НЕ ПРАВИЛЬНО УКАЗАЛИ ДАТУ ПОВТОРИТЕ ВВОД! d ###")
            else:
                break
    
    while True:
        data8 = list(input('Введите сегодняшнее число для того что бы узнать возраст или дату окончания исторического события в формате ДД ММ ГГГГ:  '))
        if len(data8) < 10 or len(data8) > 10:
            print ("### ВЫ НЕ ПРАВИЛЬНО УКАЗАЛИ ДАТУ ПОВТОРИТЕ ВВОД! a ###")
        elif checking_list_date(data8) == False:    
            print ("### ВЫ НЕ ПРАВИЛЬНО УКАЗАЛИ ДАТУ ПОВТОРИТЕ ВВОД! s ###")
        else:
            date4 = int(data8[0] + data8[1])
            date5 = int(data8[3] + data8[4])
            date6 = int(data8[6] + data8[7] + data8[8] + data8[9])
            if checking_numbers(date4, date5, date6) == False:
                print ("### ВЫ НЕ ПРАВИЛЬНО УКАЗАЛИ ДАТУ ПОВТОРИТЕ ВВОД! d ###")
            else:
                break

    data = [date1, date2, date3, date4, date5, date6, name]
    print(data)
    return data

def scripture_regle(day, month, yer):   
    result = ['дней', 'месяцев', 'лет']
    day_r = ['день', 'месяц', 'год']
    day_у = ['дня', 'месяца', 'года']


    text_day = str(day)
    if len(text_day) == 1:
        if day == 1:
            result[0] = day_r[0]
        elif day in [2, 3, 4]:  
            result[0] = day_у[0]
        else:
            pass
    else: 
        if text_day[-2] == '1':
            pass
        else:
            if text_day[-1] == '1':
                result[0] = day_r[0]
            elif text_day[-1] in ['2', '3', '4']:  
                result[0] = day_у[0]

    # if day in [1, 21, 31]:
    #     result[0] = day_r[0]
    # elif day in (2, 3, 4, 22, 23, 24):  
    #     result[0] = day_у[0] 

    if month == 1:
        result[1] = day_r[1]
    elif month in [2, 3, 4]:  
        result[1] = day_у[1]

    text_yer = str(yer)
    if len(text_yer) == 1:
        if yer == 1:
            result[2] = day_r[2]
        elif yer in [2, 3, 4]:  
            result[2] = day_у[2]
    elif len(text_yer) > 1:
        if text_yer[-2] == '1':
            pass
        else:
            if text_yer[-1] == '1':
                result[2] = day_r[2]
            elif text_yer[-1] in ['2', '3', '4']:  
                result[2] = day_у[2]
    return result

def count_month(month_data, data):
    result = 0
    if month_data == 1:
        result += 31
    if month_data == 2:
        result += 59  
    if month_data == 3:
        result += 90 
    if month_data == 4:
        result += 120 
    if month_data == 5:
        result += 151 
    if month_data == 6:
        result += 181 
    if month_data == 7:
        result += 212 
    if month_data == 8:
        result += 243 
    if month_data == 9:
        result += 273 
    if month_data == 10:
        result += 304 
    if month_data == 11:
        result += 334
    if  data % 4 and month_data > 1:
        result += 1
    return result

    ...

def year_difference(res):
    result = res * 365
    for i in range(res):
        if i % 4 == 0:
            result += 1
    return result

def counting_days(data_now, data): 
    month_data = data[1] - 1
    month_data = count_month(month_data, data[2])
    month_data_now = data_now[1] - 1
    month_data_now = count_month(month_data_now, data_now[2])
    year_data = year_difference(data[2])
    year_data_now = year_difference(data_now[2])


    count_data = data[0] + month_data + year_data
    count_data_now = data_now[0] + month_data_now + year_data_now
    
    result = count_data_now - count_data
    return result 

def data_processing():
    text = getting_data()
    data_now = text[3:6] 
    data = text[:3] 
    name = text[-1]
    yer = 0
    day = 0
    month = 0

    if data[2] > data_now[2]:
        print("Событие состоиться в будущем")
        yer += data[2] - data_now[2]
    else:
        yer += data_now[2] - data[2]

    if data[1] > data_now[1]:
        yer -= 1
        month += 12 - data[1] + data_now[1]
    elif data[1] == data_now[1]:
        month = 0
    else:
        month += data_now[1] - data[1]




    if data[0] > data_now[0]:
        if data[1] in [1, 3, 5, 7, 8, 10, 12]:
            day += 31 - data[0] + data_now[0]
        elif data[1] in [4, 6, 9, 11]:
            day += 30 - data[0] + data_now[0]
        elif data[1] == 2:
            if data[2] % 4 == 0:
                day += 29 - data[0] + data_now[0]
            else:
                day += 28 - data[0] + data_now[0]
        month -= 1
        if month < 0:
            month = 11
            yer -= 1
    elif data[0] == data_now[0]:
        day = 0
    else:
        day += data_now[0] - data[0]
    
    scripture =  scripture_regle(day, month, yer)
    counting_d = counting_days(data_now, data)
    scripture_counting_d = scripture_regle(counting_d, month, yer)

    answer = (f"""###    ОТЧЕТ    ###

Возраст человека или длительность исторического события "{name}" 
на запрашиваемую дату {data_now[0]}:{data_now[1]}:{data_now[2]} составляет: {day} {scripture[0]}, {month} {scripture[1]}, {yer} {scripture[2]}.
Или {counting_d} {scripture_counting_d[0]}
""")

    print(answer)

def start_of_the_program():
    cicle = True
    print('''

    ###Программа рассчета временного интервала###

Позволяет определить количество времени прошедшего с начала какого-либо события до его конца. Например: сколько длилась Курская битва. 

От Вас потребуется:
1. ввести имя человека чей возраст Вы хоте ли узнать или название исторического события (например: Курская битва).
2. ввести число, месяц, год начала исторического события или дату своего рождения (например: 05 07 1943).
3. ввести число, месяц, год окончания исторического события или сегодняшнюю дату что бы узнать свой возраст на сегодня 
(например: 23 08 1943).
И программа рассчитает количество дней, месяцев и лет временного интервала''')
    user_response = input("""
Если вы готовы нажмите ввод, 
или введите любой символ, что бы покинуть программу: """)
    if user_response == '':
        data_processing()
    else:
        print("""
        ###############
        Всего хорошего!
        ###############
        """)
        cicle = False

    while  cicle == True:
        user_response = input("""
Для продолжения нажмите ввод, 
или введите любой символ, что бы покинуть программу: """)
        if user_response == '':
            data_processing()
        else:
            print("""
            ###############
            Всего хорошего!
            ###############
            """)
            break

start_of_the_program()
