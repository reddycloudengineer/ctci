#1.16.4 - tic tac toe
#16.5 - Factorial Zeros
#16.6 - Smallest diff
# 16.10 - Living people
# 16.11 - diving board
# 16.15 - Master mind
# 16. 16 - Sub sort
# 16.17 - Contiguous Sequence
# 16.18 - Patter matching
# 16.19 - Pond sizes
# 16.20 - Cell phone name printing
# 16.21 - Sum swap
# 16. 22 - Langton's Ant
# 16. 24 - PairwithSum
# 16. 25 - LRU Cache
from amazonPractice import MakeNodes
def trailingZeroesSlow(n):
    """
    :type n: int
    :rtype: int
    """
    t=1
    c=0
    while(t<=n):
        s=t
        while(s>0 and s%5==0):
            c=c+1
            s=s/5
        t=t+1

    print('5 is repeated so many time so far ',c)



def trailingZerosFast(n):
    i=5
    c=0
    while(n>i):
       c=c+int(n/i)
       i=i*5
    return c


trailingZerosFast(1808548329)

def smallestDifference(n1,n2):
    pass


class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        d={}
        for i in range(1,53):
            d[i]=chr(96+i)
        print(d)


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        pass


# codec=Codec()
# codec.encode('')


def partionLabels(s):
    d={}
    for i in range(0,len(s)):
        if s[i] in d:
            d[s[i]][1]=i
        else:
            d[s[i]]=[i,i]

    t=[]

    start= d[s[0]][0]
    end= d[s[0]][1]
    print(d)
    for i in range(0,len(s)):
        current=s[i]
        currentStart=d[current][0]
        currentEnd=d[current][1]
        if currentStart>start and currentEnd>end:
            t.append(i)
            print('currentStart ',currentStart,'current End ',currentEnd,'start ',start,'end ',end)
            start=currentStart
            end=currentEnd
    print(t)

def optimalDiv(l,index):
    if index==len(l)-1:
        print(l[index])
        return [l[index]]
    moreSubsets=[]
    item=l[index]
    subsets=optimalDiv(l,index+1)
    print('subsets ',subsets)
    for each in subsets:
        t=[item]
        t.append(each)
        if t not in moreSubsets:
            moreSubsets.append(t)
        t=[item]
        t.extend(each)
        if t not in moreSubsets:
            moreSubsets.append(t)
        print('more subsets after adding ',moreSubsets)
    return moreSubsets


# print(optimalDiv(['a','b','c','d'],0))

l=[1,2,3,4,5,6,7]
head = MakeNodes.makeTreeNodes(l)
l2=[5,6,7]
l3=[]
def sumNodes(head,t):
    if not head:
        return 0
    s=head.data +sumNodes(head.right,t)+sumNodes(head.left,t)
    t.append(s)
    return s

t=[]
sumNodes(head,t)
print(t)


def findFrequentTreeSum(root):
    t=[]
    sumNodes(head,t)
    print(t)
    d={}
    for each in t:
        if each in d:
            d[each]=d[each]+1
        else:
            d[each]=1

    mx=0
    for each in d:
        if d[each]>mx:
            mx=d[each]

    m=[]
    for each in d:
        if d[each]==mx:
            m.append(each)
    return m



def isSubtree(s,t):
    pass

l=[1,2,3,4,5,6,7]
s = MakeNodes.makeTreeNodes(l)
l=[5,6,7]
t=MakeNodes.makeTreeNodes(l)

pairs=[[1,2], [2,3], [3,4]]
pairs=[[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
def findLongestChain(pairs):
    m=0
    for i in pairs:
        c=0
        for j in pairs:



findLongestChain(pairs)