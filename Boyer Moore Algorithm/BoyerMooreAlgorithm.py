# worst O(N*M)
# best O(N/M)

def BoyerMooreAlgorithm(text='big metadata', pattern='data'):

    # 1. Формування таблиці зміщення
    unique_symbols = set()   # унікальні символи в образі - S
    len_pattern = len(pattern)  # число символів в образі - M
    adjacency_list = {}   # словник суміжності - d

    for i in range(len_pattern - 2, -1, -1):  # ітерація з передостайнього символа
        if pattern[i] not in unique_symbols:    # якщо символ ще не доданий в таблицю
            adjacency_list[pattern[i]] = len_pattern - i - 1    # додаємо символ як ключ = зміщення символа
            unique_symbols.add(pattern[i])

    if pattern[len_pattern - 1] not in unique_symbols:  # окремо формуємо остайній символ
        adjacency_list[pattern[len_pattern - 1]] = len_pattern

    adjacency_list['*'] = len_pattern
    print(adjacency_list)


    # 2. Пошук образа в стрічці
    text_len = len(text)
    if text_len < len_pattern:
        raise ValueError('Wrong data: pattern not found!')

    i = len_pattern-1   # лічильник в тексті - символ який ми порівнюємо
    # лічильник образа j - символ який ми порівнюємо
    while i < text_len:
        k = 0      # для порівняння некст симполів в тексті
        fl_break = False
        # пробігаємо від ласт символа в образі до 1-го
        # лічильник образа j - символ який ми порівнюємо
        for j in range(len_pattern-1, -1, -1):
            # попарно з кінця порівнюємо ласт символ

            if text[i - k] != pattern[j]:
                # якщо символ не співпав (ласт)
                if j == len_pattern-1:
                    off = adjacency_list[text[i]] if adjacency_list.get(text[i], False) else adjacency_list['*']
                    # зміщення, якщо не однаковий  ласт символ образа
                else:
                    off = adjacency_list[pattern[j]]   # смещение, если не равен не последний символ образа

                i += off    # смещение счетчика строки
                fl_break = True  # если несовпадение символа, то fl_break = True
                break

            k += 1          # смещение для сравниваемого символа в строке

        if not fl_break:          # если дошли до начала образа, значит, все его символы совпали
            print(f"Found pattern: index = {i-k+1}")
            break
    else:
        print("Pattern not found")


if __name__ == '__main__':
    BoyerMooreAlgorithm('big metadata', 'data')