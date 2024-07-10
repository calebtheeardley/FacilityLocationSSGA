import cplex
from cplex.exceptions import CplexError

def SolveILP_CFL(data):

    I,J,C,V,G,P = data

    # I=[1,2,3,4,5]
    # J=[1,2,3,4,5]
    # C=[100,100,100,100]
    # V=[10,10,10,10,10]
    # G=[[20,120,12,54,43],
    #    [23,5,43,43,23],
    #    [23,34,23,12,75],
    #    [35,7,4,4,54,2],
    #    [24,7,5,4,32]]
    # P=[[2,3,7,4,3],
    #    [3,4,5,3,2],
    #    [3,5,6,3,2],
    #    [6,3,2,5,3],
    #    [2,4,5,4,2]]

    # I=[1,2]
    # J=[1,2]
    # C=[5,6]
    # V=[4,3]
    # G=[[2,3],
    #    [4,5]]
    # P=[[1,2],
    #    [3,4]]
    
    

    y = [f'y[{i}]' for i in range(len(I))]
    x = [[f'x[{i}][{j}]' for j in range(len(J))] for i in range(len(I))]

    x_flat = [element for sublist in x for element in sublist]
    G_flat = [element for sublist in G for element in sublist]

    print(x)
    print(y)
    print(C)
    print(V)
    print(G)
    print(P)
    
    try:
        problem = cplex.Cplex()
        problem.objective.set_sense(problem.objective.sense.minimize)

        variables = y + x_flat
        coefficients = C + G_flat
        types = problem.variables.type.binary * len(variables)


        problem.variables.add(obj=coefficients,
                            types=types,
                            names=variables)
        
        #Creates all capacity constraints
        capacityConstraints = []
        capacityRHS = []
        capacitySenses = []

        for i in range(len(I)):
            constraint = [[],[]]
            for j in range(len(J)):
                constraint[0].append(x[i][j])
                constraint[1].append(P[i][j])
            constraint[0].append(y[i])
            constraint[1].append(V[i]*-1)

            capacityConstraints.append(constraint)
            capacityRHS.append(0)
            capacitySenses.append('L')

        #Creates all demand constraints
        demandConstraints = []
        demandRHS = []
        demandSenses = []

        for j in range(len(J)):
            constraint = [[],[]]
            for i in range(len(I)):
                constraint[0].append(x[i][j])
                constraint[1].append(1)
            
            demandConstraints.append(constraint)
            demandRHS.append(1)
            demandSenses.append('E')
        

        constraints = capacityConstraints + demandConstraints
        senses = capacitySenses + demandSenses
        rhs = capacityRHS + demandRHS

        for i in range(len(constraints)):
            print(constraints[i], senses[i], rhs[i])

        problem.linear_constraints.add(lin_expr=constraints,
                                    senses=senses,
                                    rhs=rhs)

        # Solve the problem
        problem.solve()

        # Retrieve and print the solution
        solution = problem.solution
        print("Objective value:", solution.get_objective_value())
        for i, var_name in enumerate(variables):
            print(f"{var_name} = {solution.get_values(i)}")

    except CplexError as e:
        print("Cplex error:", e)
