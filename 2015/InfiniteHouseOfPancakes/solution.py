'''
First of all, we fix a number x to be the number of minutes that we expect breakfast to end in after we stop moving pancakes. After that, we pick a plate with more than x pancakes, take x pancakes from that plate and move the pancakes to an empty plate. We keep doing that until all plates has at most x pancakes, then we let the customers eat their pancakes and breakfast ends the earliest for that x value! If we move sum of M(Pi) times, in total, the breakfast ends exactly after x + sum of M(Pi) minutes," you say. "And we can try all possible values of x, since the amount of pancakes cannot be more than 1000. The complexity of the algorithm is O(D*M), where D is the number of diners and M is the maximum number of pancakes
'''

def solve(dinner_num, pan_num):
    max_pancakes = max(pan_num)
    res = max_pancakes
    for i in range(1, max_pancakes):
        moves = 0
        for p in pan_num:
            moves += int((p-1)/i)
        res = min(res, moves+i)
    return res

def main(file):
    data = open(file+'.in', 'r').read().splitlines()
    out = open(file+'.out', 'w')
    testcases = int(data[0])

    case = 0
    for i in range(1, testcases*2, 2):
        dinner_num = int(data[i])
        pan_num = [int(j) for j in data[i+1].split(' ')]
        result = solve(dinner_num, pan_num)
        case += 1
        out.write('Case #' + str(case) + ': ' + str(result) + '\n')


if __name__ == '__main__':
    main('test')
    main('B-small-practice')
    main('B-large-practice')