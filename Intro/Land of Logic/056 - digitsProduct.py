def digitsProduct(product):
    num = 4000
    menor = 4000
    while True:
        cum = 1
        #Multiply all eachs elements
        for elem in list(str(num)):
                cum *= int(elem)

        if cum == product:
                menor = num

        num = num - 1 

        if (num == 0) & (menor == 4000):
                return -1
        elif num== 0:
                return menor
