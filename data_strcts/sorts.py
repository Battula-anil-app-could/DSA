import math
class Sort:
    def __init__(self, items = []):
        self.values = items
    
    def bouble_sort(self):
        ls = self.values.copy() 
        for i in range(len(ls)):
            for j in range(len(ls)-1):
                if ls[j] > ls[j+1]:
                    ls[j], ls[j+1] = ls[j+1], ls[j]
        print(ls)
    
    def selection_sort(self):
        ls = self.values.copy()

        for i in range(len(ls)):
            for j in range(i+1, len(ls)):
                if ls[i] > ls[j]:
                    ls[i], ls[j] = ls[j], ls[i]
        print(ls)
    def insertion_sort(self, ls = []):
        if ls == []:
            ls = self.values.copy()
        for i in range(len(ls)):
            j = i-1 
            if j >= 0:
                for k in range(j+1):
                    if ls[k] > ls[i]:
                        ls[k], ls[i] = ls[i], ls[k]
        if len(ls) == len(self.values):
            print(ls)
        return ls 
    
    def bucket_sort(self):
        ls = self.values.copy()
        number_of_buckets = round(math.sqrt(max(self.values)))
        buckets = [[] for i in range(number_of_buckets)] 
        for i in ls:
            bucket_num = math.ceil((i * number_of_buckets) / max(ls))
            buckets[bucket_num-1].append(i) 
        res = []
        for i in range(len(buckets)):
            res += self.insertion_sort(buckets[i])
        print(res)
    
    def merge(self, left, right):
        merged = []
        i = j = 0 

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1 
            else:
                merged.append(right[j])
                j += 1 
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def merge_sort(self, ls = None):
         
        if ls is None:
            ls = self.values.copy()

        if len(ls) <= 1:
            return ls 
        l = 0 
        r = len(ls)
        m = r // 2 
        left = self.merge_sort(ls[:m])
        right = self.merge_sort(ls[m:])
        return self.merge(left, right)

    def piovt(self,customList, low, high):
        i = low - 1
        pivot = customList[high]
        for j in range(low,high):
            if customList[j] <= pivot:
                i += 1
                customList[i], customList[j] = customList[j], customList[i]
        customList[i+1], customList[high] = customList[high], customList[i+1]
        return (i+1)
    
    def quick_sort(self, left, right, ls = None ):
        if ls == None:
            ls = self.values.copy()
            left= 0 
            right = len(ls)-1
        if left < right:
            piovt_index = self.piovt(ls, left, right)
            self.quick_sort(left, piovt_index-1, ls)
            self.quick_sort(piovt_index+1, right, ls)
        return ls



values = Sort([5,2,6,4,3,1,7,9,8])
values.bouble_sort()
values.selection_sort()
values.insertion_sort()
values.bucket_sort()
print(values.merge_sort())