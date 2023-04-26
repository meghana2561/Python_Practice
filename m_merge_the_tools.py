def merge_the_tools(string, k):
    # your code goes here
    l = []
    for i in range(0,len(string),k):
        m = string[i:i+k]
        exists = []
        for j in range(len(m)):
            if m[j] not in exists:
                exists.append(m[j])
        print("".join(exists))
