def add(num1, num2):
    return num1 + num2



def divide(num1, num2):
    if num2 == 0:
        raise  ValueError #設置一個value錯誤，但是在test裡面是設置ZeroDivisionError，所以會報錯
    return num1 / num2
