def print_ascii_gantt(gantt):
    """
    gantt: List of tuples -> [(start, end, pid), ...]
    Example:
    [(0, 8, 'P1'), (8, 12, 'P2'), (12, 21, 'P3'), (21, 26, 'P4')]
    """

    scale = 1  # 1 time unit = 1 character

    # Top border
    total_width = sum((end - start) * scale for start, end, _ in gantt) + len(gantt) + 1
    print("-" * total_width)

    # Process row
    row = "|"
    for start, end, pid in gantt:
        width = (end - start) * scale
        row += pid.center(width) + "|"
    print(row)

    # Bottom border
    print("-" * total_width)

    # Time labels row
    time_row = ""
    cursor = 0

    for start, end, _ in gantt:
        start_str = str(start)
        time_row += " " * (cursor - len(time_row)) + start_str
        cursor += (end - start) * scale + 1

    # Final end time
    end_time = str(gantt[-1][1])
    time_row += " " * (cursor - len(time_row)) + end_time

    print(time_row)
