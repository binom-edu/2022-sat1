# Игры на Python, блок 1
## Занятие 10. Крестики-нолики 1 (24 декабря)
+ начали делать игру Крестики-нолики
+ написали функцию вывода доски
+ выбрали очередность хода
### Домашка
+ Написать приветствие
+ Напишите функцию getUserMove() для получения хода игрока с проверкой корректности.
+ должен быть один символ;
+ символ должен быть цифрой 1-9;
+ сделать из символа число (фукнция int)
+ выбранная клетка должна быть свободна (пробел в списке board)
+ если все проверки пройдены, вернуть номер введенной клетки (число!)

## Занятие 9. Виселица 6 (17 декабря)
+ завершили игру Виселица

## Занятие 8. Виселица 5 (10 декабря)
+ доделали проверки
+ перевод в нижний регистр
+ игровой цикл
+ проверяем, отгадана ли буква
### Домашка
+ проверить окончание игры
+ поражение: в списке wrong 7 букв
+ победа: все буквы secret есть в списке correct
## Занятие 7. Виселица 4 (3 декабря)
+ вывод элементов списка через пробел
+ как создавать свою функцию
+ написали функцию printFrame()
+ начали функцию getUserMove()

### Домашка
+ попробуйте реализовать остальные проверки: введенный символ должен быть в alf и не должен быть среди уже введенных букв.

## Занятие 6. Виселица 3
+ цикл for
+ оператор in
+ выводим кадр

### Домашка
+ сделать, чтобы список ошибок выводился через пробел, без квадратных скобок и запятых; найдите в интернете, как это сделать;
+ подумайте, как сделать проверку корректности ввода;
+ в файле hw6.py содержится одна или несколько ошибок. Исправьте их, чтобы на экран выводилась фраза 'Helloworld'

## Занятие 5. Виселица 2
+ чтение текстового файла
+ выбор случайного слова из списка
+ начало работы над интерфейсом
### Домашка
+ дополнить список слов

## Занятие 4. Виселица 1
+ многострочный литерал
+ список

### Домашка
+ создать текстовый файл (txt) со списком слов для загадывания, сохранить в кодировке utf-8.
+ сделать цикл для вывода всех кадров от 0 до 6 за один запуск.

## Занятие 3
+ каскадное ветвление
+ цикл с условием
+ проверка корректности ввода

### Домашка
+ Исправить логическую ошибку: userChoice - строка, secret - число
+ После заврешения игры предложить пользователю сыграть еще