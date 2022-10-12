# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример: Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('file_task_5_import.txt','r', encoding='utf-8') as text:
    text = list(text.readline()) 
    count = 1
    result_text = ''
    for i in range(len(text)-1):
            if text[i] == text[i+1]:
                count+=1
            else:
                result_text = result_text + str(count) + text[i]
                count = 1
    if count > 1: 
            result_text = result_text + str(count) + text[-1]    
with open('file_task_5_export.txt', 'w', encoding='utf-8') as result:
    result = result.write(result_text)


with open('file_task_5_export.txt','r', encoding='utf-8') as text:
    text = text.readline().strip()
    result_decoded = ''
    count = ''
    print(text)
    for char in text:
        if char.isdigit():
            count+=char
        else:
            result_decoded += char * int(count)
            count = ''
with open('file_task_5_export_decoded.txt','w', encoding ='utf-8') as result_dec:
    result_dec = result_dec.write(result_decoded)



   