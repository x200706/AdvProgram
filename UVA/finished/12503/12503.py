cases = int(input())
for _ in range(cases):
    n = int(input())
    log = []
    current = 0

    for _ in range(n):
        line = input().strip()
        parts = line.split()

        step = 0
        if parts[0] == "LEFT":
            step = -1
        elif parts[0] == "RIGHT":
            step = 1
        elif parts[0] == "SAME":
            index = int(parts[2])
            step = log[index - 1]
        
        current += step
        log.append(step)

    print(current)