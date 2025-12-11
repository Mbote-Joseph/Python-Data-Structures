def judge_square_sum(n):
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if pow(i,2) + pow(j, 2) == n:
                return True
            else:
                return False
            