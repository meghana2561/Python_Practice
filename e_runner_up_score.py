if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    m = sorted(arr)
    while(m[-1]==m[-2]):
        m.pop(-1)
    print(m[-2])
