def selection_sort(values):
    s_actions = 0
    s_loops = 0
    # perform the bubblesort
    for i in range(len(values) - 1):
        s_loops += 1
        # store a minimum value
        minimum = i
        # find the true minimum from the remaining list
        for j in range(i + 1, len(values)):
            s_loops += 1
            if values[j] < values[minimum]:
                minimum = j
            # perform the swap with the assumed minimum
        values[i], values[minimum] = values[minimum], values[i]
        s_actions += 1
    loopnsort = f"# of actions {s_actions}, number of loops {s_loops}"
    return values, loopnsort

