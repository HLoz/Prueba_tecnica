import csv
from config import ORIGIN_DB


def personas():

    data = open(ORIGIN_DB,"r")
    data = csv.reader(data, delimiter=";", quotechar='"')
    next(data)
    
    contH = 0
    contM = 0
    total_H_y_M = 0

    for register in data:
        if register[4] == "H":
            contH +=1
        if register [4] == "M":
            contM +=1
            total_H_y_M = contH + contM
    
    print(f"La empresa esta compuesta por {total_H_y_M} trabajadores, de los cuales:\n-Hombres son {contH}.\n-Mujeres son {contM}.")

def salarios():
    data = open(ORIGIN_DB,"r")
    data = csv.reader(data, delimiter=";", quotechar='"')
    next(data)

    salarios = []#pos6
    sBruto_empresa1 = 0#pos7
    salario_ct2 = []
    sBruto_ct2 = 0#pos9

    for registro in data:
        if registro[7] == "1":
            salarios.append(float(registro[6]))
            sBruto_empresa1 = sum(salarios)
    
        if registro[9] == "CT2":
            salario_ct2.append(float(registro[6]))
            sBruto_ct2 = sum(salario_ct2)
            sBruto_ct2 = sBruto_ct2
           
    print(f"El salario bruto  anual de los empleados de la Empresa 1 (Equilibra IT) es de: {sBruto_empresa1} €.")    
    print(f"El salario bruto  anual de los empleados del Centro de Alovera (CT2) es de: {sBruto_ct2} €.")
