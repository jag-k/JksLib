__author__ = "Jag_k"

print("Jk's Lib start loading...")

class File:
    def __init__(self, name):
        open(name, 'w+', encoding='utf-8').close()
        self.file_name = name
    def add(self, text):
        file = open(self.file_name, 'wa', encoding='utf-8')
        file.write('\n'+str(text))
        file.close()
    def get(self):
        file = open(self.file_name, 'r+', encoding='utf-8')
        text = file.read()
        file.close()
        return [j for j in filter(lambda x: bool(x), [i for i in text.split('\n')])]

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

print("Jk's Lib loaded")