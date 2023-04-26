def minion_game(string):
    # your code goes here
    k_score = 0
    s_score = 0
    for i in range(len(string)):
        if string[i] in ['A','E','I','O',"U"]:
            k_score = k_score + (len(string)-i)
        else:
            s_score = s_score + (len(string)-i)
    if k_score>s_score:
        print("Kevin",k_score)
    elif k_score<s_score:
        print("Stuart",s_score)
    else:
        print("Draw")
