# Пароли. Аssert
# Используя блоки assert, напишите программу для работы с паролем пользователя.
#  На вход подается пароль, а на выход – «ok»,
#  если пароль соответствует критериям, «error» – не соответствует.

# Попробуйте перехватывать в ней AssertionError, а также просто Exception.
# Пример 1
# Ввод Вывод
# 5оЫTuЬШrгэДЦ
# ok
# Пример 2
# Ввод Вывод
# UQжeъGkBT7Uyui
# error
# Пример 3
# Ввод Вывод
# WEсqОЛД
# error
# Примечания
# Критерии правильности пароля аналогичны критериям из задачи
# "Пароли часть 1"из классной работы.
# На этом уроке мы работаем с паролями пользователя.
# Всем известно, что пароли бывают хорошими и плохими.
# Запишем критерии хорошего пароля:
# Длина пароля больше 8 символов.
# В нем присутствуют большие и маленькие буквы любого алфавита.
# В нем имеется хотя бы одна цифра.
# В пароле нет ни одной комбинации из 3 буквенных символов,
# стоящих рядом в строке клавиатуры независимо от того,
# русская раскладка выбрана или английская.
# Например, недопустимы , «QwE», «TYU», «йцу», «Hjk», «ЛДЖ» и т.д.
# А «QWу», «хъф» и т.д. — вполне подходят.
# Причем, надо учесть как раскладку PC-совместимых компьютеров,
#  так и раскладку MAC’ов.
# Напишите программу в стиле LBYL для работы с паролем пользователя.
# На вход подается пароль, а на выход возвращается «ok»,
# если пароль соответствует всем критериям, или «error» в ином случае.
#

keyboard_en = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
               'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']

password = input("Введите пароль")
assert len(password) > 8, "error"
assert ((password != password.lower()) and
        (password != password.upper())), "error"
a = False
for i in range(10):
    if str(i) in password:
        a = True

assert a, "error"

password = password.lower()

b = True
count_i = -1
for j in range(5):
    count = 0
    for i, val in enumerate(keyboard_en[j]):
        if val in password:
            count += 1

        else:
            count = 0
        if count == 3:
            b = False

assert b, "error"
print(b)
