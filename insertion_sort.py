def insertion_sort(values):
    s_loops = 0
    s_actions = 0
    for step in range(1, len(values)):
        s_loops  += 1
        key = values[step]
        j = step - 1

        # if the current number is than the number behind it, they swap
        while j >= 0 and key < values[j]:
            s_loops += 1
            values[j + 1] = values[j]
            j = j-1

        values[j + 1] = key
        s_actions =+ 1
    loopnsort = f"# of actions {s_actions}, number of loops {s_loops}"
    return values, loopnsort

