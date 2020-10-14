from pulp import *

# Represents the possible values of a cell
Vals = ["Q", "-"]

# Represents the rows and columns of the board
Sequence = [0, 1, 2, 3, 4, 5, 6, 7]
Rows = Sequence
Cols = Sequence

prob = LpProblem("8 Queens Problem", LpMinimize)
choices = LpVariable.dicts("Choice", (Vals, Rows, Cols), 0, 1, LpInteger)

# We do not want a specific objective, therefore we just have 0
prob += 0, "objective function"

# This constraint ensures that every cell will get exactly one assignment of a value
for r in Rows:
    for c in Cols:
        prob += lpSum([choices[v][r][c] for v in Vals]) == 1, ""

# These constraints ensure that all rows and all columns have exactly 1 queen
for r in Rows:
    prob += lpSum([choices["Q"][r][c] for c in Cols]) == 1, ""

for c in Cols:
    prob += lpSum([choices["Q"][r][c] for r in Rows]) == 1, ""

# These constraints ensure that there is at most one queen per diagonal
for c in range(0, 17):
    # from top left to bottom right
    prob += lpSum([choices["Q"][i][c + i - 8] for i in Sequence if 16 > c + i >= 8]) <= 1, ""
    # from top right to bottom left
    prob += lpSum([choices["Q"][i][c - i] for i in Sequence if 8 > c - i >= 0]) <= 1, ""

prob.writeLP("8Queens.lp")

# Solve the problem
prob.solve()
print("Status:", LpStatus[prob.status])

# Print solution
for r in Rows:
    for c in Cols:
        if value(choices["Q"][r][c]):
            print('Q ', end='')
        else:
            print("_ ", end='')
    print(" ")
