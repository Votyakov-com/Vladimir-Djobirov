from re import findall

text = "ул. Кутузовская, дом № 13, корпус 3, квартира 98"

print(findall('\d+', text))
# Answer: ['13', '3', '98']
