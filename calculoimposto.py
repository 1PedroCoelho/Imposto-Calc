faturamento = 10000
Folha= 2800
fatorR= (Folha/faturamento)
SimplesNacional= False
EquiHosp=False
def CarneLeao(faturamento):
    if(faturamento<=2428.80):
        return print("Isento")
    elif(faturamento>=2428.81 and faturamento<=2826.65):
        return (faturamento*0.075)-182.16
    elif(faturamento>=2826.66 and faturamento<=3751.05):
        return (faturamento*0.15)-394.16
    elif(faturamento>=3751.06 and faturamento<=4664.68):
        return (faturamento*0.225)-675.49
    elif(faturamento>4664.68):
        return (faturamento*0.275)-908.73

def SimplesNacionalAnexoV(faturamento):
    Fat12=faturamento*12
    if(Fat12<=180000):
        return faturamento*0.155
    elif(Fat12>180000 and Fat12<=360000):
        AliquotaEfetiva= ((Fat12*0.18)-4500)/Fat12
        return faturamento*AliquotaEfetiva
    elif(Fat12>360000 and Fat12<=720000):
        AliquotaEfetiva= ((Fat12*0.195)-9900)/Fat12
        return faturamento*AliquotaEfetiva
    elif(Fat12>720000 and Fat12<=1800000):
        AliquotaEfetiva= ((Fat12*0.205)-17100)/Fat12
        return faturamento*AliquotaEfetiva
    elif(Fat12>1800000 and Fat12<=3600000):
        AliquotaEfetiva= ((Fat12*0.23)-62100)/Fat12
        return faturamento*AliquotaEfetiva
    elif(Fat12>3600000 and Fat12<=4800000):
        AliquotaEfetiva= ((Fat12*0.305)-540000)/Fat12
        return faturamento*AliquotaEfetiva

def SimplesNacionalAnexoIII(faturamento):
    Fat12=faturamento*12
    if(Fat12<=180000):
        return faturamento*0.06
    elif(Fat12>180000 and Fat12<=360000):
        AliquotaEfetiva= ((Fat12*0.112)-9360)/Fat12
        return faturamento*AliquotaEfetiva
    elif(Fat12>360000 and Fat12<=720000):
        AliquotaEfetiva= ((Fat12*0.135)-17640)/Fat12
        return faturamento*AliquotaEfetiva
    elif(Fat12>720000 and Fat12<=1800000):
        AliquotaEfetiva= ((Fat12*0.16)-35640)/Fat12
        return faturamento*AliquotaEfetiva
    elif(Fat12>1800000 and Fat12<=3600000):
        AliquotaEfetiva= ((Fat12*0.21)-125640)/Fat12
        return faturamento*AliquotaEfetiva
    elif(Fat12>3600000 and Fat12<=4800000):
        AliquotaEfetiva= ((Fat12*0.33)-648000)/Fat12
        return faturamento*AliquotaEfetiva

def LucroPresumido(faturamento, Equipara):
    if(Equipara):
        return faturamento*0.1633
    else:
        return faturamento*0.1093



if(SimplesNacional):
    if(fatorR>=0.28):
        print("------ Anexo III ------")
        print(f"Fator R: {fatorR}, Folha: {Folha}, Faturamento: {faturamento}")
        print(f"R${SimplesNacionalAnexoIII(faturamento)}")
    else:
        print("------ Anexo V ------")
        print(f"Fator R: {fatorR}, Folha: {Folha}, Faturamento: {faturamento}")
        print(f"R${SimplesNacionalAnexoV(faturamento)}")
else:
    LivroCaixa=0
    faturamento-=LivroCaixa
    print("---- Carnê Leão ----")
    print(CarneLeao(faturamento))
    