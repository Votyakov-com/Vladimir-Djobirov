from PIL import Image


class Picture:
    def __init__(self, mode, size, color, image_name):
        self.mode = mode
        self.size = size
        self.color = color
        self.image_name = image_name

    def load_image(self):
        try:
            picture = Image.new(self.mode, self.size, self.color)
            picture.save(self.image_name)
            print(f'Изображение {picture} успешно загружено и сохранено!')
        except ValueError:
            print('Возможно вы забыли ввести формат изображения (png, jpg и т.д.)')

    def change_image(self, size):
        picture = Image.new(self.mode, size, self.color)
        picture.save(self.image_name)
        print(f'Изображение {picture} успешно изменено!')
