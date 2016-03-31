

def solve(s):
    rate = 0
    xSol = 0
    for i in range(1, len(s)):
        if s[i-1]>s[i]:
            xSol += (s[i-1] - s[i])
            if rate < (s[i-1] - s[i]):
                rate = (s[i-1] - s[i])
    ySol = 0
    for i in range(len(s)-1):
        if s[i] < rate:
            ySol += s[i]
        else:
            ySol += rate

    return xSol, ySol


def main(file):
    inp = open(file+'.in', 'r').read().splitlines()
    out = open(file+'.out', 'w')
    case = 0
    testcases = int(inp[0])
    for tc in range(1, testcases*2, 2):
        v = int(inp[tc])

        s = [int(i) for i in inp[tc+1].split()]

        result = solve(s)

        case += 1
        out.write('Case #' + str(case) + ': ' + str(result[0]) + ' ' + str(result[1]) + '\n')


if __name__ == '__main__':
    main('test')
    main('A-small-practice')
    main('A-large-practice')