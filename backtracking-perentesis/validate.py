def is_valid1(combination):
    # Initiate empty stack
    stack = []
    # Iterate over chars in combination
    for par in combination:
        # Append stack if we found and opening (
        if par == '(':
            stack.append(par)
            print(stack)
        else:
            # Validity condition1: not poping from empty stack
            # Otherwise it meens that we found a closing parentheses without an opening one from it
            if len(stack) == 0:
                return False
            # remove one record from stack if we found a closing one
            else:
                stack.pop()
    # Validity cond #2: stack should be empty at the end
    # Otherwise it means that we have opening parentheses that we didn't close
    return len(stack) == 0

def is_valid2(combination):
    # Use int as counter
    diff = 0
    # Iterate over chars in combination
    for par in combination:
        # increase counter if we found an opening bracket
        if par == '(':
            diff += 1
        else:
            # Validity condition1: if counter is 0 than we have empty stack and can't decrease it
            # Otherwise it meens that we found a closing parentheses without an opening one from it
            if diff == 0:
                return False
            # decrease counter if we found a closing bracket
            else:
                diff -= 1
    # Validity cond #2: stack should be empty at the end
    # Otherwise it means that we have opening parentheses that we didn't close
    return diff == 0