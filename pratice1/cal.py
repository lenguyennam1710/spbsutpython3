print ("Welcome to calculator")
while True:
        s = input("mark +,-, *,/: ")
        if s =='0':
                break
        if s in ('+','-','*','/'):
                x = float(input("x = "))
                y = float(input("y = "))
                if s == "+":
                        print ("%.2f" % (x+y))
                elif s == "-":
                        print ("%.2f" % (x-y))
                elif s == "*":
                        print ("%.2f" % (x*y))
                else:
                        if y!=0:
                                print ("%.2f" %(x/y))
                        else:
                                print ("division zero")
        else:
                print ("This mark is not avaiable!")
