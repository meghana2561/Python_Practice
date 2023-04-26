if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([score,name])
    lst_sorted = sorted(lst)
    min_scr = min(lst_sorted)
    new_lst = [l for l in lst if l[0]>min_scr[0]]
    sec_min = min(new_lst)
    res = [new[1] for new in new_lst if new[0]==sec_min[0]]
    res_s = sorted(res)
    for i in res_s:
        print(i)
