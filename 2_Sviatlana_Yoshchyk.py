stroka="Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"

#Посчитать количество символов
print("1. количество символов:", len(stroka))

#Развернуть строку. Python yes -> sey nohtyP
print("2. Развернутая строка:", stroka[::-1])

#Сделать каждое слово с большой буквы
print("3. Предложение, в котором каждое слово с большой буквы:", stroka.title())

#Сделать весь текст прописными буквами
print("4. весь текст прописными буквами:", stroka.lower())

#Найти число вхождений "нд", "ам", "о" в строку
print("5а. Найти число вхождений 'нд':", stroka.count("нд"))
print("5б. Найти число вхождений 'ам':", stroka.count("ам"))
print("5в. Найти число вхождений 'о':", stroka.count("о"))

#Собственные упражнения
print("Номер индекса буквы'з' со среза:",stroka.find("з", 1,10))
print("Заменить Лондон на Москву:", stroka.replace("Лондоне", "Москве"))
print("Создать список и обьединить его в строку:",' '.join(stroka.split()))
print("Удалить начало строки:", stroka.lstrip("Не знаю, как там в Лондоне, я не была. "))

#Вывести в консоль исходную строку
print(stroka)

#Развернуть предложение. Я Денис -> Денис Я
stroka="Я Денис"
list=stroka.split()
list.reverse()
print(' '.join(list))

#Вывести в консоль исходную строку
print(stroka)