if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        ele = input().split(" ")
        if ele[0] == 'insert':
            lst.insert(int(ele[1]),int(ele[2]))
        elif ele[0] == 'append':
            lst.append(int(ele[1]))
        elif ele[0] == 'print':
            print(lst)
        elif ele[0] == 'remove':
            lst.remove(int(ele[1]))
        elif ele[0] == 'sort':
            lst.sort()
        elif ele[0]=='reverse':
            lst.reverse()
        elif ele[0] == 'pop':
            lst.pop()
