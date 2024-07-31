my_string=input("Введите текст:")
print("В введёном тексте:",len(my_string), "символа(ов)")


#Работа с методами строк

#Выведите строку my_string в верхнем регистре.
print(my_string.upper())
#Выведите строку my_string в нижнем регистре.
print(my_string.lower())
#Измените строку my_string, удалив все пробелы.
print(my_string.replace(" ","" ))
#Выведите первый символ строки my_string.
print(my_string[0])
#Выведите последний символ строки my_string.
print(my_string[-1])