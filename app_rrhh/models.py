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

