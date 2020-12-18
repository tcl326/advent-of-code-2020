def basic_ops(ops, num1, num2):
    if ops == "+":
        return num1 + num2
    elif ops == "*":
        return num1 * num2
    return None


def evaluate(calculation):
    nums = []
    ops = []
    i = 0
    while i < len(calculation):
        c = calculation[i]
        if c == " ":
            i += 1
            continue
        elif c.isdigit():
            num = int(c)
            while i < len(calculation) - 1 and calculation[i + 1].isdigit():
                num = num * 10 + int(calculation[i + 1])
                i += 1
            nums.append(num)
        elif c == "(":
            ops.append(c)
        elif c == ")":
            while ops[-1] != "(":
                nums.append(basic_ops(ops.pop(), nums.pop(), nums.pop()))
            ops.pop()
        elif c in {"+", "*"}:
            while len(ops) > 0 and ops[-1] in {"+", "*"}:
                nums.append(basic_ops(ops.pop(), nums.pop(), nums.pop()))
            ops.append(c)
        i += 1
    while ops:
        nums.append(basic_ops(ops.pop(), nums.pop(), nums.pop()))
    return nums[0]


def get_sum(calculations):
    res = 0
    for calculation in calculations:
        res += evaluate(calculation)
    return res

def evaluate_plus(calculation):
    nums = []
    ops = []
    i = 0
    while i < len(calculation):
        c = calculation[i]
        if c == " ":
            i += 1
            continue
        elif c.isdigit():
            num = int(c)
            while i < len(calculation) - 1 and calculation[i + 1].isdigit():
                num = num * 10 + int(calculation[i + 1])
                i += 1
            nums.append(num)
        elif c == "(":
            ops.append(c)
        elif c == ")":
            while ops[-1] != "(":
                nums.append(basic_ops(ops.pop(), nums.pop(), nums.pop()))
            ops.pop()
        elif c in {"+", "*"}:
            while len(ops) > 0 and precedence(c, ops[-1]) and ops[-1] in {"+", "*"}:
                nums.append(basic_ops(ops.pop(), nums.pop(), nums.pop()))
            ops.append(c)
        i += 1
    while ops:
        nums.append(basic_ops(ops.pop(), nums.pop(), nums.pop()))
    return nums[0]

def precedence(current_ops, op_from_ops):
    if current_ops == "+" and op_from_ops == "*":
        return False
    return True

def get_sum_plus(calculations):
    res = 0
    for calculation in calculations:
        res += evaluate_plus(calculation)
    return res

if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        calculations = f.read().splitlines()

    print("Part 1: ", get_sum(calculations))
    print("Part 2: ", get_sum_plus(calculations))