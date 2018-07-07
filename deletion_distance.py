def deletion_distance(s1, s2):
    cur = list(range(len(s2) + 1))
    prev = [0] * (len(s2) + 1)
    for i in range(len(s1)):
        cur, prev = prev, cur
        cur[0] = i + 1
        for j in range(len(s2)):
            # Substitution is same as two deletions
            sub = 0 if s1[i] == s2[j] else 2
            cur[j+1] = min(prev[j] + sub, cur[j] + 1, prev[j+1] + 1)

    return cur[-1]
