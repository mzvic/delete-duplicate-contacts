def between_lines(a, b):
    with open("file.txt") as f:
        for _ in range(a+1):
            next(f)
        return [next(f).strip() for _ in range(b-a-1)]

print(between_lines(0, 3))  # ['b', 'c']