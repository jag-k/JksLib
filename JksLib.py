__author__ = "Jag_k"
from urllib import request, parse
from translateApiKey import apiKey  # https://translate.yandex.ru/developers/keys

# print("Jk's Lib start loading...")


class File:
    def __init__(self, name):
        open(name, 'r+', encoding='utf-8').close()
        self.file_name = name

    def add(self, text):
        file = open(self.file_name, 'a', encoding='utf-8')
        file.write('\n' + str(text))
        file.close()

    def read(self):
        file = open(self.file_name, 'r+', encoding='utf-8')
        text = file.read()
        file.close()
        return [j for j in filter(lambda x: bool(x), [i for i in text.split('\n')])]

    def write(self, text):
        file = open(self.file_name, 'w+', encoding='utf-8')
        file.write(text)
        file.close()


# Translate #


def en(text):
    translate = request.urlopen('https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'.format(
        apiKey,
        parse.quote_plus(str(text)),
        'en'))
    return eval(str(translate.read(), encoding='utf-8'))


def ru(text):
    translate = request.urlopen('https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'.format(
        apiKey,
        parse.quote_plus(str(text)),
        'ru'))
    return eval(str(translate.read(), encoding='utf-8'))


# Selector #


def select(title="", *quest, numb=True, default=True, lang='eng'):
    if quest:
        print(title+':') if title else False
        for i in range(len(quest)):
            print('\t{}{}'.format(str(i+1)+') ' if numb else "", quest[i]+(';' if i != len(quest) else '.')))
        while True:
            t = input('1: ' if len(quest) == 1 else '1-'+str(len(quest))+': ')
            if t.isdigit():
                if 0 < int(t) < len(quest)+1:
                    return quest[int(t)-1]
    else:
        print(title, end=' ')
        if lang.lower() == 'eng' or lang.lower() == 'en':
            answer = '(Y/n)' if default else '(y/N)'
        elif lang.lower() == 'rus' or lang.lower() == 'ru':
            answer = '(Д/н)' if default else '(д/Н)'
        else:
            answer = '(Y/n)' if default else '(y/N)'
        while True:
            t = input(answer+': ')
            if not t:
                return default
            elif t:
                l = t.lower()
                if l == 'y' or l == 'yes' or l == 'д' or l == 'да':
                    return True
                elif l == 'n' or l == 'no' or l == 'н' or l == 'нет':
                    return False


"""
def installer(List, dir='', start=None):
    ls = []
    for i in List: #i = {fileName, code}
        h = open((dir+i['fileName']), 'w+')
        h.write(i['code'])
        h.close()
        ls.append(i['fileName'])
    if start is not None and type(start) == str:
        if start in ls:
            h = open((dir + 'main.py'), 'w+')
            h.write("import "+start.strip('.py'))
            h.close()
            s = open(start, 'w+')
            rs = s.read()
            s.close()
            s = open(start, 'w')
            s.write('''import os
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), {}))

            {}

            #Thanks for using Jk's Lib!'''.format("'"+dir+"main.py'", rs))
            s.close()
            import main
"""

# print("Jk's Lib loaded")
if __name__ == '__main__':
    pass
