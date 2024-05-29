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