faturamento = 10000
Folha= 2000
fatorR= (Folha/faturamento)
SimplesNacional= True
def CarneLeao(faturamento):
    if(faturamento<=2428.80):
        return print("Isento")
    elif(faturamento>=2.428,81 & faturamento<=2826.65):
        return print(f"Imposto a pagar: R${(faturamento*0.075)-182.16:.2f}")
    elif(faturamento>=2826.66 & faturamento<=3751.05):
        return print(f"Imposto a pagar: R${(faturamento*0.15)-394.16}")
    elif(faturamento>=3751.06 & faturamento<=4664.68):
        return print(f"Imposto a pagar: R${(faturamento*0.225)-675.49}")
    else:
        return print(f"Imposto a pagar R${(faturamento*0.275)-908.73:.2f}")

def SimplesNacionalAnexoV(faturamento):
    Fat12=faturamento*12
    if(Fat12<=180000):
        return print(f"Imposto a pagar: R${faturamento*0.155}")
    elif(Fat12>180000 & Fat12<=360000):
        AliquotaEfetiva= ((Fat12*0.18)-4500)/Fat12
        return print(f"Imposto a pagar: R${faturamento*AliquotaEfetiva:.2f}, faturamento {faturamento} Aliquota efetiva {AliquotaEfetiva*100:.2f}%")
    elif(Fat12>360000 & Fat12<=720000):
        AliquotaEfetiva= ((Fat12*0.195)-9900)/Fat12
        return print(f"Imposto a pagar: {faturamento*AliquotaEfetiva:.2f}, faturamento {faturamento} Aliquota efetiva {AliquotaEfetiva*100:.2f}%")
    elif(Fat12>720000 & Fat12<=1800000):
        AliquotaEfetiva= ((Fat12*0.205)-17100)/Fat12
        return print(f"Imposto a pagar: {faturamento*AliquotaEfetiva:.2f}, faturamento {faturamento} Aliquota efetiva {AliquotaEfetiva*100:.2f}%")
    elif(Fat12>1800000 & Fat12<=3600000):
        AliquotaEfetiva= ((Fat12*0.23)-62100)/Fat12
        return print(f"Imposto a pagar: {faturamento*AliquotaEfetiva:.2f}, faturamento {faturamento} Aliquota efetiva {AliquotaEfetiva*100:.2f}%")
    elif(Fat12>3600000 & Fat12<=4800000):
        AliquotaEfetiva= ((Fat12*0.305)-540000)/Fat12
        return print(f"Imposto a pagar: {faturamento*AliquotaEfetiva:.2f}, faturamento {faturamento} Aliquota efetiva {AliquotaEfetiva*100:.2f}%")

def SimplesNacionalAnexoIII(faturamento):
    Fat12=faturamento*12
    if(Fat12<=180000):
        return print(f"Imposto a pagar: R${faturamento*0.06}")
    elif(Fat12>180000 & Fat12<=360000):
        AliquotaEfetiva= ((Fat12*0.112)-9360)/Fat12
        return print(f"Imposto a pagar: R${faturamento*AliquotaEfetiva:.2f}, faturamento {faturamento} Aliquota efetiva {AliquotaEfetiva*100:.2f}%")
    elif(Fat12>360000 & Fat12<=720000):
        AliquotaEfetiva= ((Fat12*0.135)-17640)/Fat12
        return print(f"Imposto a pagar: {faturamento*AliquotaEfetiva:.2f}, faturamento {faturamento} Aliquota efetiva {AliquotaEfetiva*100:.2f}%")
    elif(Fat12>720000 & Fat12<=1800000):
        AliquotaEfetiva= ((Fat12*0.16)-35640)/Fat12
        return print(f"Imposto a pagar: {faturamento*AliquotaEfetiva:.2f}, faturamento {faturamento} Aliquota efetiva {AliquotaEfetiva*100:.2f}%")
    elif(Fat12>1800000 & Fat12<=3600000):
        AliquotaEfetiva= ((Fat12*0.21)-125640)/Fat12
        return print(f"Imposto a pagar: {faturamento*AliquotaEfetiva:.2f}, faturamento {faturamento} Aliquota efetiva {AliquotaEfetiva*100:.2f}%")
    elif(Fat12>3600000 & Fat12<=4800000):
        AliquotaEfetiva= ((Fat12*0.33)-648000)/Fat12
        return print(f"Imposto a pagar: {faturamento*AliquotaEfetiva:.2f}, faturamento {faturamento} Aliquota efetiva {AliquotaEfetiva*100:.2f}%")


if(SimplesNacional):
    if(fatorR>=0.28):
        print("------ Anexo III ------")
        print(f"Fator R: {fatorR}, Folha: {Folha}, Faturamento: {faturamento}")
        SimplesNacionalAnexoIII(faturamento)
    else:
        print("------ Anexo V ------")
        print(f"Fator R: {fatorR}, Folha: {Folha}, Faturamento: {faturamento}")
        SimplesNacionalAnexoV(faturamento)
else:
    print("---- Carnê Leão ----")
    CarneLeao(faturamento)
    