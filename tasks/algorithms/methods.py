def maximax(rows: int, columns: int, matrix) -> str:
    maxPays = []
    for r in range(rows):
        values = []
        for c in range(columns):
            num = matrix[r][c]
            values.append(num)
        maxPays.append(max(values))
    maxPay = max(maxPays)

    project = f"project {maxPays.index(maxPay) + 1}"
    return f"{maxPay} {project}"


def maximin(rows: int, columns: int, matrix) -> str:
    maxPays = []
    for r in range(rows):
        values = []
        for c in range(columns):
            num = matrix[r][c]
            values.append(num)
        maxPays.append(min(values))
    maxPay = max(maxPays)

    project = f"project {maxPays.index(maxPay) + 1}"
    return f"{maxPay} {project}"


def minimax_regret(rows: int, columns: int, matrix) -> str:
    # 1. get max value from each column
    max_values = []
    for c in range(columns):
        values = []
        for r in range(rows):
            num = matrix[r][c]
            values.append(num)
        max_values.append(max(values))

    # 2. subtract each value from max value
    new_values = []
    for c in range(columns):
        new_values.append([])
        for r in range(rows):
            num = matrix[r][c]
            new_values[c].append(max_values[c] - num)

    # 3. get max value from each row
    max_values = []
    for r in range(rows):
        values = []
        for c in range(columns):
            num = new_values[c][r]
            values.append(num)
        max_values.append(max(values))

    # 4. pick minimum value from max_values
    min_value = min(max_values)

    project = f"project {max_values.index(min_value) + 1}"
    return f"{min_value} {project}"


def equally_likely(rows: int, columns: int, matrix) -> str:
    # 1. get average value for each row
    avg_values = []
    for r in range(rows):
        values = []
        for c in range(columns):
            num = matrix[r][c]
            values.append(num)
        avg_values.append(sum(values) / len(values))

    # 2. pick maximum value from average values
    max_value = max(avg_values)

    project = f"project {avg_values.index(max_value) + 1}"
    return f"{max_value} {project}"
