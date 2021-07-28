f = open("/home/davo/random_text.txt", "r+")
data = f.read()


def letter_counter(text):
    letter_count = 0
    for i in data:
        letter_count += 1
    return letter_count


def word_counter(text):
    global data
    word_count = 0
    data = data.split()
    for i in data:
        word_count += 1
    return word_count


def sorting(text):
    global data
    data = data.split()
    for i in range(len(data) - 1, 0, -1):
        for y in range(i):
            if len(data[y]) > len(data[y + 1]):
                data[y], data[y + 1] = data[y + 1], data[y]
    return data


def symbol_counter(text):
    global data
    dict = {}
    for i in data:
        dict[i] = dict.get(i, 0) + 1
        return dict


def input_counter():
    word = input("Enter a word")
    input_count = 0
    value_list = []
    dict = {}
    for i in data:
        dict[i] = dict.get(i, 0) + 1
    for key, value in dict.items():
        if key in word:
            value_list.append(value)
    value_list.sort()
    min_letter = value_list[0]
    while min_letter != 0:
        input_count += 1
        min_letter -= 1
    return input_count

print(input_counter())
