def kthCharWhichAppearedOnce(k,strs):
    """
    [2] 脸滚键盘 hashtable
    输入参数
    ----------- 
    k:第k个只出现一遍的字符
    strs:待统计的字符串
    """
    charsFreq = {}
    for s in strs:
        if s not in charsFreq:
            charsFreq[s] = 1
        elif charsFreq[s] == 1:
            charsFreq[s] = -1
    for s in strs:
        if k > 0 and charsFreq[s] == 1:
            k -= 1
        if k == 0 and charsFreq[s] == 1:
            return '[' +  s +']'
    return "Myon~"