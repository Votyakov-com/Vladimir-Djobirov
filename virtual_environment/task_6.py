import datetime

from win11toast import toast


def validate_time(alarm_time):  # 15:30
    try:
        if int(alarm_time[:2]) in range(0, 24) and alarm_time[2] == ":" and len(alarm_time[3:]) == 2:
            if int(str(alarm_time[3] + str(alarm_time[4]))) in range(0, 61):
                return "Данные введены корректно!"
            else:
                raise ValueError('Некорректная запись времени, попробуйте еще раз!')
    except TypeError:
        print('Похоже время в некорректном типе данных. Попробуйте использовать "string"!')


def notification(time, title, message, button, audio):
    result_func = validate_time(time)

    if result_func == 'Данные введены корректно!':
        print('Будильник успешно поставлен!')
        while time != str(datetime.datetime.now())[11:16]:
            pass
        else:
            toast(title, message, button=button, audio=audio)
    else:
        raise ValueError('Ошибка валидности данных!')
