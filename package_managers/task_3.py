from pytube import YouTube


def download_video(url):
    try:
        print('Видео загружается, подождите немного...')
        try:
            video = YouTube(str(url)).streams.first().download()
        except KeyboardInterrupt:
            print('Вы отменили загрузку!')
        print(f'Видео: {video} успешно загружено!')
    except Exception as error:
        print(f'Ошибка: {error}')

