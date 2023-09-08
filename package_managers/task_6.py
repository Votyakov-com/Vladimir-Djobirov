import time

import pyperclip


def clipboard(text):
    try:
        new_text = text.lstrip().rstrip().lower()
        new_text = new_text.replace('ё', 'е')
        while True:
            time.sleep(1)
            pyperclip.copy(new_text)
            print('Текст успешно скопирован!')
    except KeyboardInterrupt:
        print('Пользователь остановил программу!')
