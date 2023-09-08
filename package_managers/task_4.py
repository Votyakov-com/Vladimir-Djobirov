import colorama

text = 'text_1'

print(colorama.Fore.RED + text, colorama.Style.RESET_ALL)
print(colorama.Back.RED + text, colorama.Style.RESET_ALL)
print(text)
print(colorama.Back.RED + (colorama.Fore.BLACK + text))
