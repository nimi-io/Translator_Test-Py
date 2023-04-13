from translate import Translator

"""

 Available languages:

       https://en.wikipedia.org/wiki/ISO_639-1
       Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)


"""
translator = Translator(to_lang="zh")

try:
    with open('./test.txt', mode='r') as my_file, open('./test-ja.txt', mode='w') as my_file2:
        # print(my_file .read())
        for line in my_file:
            translation = translator.translate(line)
            print(translation)
            my_file2.write(translation + '\n')

except FileNotFoundError as err:
    print("Check your file Silly!")
