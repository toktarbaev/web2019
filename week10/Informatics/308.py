def xor(x, y):
    if(x == 1 and y == 0) or (x == 0 and y == 1):
        return 1
    return 0


a = input().split()
print(xor(int(a[0]), int(a[1])))
