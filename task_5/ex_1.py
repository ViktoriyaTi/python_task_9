# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = input('Введите текст: ')
text = text.lower().split()
st = 'абв'
text_rez = [i for i in text if st not in i]
text_rez = ' '.join(text_rez)
print(text_rez)

