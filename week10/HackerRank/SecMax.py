if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    res = -105
    for i in arr:
        if i != mx and i > res:
            res = i
    if res == -105:
        print('')
    else:
        print(res)