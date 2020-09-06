N = int(input())
with open("input/popular-names.txt", mode='r') as f:
    all_lines = f.read().split('\n')
    LINES = (len(all_lines) + N - 1) // N
    for index, line_idx in enumerate(range(0, len(all_lines), LINES)):
        with open("output/16-py-{:02d}.txt".format(index), mode='w') as out:
            out.write('\n'.join(all_lines[line_idx:line_idx + LINES]))

