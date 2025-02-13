# Description: Program that solves a system of linear equations using Gaussian elimination and back substitution.
def Gaussian_elimination(matrix):
    count_of_variables = len(matrix)
    pos = 0
    for column in range(count_of_variables-1):
        roww = column
        list_of_variables = []
        for row_lower_than_roww in range(roww, count_of_variables):
            col = min(roww,(len(matrix[row_lower_than_roww])-1))
            list_of_variables.append(abs(matrix[row_lower_than_roww][col]))
        max_value = max(list_of_variables)
        max_index = list_of_variables.index(abs(max_value))+pos
        matrix[roww], matrix[max_index] = matrix[max_index], matrix[roww]
        pos+=1
        for roow in range((column+1), count_of_variables):
            copy_of_current_column = matrix[column].copy()
            multiplier_0 = matrix[column][column]
            multiplier = matrix[roow][column]
            for _ in range(len(copy_of_current_column)):
                copy_of_current_column[_] = copy_of_current_column[_]*multiplier
            for _ in range(len(matrix[roow])):
                matrix[roow][_] = matrix[roow][_] * multiplier_0
                matrix[roow][_] = matrix[roow][_] - copy_of_current_column[_]
    return(matrix)


def Back_substitution(matrix,variables):
    coeffs = [row[:-1] for row in matrix]
    nulls_row= []
    for i in range(len(coeffs)):
        non_zero = False
        for m in range(len(coeffs[i])):
            if coeffs[i][m] != 0:
                non_zero = True
                break
        if not non_zero:
            if matrix[i][-1] != 0:
                return "No solution"
            else:
                nulls_row.append(i)
    if len(nulls_row) == 0:
        pass
    else:
        min_null_row = min(nulls_row)
        coeffs = coeffs[:min_null_row]
        matrix = matrix[:min_null_row]
    constants = [row[-1] for row in matrix]
    pivots = set()
    for row in range(len(coeffs)):
        for i,num in enumerate(coeffs[row]):
            if num != 0:
                pivots.update(variables[i])
                break
    free_vars = set(variables) - pivots
    if len(pivots) == len(variables):
        solutions = {var: 0 for var in variables}
        for i in range(len(coeffs)-1, -1, -1):
            sum_ax = sum(coeffs[i][j] * solutions[variables[j]] for j in range(i+1, len(coeffs)))
            solutions[variables[i]] = (constants[i] - sum_ax) / coeffs[i][i]
        return(solutions)
    else:
        for i in range(len(constants)):
            first = True
            for m in range(len(coeffs[i])):
                if first:
                    if coeffs[i][m] != 0:
                        first = False
                        coef = coeffs[i][m]
                else:

                    if coeffs[i][m] == 0:
                        continue
                    else:
                        constants[i] = str(constants[i])+"-(" +str(coeffs[i][m])+")" +"*"+ str(variables[m])
            constants[i] = "("+str(constants[i])+")"+"/"+str(coef)
            pivots = sorted(list(pivots))
            print(str(pivots[i])+" = "+constants[i])
        for i in free_vars:
            print(i + " = " + i)
        return "Infinite solutions"

def Start(matrix):
    matrix, variables = Input_engine(matrix)
    matrix = Gaussian_elimination(matrix)
    print(Back_substitution(matrix, variables))


def Input_engine(matrix):


    def Equation_input(equation): 
        equation = equation.split("=")
        constant = float(equation[1].strip())
        equation_variables = equation[0].replace(" ", "")# Remove spaces

        terms = []
        variables = set()

        equation_variables = equation_variables.replace("+", " +").replace("-", " -").split()

        for term in equation_variables: # Split the equation into terms
            if term[-1].isalpha():
                coefficient = term[:-1].lstrip("+")
                variable = term[-1]
                variables.add(variable)

                if coefficient == "" or coefficient == "-":  # Handle missing coefficients (x → 1x, -x → -1x)
                        coefficient += "1"
                terms.append((float(coefficient), variable))
            else:
                constant -= float(term)            
        
        terms.sort(key=lambda x: x[1]) # Sort by variable
        return (terms, constant, variables)



    def Handeling_of_input(matrix):
        num_of_equations = int(input("Enter the number of equations: "))
        vars = set()
        equations = []

        for _ in range(num_of_equations):
            terms, constant, variables = Equation_input(input("Enter equation: "))
            equations.append((terms, constant))
            vars = vars | variables # Add the variables in current equation to the set of variables
        vars = sorted(vars)
        
        for m in range(len(equations)):
            row = [0]*(len(vars)+1)
            row[-1] = equations[m][-1]
            for n in range(len(equations[m][0])):
                term = equations[m][0][n][1]
                row[vars.index(term)] = equations[m][0][n][0]
            matrix.append(row)
        return (matrix,vars)

    return(Handeling_of_input(matrix))
Start([])