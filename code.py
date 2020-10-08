from pulp import *

# A list of strings from "1" to "8" is created
Sequence = ["1", "2", "3", "4", "5", "6", "7", "8"]

# The Vals, Rows and Cols sequences all follow this form
Vals = ["Q", "-"]
Rows = Sequence
Cols = Sequence

# The prob variable is created to contain the problem data
prob = LpProblem("8 Queens Problem", LpMinimize)

# The problem variables are created
choices = LpVariable.dicts("Choice",(Vals,Rows,Cols),0,1,LpInteger)

# The arbitrary objective function is added
prob += 0, "Arbitrary Objective Function"

# A constraint ensuring that only one value can be in each square is created
for r in Rows:
    for c in Cols:
        prob += lpSum([choices[v][r][c] for v in Vals]) == 1, ""

# The row, column and box constraints are added for each value
for r in Rows:
    prob += lpSum([choices["Q"][r][c] for c in Cols]) == 1, ""

for c in Cols:
    prob += lpSum([choices["Q"][r][c] for r in Rows]) == 1, ""

# TODO add diagonal constraint
# Diags = []
# for d in Diags:
#     prob += lpSum([choices["Q"][r][c] for (r,c ) in d]) == 1, ""

# The problem data is written to an .lp file
prob.writeLP("8Queens.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

for r in Rows:
    for c in Cols:
        if value(choices["Q"][r][c]) == 1:
            print('Q', end='')
            # check x vs y
        else:
            print("_", end='')
    print(" ")
