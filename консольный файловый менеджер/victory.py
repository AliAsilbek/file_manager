def victory():
    import random
    push = True
    dos = True
    Maiak = True
    Ein = True
    Mar = True
    Step = True
    Mark = True
    ggg = True
    konaev = True
    ali = True
    while True:
        start = input('Start the game? Yes/no: ')
        if 'yes' in start:
            question = {}
            score = 0
            people = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            questions = random.sample(people, 5)
            for i in questions:
                if i == 1:
                    answer = input('When was Pushkin born: ')
                    if answer == '26.05.1766':
                        score = score + 1
                    else:
                        push = False
                elif i == 2:
                    answer = input('When was Dostoevsky born: ')
                    if answer == '11.11.1821':
                        score = score + 1
                    else:
                        dos = False
                elif i == 3:
                    answer = input('When was Maiakovski born: ')
                    if answer == '19.07.1893':
                        score = score + 1
                    else:
                        Maiak = False
                elif i == 4:
                    answer = input('When was Einstein born: ')
                    if answer == '14.03.1879':
                        score = score + 1
                    else:
                        Ein = False
                elif i == 5:
                    answer = input('When was Marilyn Monroe born: ')
                    if answer == '01.06.1926':
                        score = score + 1
                    else:
                        Mar = False
                elif i == 6:
                    answer = input('When was Stephen William Hawking born: ')
                    if answer == '14.05.1984':
                        score = score + 1
                    else:
                        Step = False
                elif i == 7:
                    answer = input('When was Mark Elliot Zuckerberg born: ')
                    if answer == '08.01.1942':
                        score = score + 1
                    else:
                        mark = False
                elif i == 8:
                    answer = input('When was Gitler born: ')
                    if answer == '20.04.1889':
                        score = score + 1
                    else:
                        ggg = False
                elif i == 9:
                    answer = input('When was D.Konaev born: ')
                    if answer == '12.01.1912':
                        score = score + 1
                    else:
                        konaev = False
                elif i == 10:
                    answer = input('When was Alikhan Bokeihanov born: ')
                    if answer == '05.03.1866':
                        score = score + 1
                    else:
                        ali = False
            print("You gained", score, "points")
            print("You lost", 5 - score, "points")
            if push is False:
                print('Pushlin was born 26.05.1766')
            if dos is False:
                print('Dostoevsky was born 11.11.1821')
            if Ein is False:
                print('Einstein was born 14.03.1879')
            if Mar is False:
                print('Marilyn Monroe was born 01.06.1926')
            if Step is False:
                print('Stephen William Hawking was born 14.05.1984')
            if Mark is False:
                print('Mark Elliot Zuckerberg was born 14.05.1984')
            if ggg is False:
                print('Gitler was born 20.04.1889')
            if konaev is False:
                print('D.Konaev was born 12.01.1912')
            if ali is False:
                print('Alikhan Bokeihanov  was born 05.03.1866')
            if Maiak is False:
                print('Maialovski was born 19.07.1893')
        else:
            break