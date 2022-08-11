def gen(n, debug = False):
    def rec(n, diff, combination, combinations):
        if diff < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                combinations.append(''.join(combination))
        else:
            combination.append('(')
            rec(n-1, diff+1, combination, combinations)
            combination.pop()
            combination.append(')')
            rec(n-1, diff-1, combination, combinations)
            combination.pop()
    combinations = []
    rec(2*n, 0, [], combinations)
    return combinations