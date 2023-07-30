class PhotoCamera:
    def __init__(self, brand, model, x, y, is_on, memory_capacity, photos=[]):
        self.brand = brand
        self.model = model
        self.resolution = x, y
        self.is_on = is_on
        self.memory_capacity = memory_capacity
        self.photos = photos

    def take_photo(self):
        return f'Сделана фотография с разрешением {self.resolution[0]}x{self.resolution[1]}'

    def get_camera_info(self):
        return f'Марка:[{self.brand}], Модель:[{self.model}], Разрешение:[{self.resolution[0]}x{self.resolution[1]}] '

    def turn_on(self):
        self.is_on = 1
        return 'Фотокамера включена.'

    def turn_off(self):
        self.is_on = 0
        return 'Фотокамера выключена.'

    def is_camera_on(self):
        if self.is_on == 1:
            return True
        else:
            return False

    def store_photo(self, photo):
        if self.memory_capacity > len(str(photo)):
            self.photos.append(photo)
            return True
        else:
            return False

    def view_photos(self):
        self.photos.sort()
        return self.photos

    def clear_memory(self):
        self.photos = []
        return 'Все фотографии успешно удалены!'


camer = PhotoCamera('sony',1,12,5,0,1000,['1.png','2.png'])
camer.store_photo('я_на_море.png')
print(camer.view_photos())