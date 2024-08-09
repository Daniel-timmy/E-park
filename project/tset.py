# import time
# days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thur", "Fri"]


# idx = days.index("Fri")
# i = (idx + 7) % len(days)
# print( days[idx:] + days[i+1:])
# timestamp = time.time()
# current_date = time.ctime(timestamp)
# cd = current_date.split(' ')
# day = list(cd)

# hour = day[4].split(':')[0]
# idx = days.index(day[0])
# idx =  (idx) % len(days)
# print(f'idx {idx}')
# days[:] = days[idx:] + days[:idx]
# print(days)
# print(hour)
# print(day[0])
# # hour = [i for i in range(0, 24)]
# # hours = [[i for i in range(0, 24)]] * 7
# # hours[0] = [i for i in range(6, 24)]
# # print(hours)

# dct = {'e': 1, 'r': 3}
# for f in dct.values():
#     print(f)

# from datetime import datetime, timedelta
# print(datetime.now().day)

# lst = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
# i = 8 % len(lst)
# idx = 5
# d = 3
# l = 7
# print(lst[idx:] + lst[:d-(l-idx)])
# print(d-(l-idx))
# # Step 2: Example datetime object
# original_datetime = datetime.now()

# # Step 3: Number of days to add
# days_to_add = 0

# # Step 4: Create a timedelta object
# delta = timedelta(days=days_to_add)

# # Step 5: Add the timedelta to the original datetime
# new_datetime = original_datetime + delta

# # Step 6: The result
# print("Original datetime:", original_datetime)
# print("New datetime:", new_datetime)
# def findMaxAverage( nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: float
#     """
#     mx = 0
#     for i in range(len(nums)):
#         if i + k > len(nums):
#             break
#         lsum = sum(nums[i: i+k])
#         mx = max(mx, lsum)
#     return round(mx/k, 5)
# print(findMaxAverage([1,12,-5,-6,50,3],4))
# def amount(duration, surge=1):
#     """"""
   
#     return duration * 500 * 24 * surge
# amt = amount(1, 1)
# print(amt)

# def minReorder(n, connections):
#     """
#     :type n: int
#     :type connections: List[List[int]]
#     :rtype: int
#     """
#     seen = set()
#     def dfs(connect, cn):
#         if connect[0] == 0:
#             connect[0], connect[1] = connect[1], connect[0]
#             seen.add(connect[1])
#             seen.add(connect[0]) 
#             print('hgcxfv nb')
#             cn += 1
#             print(f'cn {cn}')
#             return 2
#             dfs(connections[connect[0]], cnt)
#         elif connect[0] in seen:
#             connect[0], connect[1] = connect[1], connect[0]
#             seen.add(connect[1])
#             seen.add(connect[0]) 
#             cn += 1
#     cnt = 0
    
#     for connect in connections:
#         if connect[1] in seen:
#             seen.add(connect[0])
#             if connect[0] < n-1:
#                 dfs(connections[connect[0]], cnt)  
#                 print('1')
#         else:
#             print('ypuh')
#             dfs(connect, cnt)    
#     return cnt
# print(minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))



# def findPeakElement( nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     pr = float('inf')
#     pl = float('inf')
#     l = 0
#     r = len(nums) - 1
#     idx = l
#     while l <= r:
#         if nums[r] > pr and nums[r] > nums[r - 1]:
#             idx = r
#             break 
#         if nums[l] > pl and nums[l] > nums[l + 1]:
#             idx = l
#             break
#         if nums[r] > nums[l]:
#             idx = r
#         else:
#             idx = l
#         pr = nums[r]
#         pl = nums[l]
#         r -= 1
#         l += 1
    
#     return idx
# print(findPeakElement([1,2,1]))

# st1 = {'a', 'b', 'c', 'd'}
# st2 = {'a', 'b', 'c', 'e'}
# print(st1 - st2)
# print(st1.difference(st2))

# d = {}

# d['a'] = 2
# if 'b' in d:
#     d['b'] += 1
#     print(d)
# else:
#     d['b'] = 1
# #     print(d)

# import math
# print(math.ceil(3/2))

# def reverseVowels(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     dct = {}
#     vowels = {'a', 'u', 'o', 'i', 'e', 'A', 'E', 'I', 'O', 'U'}
#     s = list(s)
#     for c in range(len(s)):
#         if s[c] in vowels:
#             dct[c] = s[c]
#     val = dct.values()
#     print(val)
#     val = list(val)
#     print(type(val))
#     # return ''.join(val)
#     for i in dct.keys():
#         v = val.pop()
#         s[i] = v
#     return ''.join(s)

# print(reverseVowels('race a car'))
# def canJump( nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """
#     jmp = len(nums)
#     steps = nums[0]
#     count = 0
#     if len(nums) == 1:
#         return True
#     for i in range(len(nums)):
#         if nums[i] > steps:
#             steps = nums[i]
#         if steps > 0:
#             count += 1
#             steps -= 1
#         elif steps == 0 and count < jmp:
#             return False
#     return count

# print(canJump([2,3,0,1,4]))


# def canCompleteCircuit(gas, cost):
#     """
#     :type gas: List[int]
#     :type cost: List[int]
#     :rtype: int
#     """
#     for i in range(len(gas)):
#         print(f'gas[{i}] {gas[i]}')
#         # if i == 2:
#         #     continue
#         tank = gas[i]
#         idx = i
#         while True:
#             if tank <= 0:
#                 break
#             idx = (idx + 1 ) % len(gas)
#             tmp = gas[idx] - cost[idx-1]
#             tank = tank + tmp
            
#             if idx == i and tank > 0:
#                 print(f'{tank}')
#                 return i
#     return -1
# print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
# lst = [5,4,2,1,8,4,1,8]
# n = len(lst)
# print(n/2)
# h = int(n/2)
# lst1 = lst[:h]
# lst2 = lst[h:]
# lst2.reverse()
# mx = 0
# for a, b in zip(lst1, lst2):
#     mx = max(mx, a+b)
# print(mx)
# class SmallestInfiniteSet(object):

#     def __init__(self):
#         self.sSet = set(list(range(1, 10001)))
#         self.smallest = 1
        

#     def popSmallest(self):
#         """
#         :rtype: int
#         """
#         mn = min(self.sSet)
#         self.sSet.remove(mn)
#         return mn

#     def addBack(self, num):
#         """
#         :type num: int
#         :rtype: None
#         """
#         self.sSet.add(num)
#         # if num in self.sSet:
#         #     return
#         # if num < self.smallest:
#         #     lst = list(self.sSet)
#         #     lst.insert(0, num)
#         #     self.smallest = num
#         #     self.sSet = set(lst) 
#         # else:
#         #     lst = list(self.sSet)
#         #     for i in range(len(lst)):
#         #         if lst[i] > self.smallest:
#         #             lst.insert(i, num)
#         #             self.sSet = set(lst)

from datetime import datetime, timedelta
original_datetime = datetime.now()
delta = timedelta(days=0)
sTime = original_datetime + delta
formatted_sTime = sTime.strftime("%b %d, %Y %H:%M:%S")
print(formatted_sTime)


# def letterCombinations(digits):
#     """
#     :type digits: str
#     :rtype: List[str]
#     """
#     if not digits:
#         return []
#     ltr = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl",
#      "6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
#     output = []
#     def backtrack(current, index):
#         print(f'index {index}')
#         if index == len(digits):
#             output.append(current)
#             return
        
#         print(f'current {current}')
#         d = digits[index]
#         letters = ltr[d]
#         for l in letters:
        
#             print(f'current {current}')
#             backtrack(current + l, index + 1)
    
#     backtrack("", 0)
#     return output
# print(letterCombinations("23"))


# def combinationSum3( k, n):
#     """
#     :type k: int
#     :type n: int
#     :rtype: List[List[int]]
#     """
#     nums = [1,2,3,4,5,6,7,8,9]
#     output = []
#     def backtrack(lst, index):
#         if len(lst) == k:
#             if sum(lst) == n:
#                 output.append(lst)
#                 # lst.pop()
#                 print(f'lst {lst}')
#                 return
#             elif sum(lst) < n:
#                 print(f'lst {lst}')
#                 lst.pop()
#             else: 
#                 return
#         lst.append(nums[index])
#         for num in nums[index:]:
#             backtrack(lst, index+1)
#             lst.pop()
#     backtrack([], 0)
#     return output

# print(combinationSum3(3, 7))


# class User(Document):  
    
#     # assign a collection
#     meta = {"collection": "my_users"}    
#     username = fields.StringField(required=True)
#     profile_image = fields.ImageField(thumbnail_size=(150,150, False))
    
# # create a user, upload image, store the user into database
# conny = User(username="conny")
# my_image = open('static/img/cat.jpg', 'rb')
# conny.profile_image.replace(my_image, filename="conny.jpg")
# conny.save()

# # retrieve image
# from IPython.display import Image
# user = User.objects(username="conny").first()
# ## show image
# Image(user.profile_image.read())


# ## Replace the image
# my_image = open('static/img/cat2.jpg', 'rb')
# user.profile_image.replace(my_image)
# user.save()

# ## show image
# Image(user.profile_image.read())

# import string

# alphanumeric_set = set(string.ascii_lowercase + string.digits)
# print(alphanumeric_set)
# print(len(alphanumeric_set))
# s = 'a1b2c3AYUHJK'
# print(s.is)
# ch = [' '] * 3
# matrix = [ch] * 5
# print(matrix)

# l = ['fgfhj','fghj', 'djpd']
# print(" ".join(l))


# def convert(s, numRows):
#     """
#     :type s: str
#     :type numRows: int
#     :rtype: str
#     """
#     r = 0
#     c = 0
#     cnt = 0
#     output = []
#     matrix = [[] for _ in range(numRows)]
#     if numRows == 1:
#         return s
    
#     while cnt <= len(s)-1:
#         print(r)
#         while r < numRows and cnt < len(s):

#             matrix[r].append(s[cnt])
#             print(matrix)
#             r += 1
#             cnt += 1
#             # handles the straights
#         else:
#             r = numRows -1
#         while r > 0 and cnt < len(s):
#             # handles the slant
#             c += 1
#             r -= 1
#             matrix[r].append(s[cnt])
#             cnt += 1
#         else:
#             r += 1
            
#     for lst in matrix:
#         for l in lst:
#             if l.isalpha():
#                 output.append(l)
#     return "".join(output)
# print(convert("PAY", 2))
# "PINALSIGYAHRPI"
# "PAHNAPLSIIGYIR"

# def findSubstring(s, words):
#     """
#     :type s: str
#     :type words: List[str]
#     :rtype: List[int]
#     """
#     perm = set()
#     sol = []
#     res = []
#     idx = []
#     def backtrack():
#         # print(f'sol {sol}')
#         if len(sol) == len(words):
#             # print(sol)
#             perm.add("".join(sol))
#             return
        
#         for key, i in enumerate(words):
#             if key not in idx:
#                 idx.append(key)
#                 sol.append(i)
#                 backtrack()
#                 sol.pop()
#                 idx.pop()
#     backtrack()
#     print(perm)
                
#     ln = len(words[0]) * len(words)
#     for i in range(0,len(s)):
#         print(f'i {i}')
#         print(f's[i:ln] {s[i:ln]}')
#         if s[i:ln] in perm:
#             res.append(i)
#         ln += 1
#     return res
# # print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
# print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
# print(findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))


# l = [1,3,5,2,4,8,6,7]
# l2 = ['e','r','t','y','u','i','o','p']
# re = l + l2
# print(re)
# def idiot(X, Y, S):
#     sol = [0] * len(S)
#     if len(Y) == 0:
#         return sol
#     for i in range(len(S)):
#         for j in range(len(Y)):
#             if abs(X[i]-Y[j]) <= S[i]:
#                 sol[i] += 1

#     return sol

# st = {1,3,5,7,23,4,132}
# st2 = {1,2,3,132}
# print(st.intersection(st2))

# mat = [[1,3,2], [3,3,4], [7,9,0]]

# print(mat[:,1])
import time
print(datetime.now().month)
timestamp = time.time()
current_date = time.ctime(timestamp)
current_date = current_date.split(' ')
day = list(current_date)
print(day)