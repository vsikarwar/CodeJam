'''

'''



def multiply(m, c):

    idx = {'1':0, 'i':1, 'j':2, 'k':3}
    table = [['1', 'i', 'j', 'k'],
             ['i', '-1', 'k', '-j'],
             ['j', '-k', '-1', 'i'],
             ['k', 'j', '-i', '-1']]

    temp = table[idx[m[0]]][idx[c]]
    if len(temp) > 1:
        m[0] = temp[1]
        m[1] *= -1
    else:
        m[0] = temp[0]
        m[1] *= 1

    return m


def solve(s,r):
    mi = ['1', 1]
    mj = ['1', 1]
    mk = ['1', 1]
    ms = ['1', 1]
    for i in range(r):
        ms = ['1', 1]
        ms = multiply(ms, ms)
        for v in s:
            ms = multiply(ms, v)
            if not (mi[0] == 'i' and mi[1] == 1):
                mi = multiply(mi, v)
            elif not (mj[0] == 'j' and mj[1] == 1):
                mj = multiply(mj, v)
            else:
                mk = multiply(mk, v)
        if mj[0] == 'j' and mj[1] == 1:
            break


    if mk[0] == 'k' and mk[1] == 1:
        return 'YES'
    return 'NO'

def main(file):
    inp = open(file+'.in', 'r').read().splitlines()
    out = open(file+'.out', 'w')
    case = 0
    testcases = int(inp[0])
    for tc in range(1, testcases*2, 2):
        rep = int(inp[tc].split(' ')[1])

        s = inp[tc+1]

        result = solve(s, rep)

        case += 1
        out.write('Case #' + str(case) + ': ' + str(result) + '\n')

def test():
    print(solve('jijijijijiji'))

if __name__ == '__main__':
    #main('C-small-practice')
    import time
    print(time.ctime())
    main('C-large-practice')
    print(time.ctime())





