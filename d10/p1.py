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
    pivot_col = 0
    for row_idx in range(n_lights):
        if pivot_col >= n_buttons:
            break

        # Find pivot
        pivot_row = None
        for i in range(row_idx, n_lights):
            if matrix[i][pivot_col] == 1:
                pivot_row = i
                break

        if pivot_row is None:
            pivot_col += 1
            row_idx -= 1
            continue

        # Swap rows
        matrix[row_idx], matrix[pivot_row] = matrix[pivot_row], matrix[row_idx]

        # Eliminate
        for i in range(n_lights):
            if i != row_idx and matrix[i][pivot_col] == 1:
                for j in range(n_buttons + 1):
                    matrix[i][j] ^= matrix[row_idx][j]

        pivot_col += 1

    # Back substitution / check for solutions
    solution = [0] * n_buttons

    for row_idx in range(n_lights - 1, -1, -1):
        # Find the leading 1 in this row
        leading_col = None
        for col_idx in range(n_buttons):
            if matrix[row_idx][col_idx] == 1:
                leading_col = col_idx
                break

        if leading_col is None:
            # This row is all zeros (except possibly the augmented column)
            if matrix[row_idx][n_buttons] == 1:
                # Inconsistent system
                return -1
            continue

        # Set the solution for this variable
        val = matrix[row_idx][n_buttons]
        for col_idx in range(leading_col + 1, n_buttons):
            val ^= (matrix[row_idx][col_idx] & solution[col_idx])
        solution[leading_col] = val

    return sum(solution)

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
