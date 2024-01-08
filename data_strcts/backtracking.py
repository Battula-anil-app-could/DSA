
def solve(ip, index, op =[]):
    if index < 0:
        if op:
            print("".join(op))
        return 
    solve(ip,index -1, op)
    op.append(ip[index])
    solve(ip,index-1, op)
    op.pop() # it is back track line

# ip = "abc"
# solve(ip, len(ip)-1)


def paths_to_home(rows, cols, x,y,count = 0, memo = [], path = []):
    if x == rows or y == cols:
        return 0
    if x == rows-1 and y == cols-1:
        memo.append(path)
        path = []
        return 1
    paths_to_home(rows, cols, x+1, y, count, memo, path+["D"])
    paths_to_home(rows, cols, x, y+1, count, memo, path+["R"])
    return memo
#[print(" ".join(i)) for i in paths_to_home(3,3,0,0,0)]


def get_permutations(s, index = 0, memo = []):
    if index == len(s)-1:
        if s not in memo:
            memo.append("".join(s))
        return s
    for i in range(index, len(s)):
        s[i],s[index] = s[index], s[i]
        get_permutations(s, index+1, memo)
        s[i],s[index] = s[index], s[i] # it is back track line
    return memo
        

s = "3214"
s = list(s)
#print(get_permutations(s))


def rat_to_home(table, rows, cols, x,y,count = 0, memo = [], path = []):
    if x == rows or y == cols:
        return 
    if x == rows-1 and y == cols-1:
        memo.append(path)
        path = []
        return memo
    if table[x][y] == 1:
        down = rat_to_home(table, rows, cols, x+1, y, count, memo, path+["D"])
        right = rat_to_home(table, rows, cols, x, y+1, count, memo, path+["R"])

        if down:
            return down 
        else:
            return right
        
    
# n = int(input()) #4
# table = [list(map(int, input().split())) for i in range(n)] #[[1,0,0,0],[1,1,0,0],[1,1,0,1],[0,1,1,1]]
#[print(" ".join(i)) for i in rat_to_home(table, n,n,0,0,0)]




def rat_to_home_best_way(reffernce, table, rows, cols, x,y,count = 0, memo = [], path = []):
    if x == rows or y == cols:
        return 
    if x == rows-1 and y == cols-1:
        reffernce[x][y] = 1
        memo.append(path)
        path = []
        return memo
    if table[x][y] == 1:
        reffernce[x][y] = 1
        down = rat_to_home_best_way(reffernce, table, rows, cols, x+1, y, count, memo, path+["D"])
        if down:
            return reffernce
        right = rat_to_home_best_way(reffernce, table, rows, cols, x, y+1, count, memo, path+["R"])
        if right:
            return reffernce 
        reffernce[x][y] = 0 # it is back track line
        
    
# n = int(input())
# table = [list(map(int, input().split())) for i in range(n)]
# reffernce = [[0 for j in range(n)] for i in range(n)]
#[print(i) for i in rat_to_home_best_way(reffernce, table, n,n,0,0,0)]


def get_sum_of_k(arr, k, path = [], memo={}, index = 0):
    if index == len(arr):
        if sum(path) == k:
            memo[tuple(path)] = k
            return memo 
        return memo
    path.append(arr[index])
    get_sum_of_k(arr, k, path, memo, index+1)
    path.pop() # it is back track line
    get_sum_of_k(arr, k, path, memo, index+1)
    return memo
        

# arr = [10,1,2,7,6,1,5]
# k = 8
# [print(i) for i in get_sum_of_k(arr, k).keys()]


def palindrome_partitioning(s, index=0, memo=None, path=None):
    if memo is None:
        memo = []
    if path is None:
        path = []

    if index >= len(s):
        memo.append(path.copy())
        return

    for i in range(index+1, len(s)+1):
        sub = s[index: i]
        if sub == sub[::-1]:
            path.append(sub)
            palindrome_partitioning(s, i, memo, path)
            # back track
            path.pop()
    return memo


# s = "aab"
# print(palindrome_partitioning(s))

def min_palindrome_cut(s, n, index = 0, memo = None, path = None):
    if memo is None:
        memo = []
    if path is None:
        path = [] 
    
    if index >= n:
        memo.append(path.copy())
        return 
    
    for end in range(index+1, n+1):
        sub = s[index: end]
        if sub == sub[::-1]:
            path.append(sub)
            min_palindrome_cut(s, n, end, memo, path)
            path.remove(sub)
    return min(list(map(len,memo)))-1

# s = "rkbaabfl"
# print(min_palindrome_cut(s, len(s)))



def mix_water(x,y, x1, y1, memo=[], path = []):
    if x <= 0 or y <= 0:
        return 
    if x == y:
        memo += path.copy()
        return memo 
    if x > y:
        x = x - y1
        y = y+y1
    elif y > x:
        y = y - x1 
        x = x+x1
    path.append((x,y))
    mix_water(x, y, x1, y1, memo, path)
    #path.pop() # back track
    return memo 

# x = 10
# y = 6
# res = mix_water(x,y, x,y) 
# if res:
#     [print("steps: ", i) for i in res]
# else:
#     print("unable to mix water with this bottles")





def get_chain_pair(s, index = 0, memo= [], path = []):
    if index == len(s):
        memo += path.copy()
        return  
    if index < len(s):
        if path[-1][1] < s[index][0]:
            path.append(s[index]) 
        get_chain_pair(s, index+1, memo, path)
        if s[index] in path:
            path.remove(s[index]) # back track
        return memo 
        
    

def chain_pairs(s):
    k = []
    for i in range(len(s)):
        res = get_chain_pair(s,0, [], [s[i]])
        if len(res) > 1:
            k.append(res)
    return k
s = [[5, 24], [39, 40], [15, 28], [27, 40], [50, 90]]
s.sort(key = lambda x: x[0])
res = chain_pairs(s)
#[print(i) for i in list(filter(lambda x: len(x) == max(list(map(len, res))), res))]


def is_safe(n, row, col, grid):
    col_check = row
    while col_check >= 0:
        if grid[col_check][col] == "Q":
            return False 
        col_check -= 1
    right_cor_row = row -1
    right_cor_col = col -1
    while right_cor_col >= 0 and right_cor_row >= 0:
        if grid[right_cor_row][right_cor_col] == "Q":
            return False
        right_cor_row -= 1 
        right_cor_col -= 1
    left_cor_row = row -1 
    left_cor_col = col +1 
    while left_cor_row >= 0 and left_cor_col < n:
        if grid[left_cor_row][left_cor_col] == "Q":
            return False
        left_cor_row -= 1 
        left_cor_col += 1
    return True
    

def nqueens(n, grid, row = 0, memo = []):
    if row >= n:
        memo.append([row[:] for row in grid])
        return memo
    for col in range(n):
        if is_safe(n, row, col, grid):
            grid[row][col] = "Q"
            nqueens(n, grid, row+1, memo)
            grid[row][col] = "*" #back tracking line
    return memo                

# n = 4
# chess_board = [["*" for _ in range(n)] for _ in range(n)]
# res = nqueens(n, chess_board)
# for i in res:
#     for j in i:
#         print("  ".join(j))
#     print("----------------------------------------------------------------------")


def search_word(board, word, n, row = 0, col = 0, memo=[], path = None, storage = []):
    if path is None:
        path = ""
    
    
    if row >= n or col >= len(board[0]) or row < 0 or col < 0:
        return 
    if board[row][col] == "V":
        return
    if path == word:
        if memo not in storage:
            storage.append(memo.copy())
        return
    letter = board[row][col]
    board[row][col] = "V"
    memo.append((row, col))
    search_word(board, word, n, row, col+1, memo, path + letter)
    search_word(board, word, n, row, col-1, memo, path + letter)
    search_word(board, word, n, row+1, col, memo, path + letter)
    search_word(board, word, n, row-1, col, memo, path + letter)
    board[row][col] = letter #back tracking line
    memo.remove((row, col)) #back tracking line
    return storage
        
    

# board = [["a","l","e","b"], ["p","p","o","a"], ["k", "l", "e","t"]]
# word = "apple"
# n = len(board)
# [print(i) for i in search_word(board, word,n)]



def add_operator(s, target, index = 0 , memo = None, path = None):
    if memo is None:
        memo = []
    if path is None:
        path = []
    if index >= len(s):
        if sum(path) == target:
            path_s = "".join(list(map(str, path)))
            new_path = "".join([path_s[i] + "+" for i in range(len(path_s)-1)]) + path_s[-1]
            memo.append([new_path, target])
        return 
    path.append(int(s[index]))
    add_operator(s, target, index+1, memo, path)
    path.pop()
    add_operator(s, target, index+1, memo, path)
    return memo
# s = "1234"
# n = 6
# print(add_operator(s, n))


def number_of_combinations_with_self(s, target, index = 0 , memo = None, path = None):
    if memo is None:
        memo = []
    if path is None:
        path = []
    if sum(path) > target:
        return
    if path in memo or path[::-1] in memo:
        return
    if index >= len(s):
        return 
    if sum(path) == target:
        if path not in memo:
            memo.append(path.copy())
        if path[::-1] not in memo:
            memo.append(path[::-1].copy())
        return 
    
    path.append(int(s[index]))
    number_of_combinations_with_self(s, target, index+1, memo, path)
    path.pop()
    number_of_combinations_with_self(s, target, index+1, memo, path)
    return memo
# s = "243"
# n = 6
# s = "".join(["".join([i for _ in range(n)]) for i in s])
# print(number_of_combinations_with_self(s, n))



def is_subset(path, s):
    index = s.index(path[0])
    for i in path:
        if index < len(s):
            if i in s[index:]:
                index += 1 
            else:
                return False
        else:
            return False
    return True

def get_all_subsets(s, index = 0, memo = [], path = []):
    if index >= len(s):
        return 
    if path:
        if path not in memo:
            if is_subset(path, s):
                memo.append(path.copy()) 
    for i in range(index, len(s)):
        path.append(s[i])
        get_all_subsets(s, index+1, memo, path)
        path.pop()
    memo.sort(key = lambda x: len(x))
    return memo 

# s = [1,2,3]
# print(get_all_subsets(s,0, [s]))




def is_make_word(word, table, row = 0, col = 0, letter = 0 , memo = None, path = None):
    if memo is None:
        memo = []
    if path is None:
        path = []
    if "".join(path) == word:
        if word not in memo:
            memo.append(True)
        return
    if letter >= len(word):
        memo.append(True)
    if row >= len(table) or col >= len(table) or row < 0 or col < 0:
        return 
    if table[row][col] == "v":
        return
    if table[row][col] == word[letter]:
        table[row][col] = "v"
        path.append(word[letter])
        is_make_word(word, table, row, col+1, letter+1, memo, path)
        is_make_word(word, table, row, col-1, letter+1, memo, path)
        is_make_word(word, table, row+1, col, letter+1, memo, path)
        is_make_word(word, table, row-1, col, letter+1, memo, path)
        
        is_make_word(word, table, row-1, col-1, letter+1, memo, path)
        is_make_word(word, table, row-1, col+1, letter+1, memo, path)
        is_make_word(word, table, row+1, col+1, letter+1, memo, path)
        is_make_word(word, table, row+1, col-1, letter+1, memo, path)
        path.remove(word[letter])
        table[row][col] = word[letter]
    return memo


# word = "quiz"
# table = [["g", "i", "z"], ["u", "e", "k"], ["q", "s", "e"]]
# print(is_make_word(word, table))


import copy 

def knightes_tour(chess_board, n, row=0, col=0, visited=0,  memo = []):
    if visited == (n * n) :
        if not memo:
            memo += copy.deepcopy(chess_board)
        return memo

    if row >= n or col >= n or row < 0 or col < 0:
        return memo

    if chess_board[row][col] != "N":
        return memo

    chess_board[row][col] = visited
    visited += 1
    if knightes_tour(chess_board, n, row + 2, col + 1, visited):
        return memo
    if knightes_tour(chess_board, n, row + 1, col + 2, visited):
        return memo
    if knightes_tour(chess_board, n, row - 1, col +2, visited):
        return memo
    if knightes_tour(chess_board, n, row - 2, col + 1, visited):
        return memo
    if knightes_tour(chess_board, n, row - 2, col -1, visited):
        return memo
    if knightes_tour(chess_board, n, row - 1, col - 2, visited):
        return memo
    if knightes_tour(chess_board, n, row + 1, col - 2, visited):
        return memo
    if knightes_tour(chess_board, n, row + 2, col - 1, visited):
        return memo
    chess_board[row][col] = "N"
    visited -= 1

    return memo

n = 9
chess_board = [["N" for _ in range(n)] for _ in range(n)]
result = knightes_tour(chess_board, n)
if result:
    [print(i) for i in result] 
else:
    print(f"knight not able to tour {n} X {n} chess board")