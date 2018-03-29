from account import *
from exchange import *

def main():
        rate = int (input("введите процентную ставку: "))
        money = int (input("введите сумму: "))
        period = int (input("введите период ведения счета в месяцах: "))
        result = calculate_income(rate, money,period)
        print ("Параметры счета:\n", "сумма: ", money, "\n", "Ставка: ",rate, "\n",
                "Период: ", period, "\n", "Сумма на счете в конце периода: ", result)
        x = int (input("Сколько вы хотите снять?"))
        if x<=result:
                ch=  input("Вы хотите обменять? Y - Да, N - Нет")
                if ch == "Y":
                        exchange(result)
        else:
                print ("ваш счет не достаточно!!")
        
if __name__ == "__main__":
    main()
