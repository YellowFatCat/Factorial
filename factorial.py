# Функция вычисления факториала.
# Возвращает 0, если факториал не может быть вычислен, и ненулевое результирующее значение для корректных входных данных.
def fact(n):
    '''Calculates factorial for argument n
    '''
    try:
        n = int(n);
    except ValueError:
        return 0; # Введено вещественное число или некорректный символ (строка).

    if (n < 0): return 0; # Введено отрицательное число.
    
    if (n == 0): # По определению 0! = 1.
        return 1;
    
    return n*fact(n-1);

flag = True; # Если флаг поднят, то работа программы продолжается.
while (flag):
    x = input("Введите аргумент для вычисления факториала: ");
    
    if (fact(x) == 0): print("Факториал определён только для целых неотрицательных чисел.");
    else: print ("Факториал введенного числа:", fact(x));
    
    answ = input("Продолжить работу? (Y/N): ");
    answ = answ.lower();
    if answ in ('y', 'yes'): flag = True;
    else: flag = False;
    if (flag): print("");
