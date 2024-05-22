def triangle ():
    while True:
        try:
            number = int(input('enter number'))
            flag = 1
            break
        except Exception:
            print('incorrect input')
    string_lenght=1
    for g in range(int(number)-1):
        string_lenght += 2
    plate = string_lenght//2

    for i in range(int(number)):
        print(' '*(plate-i),'*'*(1+i*2))

def translate() :
    from num2words import num2words
    from translate import Translator
    while True:
        try:
            number = int(input('enter number'))
            break
        except Exception:
            print('incorrect input')

    translator = Translator(from_lang='en',to_lang="ru")
    number = num2words(number)
    print(translator.translate(number))

translate()


def sum_sum() :
    while True:
        try:
            number = int(input('enter number'))
            break
        except Exception:
            print('incorrect input')

    while number > 9:
        number = sum([int(i) for i in str(number)])
    print(number)
