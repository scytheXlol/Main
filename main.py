print('Это тест "Кто ты из "Колобка". Отвечай на вопросы и узнаешь, на кого ты больше похож!')

question1 = "Если тебе нечего делать, то чем ты займёшься?"
question2 = "Как ты поздороваешься с кем-то незнакомым?"
question3 = "Покажешь ли ты дорогу незнакомцу?"
question4 = "Ты всегда найдёшь, что поесть?"
question5 = "Как часто ты споришь с кем-то?"
kolobok_points = 0

print(question1)
print("1. Пойду скрести по сусекам. 2. Пойду гулять.")
answer1 = input("Введите ответ цифрой: ")
if answer1 == "2":
  kolobok_points = kolobok_points + 1

print(question2)
print("1. Вежливо. 2. Засмеюсь и поздороваюсь, как будто его знаю.")
answer2 = input("Введите ответ цифрой: ")
if answer2 == "2":
  kolobok_points = kolobok_points + 1

print(question3)
print("1. Да. 2. Нет.")
answer3 = input("Введите ответ цифрой: ")
if answer3 == "1":
  kolobok_points = kolobok_points + 1

print(question4)
print("1. Да. 2. Нет.")
answer4 = input("Введите ответ цифрой: ")
if answer4 == "1":
  kolobok_points = kolobok_points + 1

print(question5)
print("1. Часто. 2. Редко.")
answer5 = input("Введите ответ цифрой: ")

if answer5 == "1":
  kolobok_points = kolobok_points + 1

if kolobok_points >= 3:
  print('Из сказки "Колобок" ты определённо сам Колобок! Такой же непосредственный и бесстрашный.')
else:
  print('Из сказки "Колобок" ты бабка, которая испекла Колобка! Вежливый и приятный человек.')