# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello world, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('результат')

# 1st program
print('ответ на задачу №1')
print( (9 **0.5) * 5 )
# 2nd program
print('ответ на задачу №2')
print(9.99 >9.98 and 1000!=1000.1)
# 3rd program
print('ответ на задачу №3')
print(2 * 2 + 2)
print(2 * (2 + 2))
print((2 * 2 + 2)==(2*(2+2)))
# 4th program
print('решение задачи №4')
print('123.456', '-запись чисел в текстовом формате')
print(float('123.456')*10) # текст в число, переносим запятую за 4 = 1234,56
print(int(float('123.456')*10)) #преобразование в целое число = 1234
print(int(float('123.456')*10) /10) # перенос запятой перед 4 =123,4
print(int((int(float('123.456')*10) /10-123)*10) ) #вычетанием убираем числа перед запятой, переносим 4 перед запятой, преобразуем в целое число

print ('решение задачи 4') #c использованием остатка от деления
print(int(float('123.456')*10)%10)