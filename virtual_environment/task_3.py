from pyscreenshot import grab
import time

for frame in range(1, 6):
    screenshot = grab()
    screenshot.save(f"C:\\Users\\Lenovo\\Desktop\\frames\\screenshot_{frame}.png")
    print(f'Скриншот №{frame} успешно сохранен!')
    time.sleep(5)
