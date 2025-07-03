
function CarneLeao(faturamento)
{
    if(faturamento<=2428.80)
    {
        return 0;
    }
    else if(faturamento>=2428.81 && faturamento<=2826.65)
    {
        return (faturamento*0.075)-182.16;
    }
    else if(faturamento>=2826.66 && faturamento<=3751.05)
    {
        return (faturamento*0.15)-394.16;
    }
    else if(faturamento>=3751.06 && faturamento<=4664.68)
    {
        return (faturamento*0.225)-675.49;
    }
    else if(faturamento>4664.68)
    {
        return (faturamento*0.275)-908.73;
    }  
} 

function SimplesNacionalAnexoV(faturamento)
{
    let Fat12=faturamento*12;
    if(Fat12<=180000)
    {
        return faturamento*0.155;
    }
    else if(Fat12>180000 && Fat12<=360000)
    {
        AliquotaEfetiva= ((Fat12*0.18)-4500)/Fat12;
        return faturamento*AliquotaEfetiva;
    }
    else if(Fat12>360000 && Fat12<=720000)
    {
        AliquotaEfetiva= ((Fat12*0.195)-9900)/Fat12
        return faturamento*AliquotaEfetiva;
    }
    else if(Fat12>720000 && Fat12<=1800000)
    {
        AliquotaEfetiva= ((Fat12*0.205)-17100)/Fat12;
        return faturamento*AliquotaEfetiva;
    }
    else if(Fat12>1800000 && Fat12<=3600000)
    {
        AliquotaEfetiva= ((Fat12*0.23)-62100)/Fat12;
        return faturamento*AliquotaEfetiva;
    }
    else if(Fat12>3600000 && Fat12<=4800000)
    {
        AliquotaEfetiva= ((Fat12*0.305)-540000)/Fat12;
        return faturamento*AliquotaEfetiva;
    }
}

function SimplesNacionalAnexoIII(faturamento)
{
    Fat12=faturamento*12;
    if(Fat12<=180000)
    {
        return faturamento*0.06;
    }
    else if(Fat12>180000 && Fat12<=360000)
    {
        AliquotaEfetiva= ((Fat12*0.112)-9360)/Fat12;
        return faturamento*AliquotaEfetiva;
    }
    else if(Fat12>360000 && Fat12<=720000)
    {
        AliquotaEfetiva= ((Fat12*0.135)-17640)/Fat12;
        return faturamento*AliquotaEfetiva;
    }
    else if(Fat12>720000 && Fat12<=1800000)
    {
        AliquotaEfetiva= ((Fat12*0.16)-35640)/Fat12;
        return faturamento*AliquotaEfetiva;
    }
    else if(Fat12>1800000 && Fat12<=3600000)
    {
        AliquotaEfetiva= ((Fat12*0.21)-125640)/Fat12;
        return faturamento*AliquotaEfetiva;
    }
    else if(Fat12>3600000 && Fat12<=4800000)
    {
        AliquotaEfetiva= ((Fat12*0.33)-648000)/Fat12;
        return faturamento*AliquotaEfetiva;
    }
}

function LucroPresumido(faturamento, Equipara)
{
    if (Equipara)
    {
        return faturamento*0.1633
    }
    else
    {
        return faturamento*0.1093
    }
}
function MostraFat()
{
var faturamento= document.getElementById("faturamento").value;
document.getElementById("MostraFat").innerHTML="Faturamento: R$"+ faturamento;
}
function MostrarCarne()
{
    const valor = parseFloat(document.getElementById("faturamento").value);
    const resultado = CarneLeao(valor);
    document.getElementById("impostocarne").innerText ="Imposto R$:" + resultado.toFixed(2);
}
function MostrarAnexoV()
{
    const valor = parseFloat(document.getElementById("faturamento").value);
    const resultado = SimplesNacionalAnexoV(valor);
    document.getElementById("impostoanexov").innerText ="Imposto: R$" + resultado.toFixed(2);
}
function MostrarAnexoIII()
{
    const valor = parseFloat(document.getElementById("faturamento").value);
    const resultado = SimplesNacionalAnexoIII(valor);
    document.getElementById("impostoanexoIII").innerText ="Imposto: R$" + resultado.toFixed(2);
    document.getElementById("folhamin").innerText ="Folha mínima: R$"+(valor*0.28).toFixed(2);
}
function MostraLucroPresumido()
{
    const valor = parseFloat(document.getElementById("faturamento").value);
    const resultado= LucroPresumido(valor,true);
    document.getElementById("lucropresumido").innerText= "Imposto: R$"+resultado;
    const resultado2= LucroPresumido(valor,false);
    document.getElementById("lucroequipa").innerText="Imposto: R$"+resultado2;
}