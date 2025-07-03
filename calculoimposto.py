faturamento = 10000


def CarneLeao(faturamento):
    if(faturamento<=2428.80):
        return print("Isento")
    elif(faturamento>=2.428,81 & faturamento<=2826.65):
        return print(f"Imposto a pagar: {(faturamento*0.075)-182.16}")
    elif(faturamento>=2826.66 & faturamento<=3751.05):
        return print(f"Imposto a pagar: {(faturamento*0.15)-394.16}")
    elif(faturamento>=3751.06 & faturamento<=4664.68):
        return print(f"Imposto a pagar: {(faturamento*0.225)-675.49}")
    else:
        return print(f"Imposto a pagar {(faturamento*0.275)-908.73}")

def SimplesNacional(faturamento):
    if()



CarneLeao(faturamento)