def exchange(money):
        usd = 57
        euro = 60
        aud = 44
        currency = int(input("Укажите код валюты(доллары - 400. евро - 401, Австралийский доллар - 402 ): "))

        if currency == 400:
                cache = round(money/usd, 2)
                print ("вылюта: доллары США ")
        elif currency == 401:
                cache = round(money/euro, 2)
                print ("вылюта: эвро")
        elif currency == 402:
                cache = round(money/aud, 2)
                print ("вылюта: Австралийский доллар")
        else:
                cache = 0
        print("Неизвестная валюта")
        print ("к получению: ", cache)
def main():
        money = int(input("введите сумму, которую вы хотите обменять: "))
        exchange(money)
if __name__ == "__main__":
        main()
