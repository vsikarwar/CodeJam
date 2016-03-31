
def countServedCustomer(T, m):
    res = 0
    for i in m:
        res += T//i + 1
    return res

def solve(b,n,m):

    low = -1
    high = 10000 * n
    while low + 1 < high:
        mid = (low + high)//2
        if countServedCustomer(mid, m) < n:
            low = mid
        else:
            high = mid

    T = high
    customer_serviced_before = countServedCustomer(T - 1, m)
    customer_serviced_after = n - customer_serviced_before

    for i in range(b):
        if T % m[i] == 0:
            customer_serviced_after -= 1
            if customer_serviced_after == 0:
                return i

def main(file):
    inp = open(file+'.in', 'r').read().splitlines()
    out = open(file+'.out', 'w')
    case = 0
    testcases = int(inp[0])
    for tc in range(1, testcases*2, 2):
        #Line one
        b, n = [int(i) for i in inp[tc].split()]
        #Line two
        m = [int(i) for i in inp[tc+1].split()]

        result = solve(b, n, m)

        case += 1
        out.write('Case #' + str(case) + ': ' + str(result+1) + '\n')


if __name__ == '__main__':
    main('test')
    main('B-small-practice')
    main('B-large-practice')