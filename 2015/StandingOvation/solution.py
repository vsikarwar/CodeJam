def solve(maxS, s):
    standing = s[0]
    need = 0
    for i in range(1, len(s)):
        if standing < i:
            need += 1
            standing += 1
        standing += s[i]
    return need


def main(file):
    data = open(file + '.in', 'r').read().splitlines()
    out = open(file + '.out', 'w')
    testCases = int(data[0])

    for tc in range(1, testCases+1):
        testCase = data[tc].split(' ')
        maxS = int(testCase[0])
        s = [int(i) for i in list(testCase[1])]
        result = solve(maxS, s)
        out.write('Case #' + str(tc) + ': ' + str(result) + '\n')


if __name__ == '__main__':
    main('A-small-practice')
    main('A-large-practice')