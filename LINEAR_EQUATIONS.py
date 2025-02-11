# Description: Program that solves a system of linear equations using Gaussian elimination and back substitution.
def Gaussian_elimination(matrix_variables):
    matrix = matrix_variables[0]
    variables = matrix_variables[1]
    Count_of_variables = len(matrix)
    for column in range(Count_of_variables-1):
        for riadok in range((column+1), Count_of_variables):
            Copy_of_current_column = matrix[column].copy()
            Multiplier_0 = matrix[column][column]
            Multiplier = matrix[riadok][column]
            for _ in range(len(Copy_of_current_column)):
                Copy_of_current_column[_] = Copy_of_current_column[_]*Multiplier
            for _ in range(len(matrix[riadok])):
                matrix[riadok][_] = matrix[riadok][_] * Multiplier_0
                matrix[riadok][_] = matrix[riadok][_] - Copy_of_current_column[_]
    return(matrix, Count_of_variables, variables)

def Back_substitution(matrix,Count_of_variables,variables):
    unknowns = 0
    List_of_variable_constants = [1] * Count_of_variables
    for i in range(1, len(matrix) + 1):
        unknowns+=1
        first = matrix[i * -1].pop(-1)
        for o in range(0, unknowns):
            number = (matrix[i * -1][(o+1)*-1])*List_of_variable_constants[o]
            if o == unknowns-1:
                if number == 0:
                    print("Not possible")
                    return("Not possible")
                else:
                    List_of_variable_constants[unknowns-1] = first/number
            else:
                first-=number
    return(List_of_variable_constants,variables)

def Variables_printout(List_of_variable_constants,variables):
    for i in range(1, len(List_of_variable_constants)+1):
        print(round(List_of_variable_constants[-i],2),variables[i-1])

def start(matrix):
    matrix, Count_of_variables, variables = Gaussian_elimination(input_engine(matrix))
    if Back_substitution(matrix, Count_of_variables, variables) == "Not possible":
        return()
    else:
        List_of_variable_constants,variables = Back_substitution(matrix, Count_of_variables, variables)
        Variables_printout(List_of_variable_constants,variables)
        return()

def input_engine(matrix):



    def equation_input(equation): 
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



    def insert(terms, constant, matrix):
        # Extract coefficients as integers and append the constant
        riadok = [term[0] for term in terms] + [constant]
        matrix.append(riadok)
        return matrix



    def handeling_of_input(matrix):
        num_equations = int(input("Enter the number of equations: "))
        vars = set()

        for _ in range(num_equations):
            terms, constant, variables = equation_input(input("Enter equation: "))
            matrix = insert(terms, constant, matrix) # Insert the equation into the matrix
            vars = vars | variables # Add the variables in current equation to the set of variables
        vars = sorted(vars)
        return (matrix,vars)

    return(handeling_of_input(matrix))
start([])