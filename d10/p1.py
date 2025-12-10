def solve_machine(lights_pattern, buttons):
    """
    Solve for minimum button presses using Gaussian elimination over GF(2).
    Returns the minimum number of button presses, or -1 if impossible.
    """
    n_lights = len(lights_pattern)
    n_buttons = len(buttons)

    # Build augmented matrix
    # Each row represents a light, each column (except last) represents a button
    # The last column is the target state
    matrix = []
    for light_idx in range(n_lights):
        row = []
        for button_idx in range(n_buttons):
            # Does this button toggle this light?
            row.append(1 if light_idx in buttons[button_idx] else 0)
        # Target state for this light
        target = 1 if lights_pattern[light_idx] == '#' else 0
        row.append(target)
        matrix.append(row)

    # Gaussian elimination over GF(2)
    pivot_cols = []
    row_idx = 0
    for col_idx in range(n_buttons):
        # Find pivot
        pivot_row = None
        for i in range(row_idx, n_lights):
            if matrix[i][col_idx] == 1:
                pivot_row = i
                break

        if pivot_row is None:
            continue

        # Swap rows
        matrix[row_idx], matrix[pivot_row] = matrix[pivot_row], matrix[row_idx]

        # Eliminate
        for i in range(n_lights):
            if i != row_idx and matrix[i][col_idx] == 1:
                for j in range(n_buttons + 1):
                    matrix[i][j] ^= matrix[row_idx][j]

        pivot_cols.append(col_idx)
        row_idx += 1

    # Check for inconsistencies
    for i in range(row_idx, n_lights):
        if matrix[i][n_buttons] == 1:
            # Inconsistent system
            return -1

    # Identify free variables
    free_vars = []
    for col_idx in range(n_buttons):
        if col_idx not in pivot_cols:
            free_vars.append(col_idx)

    # Try all assignments of free variables
    min_presses = float('inf')

    for mask in range(1 << len(free_vars)):
        solution = [0] * n_buttons

        # Set free variables
        for i, var in enumerate(free_vars):
            solution[var] = (mask >> i) & 1

        # Back substitution for dependent variables
        for i in range(len(pivot_cols) - 1, -1, -1):
            col = pivot_cols[i]
            val = matrix[i][n_buttons]
            for j in range(col + 1, n_buttons):
                val ^= (matrix[i][j] & solution[j])
            solution[col] = val

        presses = sum(solution)
        min_presses = min(min_presses, presses)

    return min_presses if min_presses != float('inf') else 0

# Read input
content = open(0).read().strip()
total_presses = 0

for line in content.splitlines():
    if not line.strip():
        continue

    parts = line.split()
    lights_pattern = parts[0][1:-1]  # Remove [ and ]

    # Parse buttons - they're in format (i,j,k) or (i)
    buttons = []
    for i in range(1, len(parts) - 1):
        button_str = parts[i][1:-1]  # Remove ( and )
        if button_str:
            indices = [int(x) for x in button_str.split(',')]
            buttons.append(set(indices))
        else:
            buttons.append(set())

    presses = solve_machine(lights_pattern, buttons)
    total_presses += presses

print(total_presses)
