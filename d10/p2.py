from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PULP_CBC_CMD

def solve_machine_part2(buttons, targets):
    """
    Solve for minimum button presses in joltage mode using integer linear programming.

    buttons: list of sets, where buttons[i] contains indices of counters affected
    targets: list of target values for each counter

    Returns the minimum total button presses.
    """
    n_counters = len(targets)
    n_buttons = len(buttons)

    # Create the LP problem
    prob = LpProblem("ButtonPresses", LpMinimize)

    # Create variables for button presses (must be non-negative integers)
    button_vars = [LpVariable(f"button_{i}", lowBound=0, cat='Integer') for i in range(n_buttons)]

    # Objective: minimize sum of button presses
    prob += lpSum(button_vars)

    # Constraints: for each counter, the sum of presses affecting it must equal target
    for counter_idx in range(n_counters):
        constraint = lpSum(button_vars[button_idx] for button_idx in range(n_buttons)
                          if counter_idx in buttons[button_idx])
        prob += constraint == targets[counter_idx]

    # Solve
    prob.solve(PULP_CBC_CMD(msg=0))

    # Check if solved optimally
    if prob.status == 1:  # Optimal solution found
        total_presses = int(sum(var.varValue for var in button_vars))
        return total_presses

    return -1

# Read input
content = open(0).read().strip()
total_presses = 0

for line in content.splitlines():
    if not line.strip():
        continue

    parts = line.split()

    # Parse buttons - they're in format (i,j,k) or (i)
    buttons = []
    for i in range(1, len(parts) - 1):
        button_str = parts[i][1:-1]  # Remove ( and )
        if button_str:
            indices = [int(x) for x in button_str.split(',')]
            buttons.append(set(indices))
        else:
            buttons.append(set())

    # Parse targets - last part in format {3,5,4,7}
    targets_str = parts[-1][1:-1]  # Remove { and }
    targets = [int(x) for x in targets_str.split(',')]

    presses = solve_machine_part2(buttons, targets)
    if presses == -1:
        print(f"ERROR: Could not solve {line}", file=__import__('sys').stderr)
    total_presses += presses

print(total_presses)
