def computeExpression(self,expr):
    """
    [3] 简单表达式计算 - 双栈
    输入参数
    ------
    expr: 待计算的表达式(str)
    """
    numStk,operStk = [],[]

    tmp,isPositive = 0,1
    for s in expr:
        print(numStk,operStk)
        if s.isdigit():
            tmp = tmp*10 + int(s)
        else:
            numStk.append(isPositive*tmp)
            tmp = 0
            if s == '-':
                isPositive = -1
            else:
                isPositive = 1
            # operstk有没有符号
            if len(operStk) != 0:
                oper = operStk.pop()
                numStk.append(numStk.pop()*numStk.pop())
            if s == '*':
                operStk.append(s)
    # 最后一个数字
    if len(operStk) == 1:
        numStk.append(tmp*numStk.pop())
    else:
        numStk.append(tmp*isPositive)
    return sum(numStk)