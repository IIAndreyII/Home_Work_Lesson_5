#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from encodings import utf_8

with open("Text_1.txt", encoding='utf_8') as f:
    for line in f:
        text = line.split()
        for text_1 in text:
            if 'абв' in text_1:
                text.remove(text_1)
        res = " ".join(text)
        print(res)

