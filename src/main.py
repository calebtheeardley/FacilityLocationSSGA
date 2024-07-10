from ILP import SolveILP_CFL
from Parsing import parseBeasley

data = parseBeasley("Data/Beasley/Class1/1Cap10.txt")
SolveILP_CFL(data)