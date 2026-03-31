# Дополнительное задание 2

def digit_root(num):
    while num > 9:
        summa = 0
        while num > 0:
            summa = summa + num % 10
            num = num // 10
        num = summa
    print(num)

digit_root(4851)
digit_root(97569)
digit_root(889987)