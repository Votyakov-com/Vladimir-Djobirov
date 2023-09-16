import pyttsx3
from psutil import sensors_battery


def checking_the_battery():
    engine = pyttsx3.init()

    engine.setProperty('rate', 120)
    engine.setProperty('volume', 1)

    if sensors_battery()[0] < 20:
        engine.say('Your battery level is below 20 percent, '
                   'it is recommended to charge the device')
        engine.runAndWait()
    else:
        engine.say(f'Your charging level is {sensors_battery()[0]} percent everything is fine!')
        engine.runAndWait()

