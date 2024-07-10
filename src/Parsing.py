import numpy as np
from typing import Tuple

def parseBeasley(filename : str) -> Tuple[list, list, list, list, list[list], list[list]]: #(I,J,C,V,G,P)

    with open(filename, 'r') as file:
        for _ in range(3):
            next(file)

        line = next(file)
        row = [float(value) for value in line.split()]
        fixedCost = row[1]
        capacity = row[2]

        for _ in range(1):
            next(file)

        data = []
        for line in file:
            row = [float(value) for value in line.split()]
            if(len(row)>0):
                data.append(row)

    facilities = 0
    clients = 0

    for row in data:
        if(row[0] > facilities):
            facilities = row[0]
        if(row[1] > clients):
            clients = row[1]
    facilities = int(facilities)
    clients = int(clients)

    I : list = []
    J : list = []

    for i in range(facilities):
        I. append(i+1)

    for j in range(clients):
        J. append(j+1)

    C = [fixedCost for _ in range(facilities)] #Fixed cost
    V = [capacity for _ in range(facilities)]  #Capacity
    G = [[0 for _ in range(facilities)] for _ in range(clients)] #Cost for facility to client
    P = [[0 for _ in range(facilities)] for _ in range(clients)] #Demand

    for row in data:
        facility = int(row[0])
        client = int(row[1])
        cost = row[2]
        demand = row[3]

        G[facility-1][client-1] = cost
        P[facility-1][client-1] = demand

    return(I,J,C,V,G,P)






