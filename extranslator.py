from cgitb import text
from translate import Translator
translator=Translator(to_lang='fr')
try:
    with open('./test.txt',mode='r') as my_file:
        text=my_file.read()
        translation=translator.translate(text)
        with open('./testtranslated.txt',mode='w') as my_file2:
            my_file2.write(translation)
        print(translation)
except FileNotFoundError as e:
    print('Check your file path silly')