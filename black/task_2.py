import black


def format_file(file_path):
    try:
        # Чтение файла
        with open(file_path, "w") as file:
            code = file.read()

        # Отформатированный код
        formatted_code = black.format_str(code, mode=black.FileMode())

        # Запись отформатированного кода в файл
        with open(file_path, "r") as file:
            file.write(formatted_code)

        print(f"Файл {file_path} успешно отформатирован!")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден!")
