def maxEncounteredPersonNum(n,i,rels):
    """
    [4] 小A最多会新认识的多少人 - 图/计算可达矩阵
    ------
    输入参数
    n:总人数
    i:小明的序号
    rels:两两认识的关系
    """
    dist = [[0 for i in range(n)] for j in range(n)]
    # 初始化邻接矩阵dist
    for r in rels:
        dist[r[0]][r[1]] = 1
        dist[r[1]][r[0]] = 1
    initFriendsNum = sum(dist[i])

    # 传递闭包算法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = dist[i][j] or (dist[i][k] and dist[k][j])
    return sum(dist[i]) - initFriendsNum - 1