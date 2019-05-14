def isInternalIP(addr):
    addrArr = addr.split('.')
    # 127 10 172.16-31 192.168.0-255
    if addrArr[0] == '10':
        return 1
    elif addrArr[0] == '172' and int(addrArr[1]) >= 16 and int(addrArr[1]) < 32:
        return 1
    elif addrArr[0] == '192' and addrArr[1] == '168':
        return 1
    elif addrArr[0] == '127':
        return 1
    else:
        return 0

