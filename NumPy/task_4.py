def mostly(array):
    array = list(map(str, array))
    dictionary = dict()
    for i in array:
        dictionary[i] = array.count(i)
    answers = []
    for i in dictionary:
        answers.append(dictionary[str(i)])

    for i in dictionary:
        if dictionary[str(i)] == max(answers):
            return str(i)
