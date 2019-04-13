def count_substring(string, sub_string):
    l = len(sub_string)
    n = len(string)
    cnt = 0
    for i in range(0, n - l + 1):
        if string[i:i + l] == sub_string:
            cnt += 1
    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)