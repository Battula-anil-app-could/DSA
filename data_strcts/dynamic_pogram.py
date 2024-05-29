# Problem Statement
# There are 
# N stones, numbered 
# 1,2,…,N. For each 
# i (
# 1≤i≤N), the height of Stone 
# i is 
# h 
# i
# ​
#  .

# There is a frog who is initially on Stone 
# 1. He will repeat the following action some number of times to reach Stone 
# N:

# If the frog is currently on Stone 
# i, jump to Stone 
# i+1 or Stone 
# i+2. Here, a cost of 
# ∣h 
# i
# ​
#  −h 
# j
# ​
#  ∣ is incurred, where 
# j is the stone to land on.
# Find the minimum possible total cost incurred before the frog reaches Stone 
# N.

#frog 1 optional method 

def minimum_frog_jump(n, ls, i = 0, memo = [], cost = 0):

    if i == n-1:
        memo.append(cost)
        cost = 0 
        return memo
    if i +1 >= n:
        return 0
    if i + 2 >= n:
        minimum_frog_jump(n, ls, i + 1, memo, cost + abs(ls[i] - ls[i+1]))
        return 0

    minimum_frog_jump(n, ls, i + 2, memo, cost + abs(ls[i] - ls[i+2]))
    minimum_frog_jump(n, ls, i + 1, memo, cost + abs(ls[i] - ls[i+1]))
    return min(memo)

n = int(input("enter number of stons: "))
ls = list(map(int, input("enter values: ").split()))
res = minimum_frog_jump(n, ls)
print(res)

#frog 1 memo bottom up method 
def minimum_frog_jump(n, ls, memo = None):
    if memo is None:
        memo = [0 for i in range(n+1)]
    if n == 0:
        return 0
    minimum_frog_jump(n-1, ls, memo)
    cost = memo[n-1] + abs(ls[n-1]-ls[n])
    if n-2 >= 0:
        cost =  min(cost, memo[n-2] + abs(ls[n-2] - ls[n]))
    memo[n] = cost
    
    return memo[n]

n = int(input())
ls = list(map(int, input().split()))
res = minimum_frog_jump(n-1, ls)
print(res)

# Problem Statement
# There are 
# N stones, numbered 
# 1,2,…,N. For each 
# i (
# 1≤i≤N), the height of Stone 
# i is 
# h 
# i
# ​
#  .

# There is a frog who is initially on Stone 
# 1. He will repeat the following action some number of times to reach Stone 
# N:

# If the frog is currently on Stone 
# i, jump to one of the following: Stone 
# i+1,i+2,…,i+K. Here, a cost of 
# ∣h 
# i
# ​
#  −h 
# j
# ​
#  ∣ is incurred, where 
# j is the stone to land on.
# Find the minimum possible total cost incurred before the frog reaches Stone 
# N.
#frog2 k jumps 
def path(memo, ls,n, k):
    print(n)
    for i in range(1, k+1):
        if n-i >= 0:
            if memo[n] == memo[n-i] + abs(ls[n] - ls[n-i]):
                path(memo, ls, n-i, k)
                return
def minimum_frog_jump(n, k, ls, memo = None):
    if memo is None:
        memo = [0 for i in range(n+1)]
    if n == 0:
        memo[0] = 0
        return 0
    minimum_frog_jump(n-1,k, ls, memo)
    cost = 100000000000000000000000000000000000000000
    for i in range(1, k+1):
        if n-i >= 0:
            cost = min(cost, memo[n-i] + abs(ls[n] - ls[n-i]))
    memo[n] = cost
    return memo

n, k = list(map(int, input().split()))

ls = list(map(int, input().split()))
res = minimum_frog_jump(n-1, k, ls)
print(res)

path(res, ls, n-1, k)



# Problem Statement
# Taro's summer vacation starts tomorrow, and he has decided to make plans for it now.

# The vacation consists of 
# N days. For each 
# i (
# 1≤i≤N), Taro will choose one of the following activities and do it on the 
# i-th day:

# A: Swim in the sea. Gain 
# a 
# i
# ​
#   points of happiness.
# B: Catch bugs in the mountains. Gain 
# b 
# i
# ​
#   points of happiness.
# C: Do homework at home. Gain 
# c 
# i
# ​
#   points of happiness.
# As Taro gets bored easily, he cannot do the same activities for two or more consecutive days.

# Find the maximum possible total points of happiness that Taro gains.

# usied by tabulation 
def get_max_points_of_happy(n, activities, i, memo):
    max_points = 0
    
    for j in range(0, 3):
        if i != j:
            max_points = max(max_points, (memo[n-1][j] + activities[n][i]))
    return max_points

def do_activities(n, activities, memo = None):
    if memo is None:
        memo = [[0 for i in range(3)] for j in range(n+1)]
    if n == 0:
        memo[0] = activities[0].copy()
        return memo
    do_activities(n-1, activities, memo)
    for i in range(0, 3):
        memo[n][i] = get_max_points_of_happy(n, activities, i, memo)
    return memo

n = int(input())
activities = [list(map(int, input().split())) for i in range(n)]
res = do_activities(n-1, activities)
print(max(res[n-1]))