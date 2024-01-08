def robber(arr, index = 0):
    if index >= len(arr):
        return 0 
    firts = arr[index] + robber(arr, index + 2)
    sec = robber(arr, index + 1)
    return max(firts, sec)


# arr = [60,30,5,40,30,70,80]
# print(robber(arr))


def strin(s1, s2, index1, index2):
    if index1 >= len(s1):
        return len(s2) - index2 
    elif index2 >= len(s2):
        return len(s1) - index1 
    elif s1[index1] == s2[index2]:
        return strin(s1, s2, index1 + 1, index2 + 1)
    else:
        delete = 1 + strin(s1, s2, index1, index2 + 1)
        inse = 1 + strin(s1, s2, index1+1, index2)
        repl = 1 + strin(s1, s2, index1+1, index2 + 1)

        return min(delete, inse, repl) 
    
# print(strin("arnnil", "aknil", 0, 0))



def number_factor(n, dic = {}):
    if n in (0,1,2):
        return 1 
    if n == 3:
        return 2 
    if n not in dic.keys():
        res1 = number_factor(n-1 ,dic)
        res2 = number_factor(n-3, dic)
        res3 = number_factor(n-4, dic)
        dic[n] = res1 + res2 + res3
        return dic[n]
    return dic[n]

def number_fact(n, base):
    result = []
    res = []
    for i in range(len(base)):
        js = []
        for j in range(n):
            rs = [base[i]]
            for h in range(j):
                rs.append(base[i]) 
            js.append(rs)
        res += js
        
        for a in js:
            jjss = []
            for b in range(i+1, len(base)):
                
                for c in range(1, len(a)):
                    jjs = a.copy()
                    for d in range(c):
                        jjs[d] = base[b]
                    jjss.append(jjs)
            for e in jjss:
                res.append(e)
    for i in res:
        if sum(i) == n:
            
            if i not in result:
                result.append(i)
                if i[::-1] not in result:
                    result.append(i[::-1])
    [print(i) for i in result]

number_fact(7, [1,2,3])

def house_robber(ls, current = 0, dic = {}):

    if current >=len(ls):
        return 0
    if current not in dic.keys():
        took_first = ls[current] + house_robber(ls, current + 2, dic)
        skip_first = house_robber(ls, current + 1, dic)
        dic[current] = max(took_first, skip_first)
        return dic[current]
    return dic[current]

print(house_robber([5,8,7,8,9,10]))



def LCSLength(S1, S2, lenS1, lenS2, dic={}):
    if lenS1 == len(S1) or lenS2 == len(S2):
        return ""

    if (lenS1, lenS2) in dic:
        return dic[(lenS1, lenS2)]

    if S1[lenS1] == S2[lenS2]:
        result = S1[lenS1] + LCSLength(S1, S2, lenS1 + 1, lenS2 + 1, dic)
    else:
        option1 = LCSLength(S1, S2, lenS1 + 1, lenS2, dic)
        option2 = LCSLength(S1, S2, lenS1, lenS2 + 1, dic)
        result = max(option1, option2, key=len)

        dic[(lenS1, lenS2)] = result
        return result
    return result

S1 = "ABCBDAB"
S2 = "BDCABA"
result = LCSLength(S1, S2, 0, 0)

print(result)


def check_sum(ls, s, index = 0, dic = []):
    if index == len(ls):
        return False
    if ls[index] < s:
        k = s - ls[index]
        if k in ls[index+1:]:
            return True 
        else:
            res1 = check_sum(ls, k, index+1, dic)
            res2 = check_sum(ls, s, index+1, dic)
            if res1 == True or res2 == True:
                dic.append(ls[index])
                dic.append(k)
    else:
        check_sum(ls, s, index+1, dic)
    return dic 

ls = [3, 34, 4, 12, 5, 2]
s = 9
res = check_sum(ls, s)
        







def lps(s, start, end, dic = {}):
    if start == end:
        return s[start] 
    if start > end:
        return ""
    if (start, end) in dic.keys():
        return dic[(start, end)]
    elif s[start] == s[end]:
        dic[(start, end)] = s[start] + lps(s, start+1, end-1) + s[end]
        return dic[(start, end)]
    else:
        option2 = lps(s, start+1, end)
        option3 = lps(s, start, end-1)
        result = max(option2, option3, key = len)
        dic[(start, end)] = result 
        
    return dic[(start, end)]
        




k = lps("ABABCBA", 0, 6)
print(k)


