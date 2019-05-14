def getMinCoins(N):
    """
    [1] 扭蛋机 
    输入参数 N：int,最终需要扭出的扭蛋数
    """
    if N <= 2:
        return '2' if N == 1 else '3'
    dp = [1 for i in range(N+1)]
    dp[1],dp[2] = 1,2
    s = [None for i in range(N+1)]
    s[1],s[2] = '2','3'
    for i in range(3,N+1):
        if (i-1)%2 == 0 and (i-1)//2 >= 1:
            # 22娘
            dp[i] = dp[(i-1)//2] + 1
            s[i] = '2'
        elif (i-2)%2 == 0 and (i-2)//2 >= 1:
            # 33娘
            dp[i] = dp[(i-2)//2] + 1
            s[i] = '3'
    cur = N
    cache = []
    while cur > 0:
        print(cur)
        # 寻找前一个
        cache.append(s[cur])
        cur = (cur - 1)//2 if s[cur] == '2' else (cur-2)//2
    print(cur)
    cache.reverse()
    return "".join(cache)
    # 似乎要o(1)空间复杂度，总是内存超