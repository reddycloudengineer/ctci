#8.1 triple steps

def tripleSteps(n):
    ways=0
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        ways=ways+tripleSteps(n-1)+tripleSteps(n-2)+tripleSteps(n-3)
    return ways

def tripleStepsMemo(n,m):
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m[n]>0:
        return m[n]
    else:
        m[n]=tripleStepsMemo(n-1,m)+tripleStepsMemo(n-2,m)+tripleStepsMemo(n-3,m)
    return m[n]

n=10
m=[-1]*(n+1)
# print(tripleStepsMemo(n,m))
# print(tripleSteps(25))



matrix=[[1,1,0],
        [1,0,0],
        [1,1,1]]

def getPath(matrix):
    if not matrix:
        return None
    else:
        return getPathHelper(matrix,len(matrix)-1,len(matrix[0])-1)

def getPathHelper(matrix,row,col,path):

    if row<0 or col<0:
        return False

    isatorigin= row==0 and col==0

    if isatorigin or getPathHelper(matrix,row-1,col,path) or getPathHelper(matrix,row,col-1,path):
        path.append([row,col])
        return True

    return False

def getPathMemo(matrix):
    if not matrix:
        return None
    else:
        return getPathMemoHelper(matrix,len(matrix)-1,len(matrix[0])-1,[],[])

def getPathMemoHelper(matrix,row,col,path,memo):
    if row<0 or col<0:
        return False

    if [row,col] in memo:
        return False

    isAtOrigin=row==0 and col==0

    if getPathMemoHelper(matrix,row-1,col,path,memo) or isAtOrigin or getPathMemoHelper(matrix,row,col-1,path,memo):

        path.append([row,col])
        return True

    memo.append([row,col])
    return False

a=[-40,-20,-1,1,2,3,5,7,9,12,13]

def magicIndex(a):
    return magicHelper(a,0,len(a)-1)

def magicHelper(a,start,end):
    mid=int((start+end)/2)

    if start>end:
        return -1
    elif a[mid]==mid:
        return mid
    elif a[mid]>mid:
        return magicHelper(a,start,mid-1)
    elif a[mid]<mid:
        return magicHelper(a,mid+1,end)

# print(magicIndex(a))


p=[1,2,3,4]

def powerSet(p):
    return powerSetHelper(p,0)

def powerSetHelper(p,index):
    allSubsets=[]
    if index==len(p):
        return [[]]
    else:
        allSubsets=powerSetHelper(p,index+1)
        moreSubsets=[]
        item=p[index]
        for each in allSubsets:
            moreSubsets.append([item]+each)
        allSubsets.extend(moreSubsets)

    return allSubsets


# print(powerSet(p))


s='abca'

def permDups(s):
    return permDupsHelper(s,0)

def permDupsHelper(s,index):
    if index==len(s)-1:
        return [s[len(s)-1]]
    else:
        allSubsets=permDupsHelper(s,index+1)
        item=s[index]
        moreSubsets=[]
        for each in allSubsets:
            moreSubsets.extend(stringCombinations(item,each))
        allSubsets=moreSubsets
    return allSubsets


def stringCombinations(c,s):
    t=[]
    for i in range(0,len(s)+1):
        k=s[:i]+c+s[i:]
        if k not in t:
            t.append(s[:i]+c+s[i:])
    return t

# print(permDups(s))


n=3

def paran(n):
    if n==1:
        return ['()']
    else:
        allSubsets=paran(n-1)
        moreSubsets=[]
        for each in allSubsets:
            moreSubsets.extend(paranHelper(each))
        allSubsets=moreSubsets
    return allSubsets

def paranHelper(s):
    t=[]
    for i,each in enumerate(s):
        temp=s[:i]+'()'+s[i:]
        if temp not in t:
            t.append(temp)
    return t


# print(paran(3))

matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
def paintFill(matrix):
    if not matrix:
        return None
    else:
        return paintFillHelper(matrix,0,0)

def paintFillHelper(matrix,row,col):
    if row>=len(matrix) or row<0 or col>=len(matrix[0]) or col<0:
        return False
    else:
        if matrix[row][col]!=12:
            matrix[row][col]=12
            paintFillHelper(matrix,row+1,col)
            paintFillHelper(matrix,row,col+1)
            paintFillHelper(matrix,row-1,col)
            paintFillHelper(matrix,row,col-1)
        return True
# paintFill(matrix)
# print(matrix)


def paintFillMemo(matrix):
    if not matrix:
        return None
    else:
        m={}
        return paintFillMemoHelper(matrix,0,0,m)

def paintFillMemoHelper(matrix,row,col,memo):
    if row>=len(matrix) or row<0 or col>=len(matrix[0]) or col<0:
        return False
    if (row,col) in memo:
        return memo[(row,col)]
    else:
        if matrix[row][col]!=12:
            paintFillMemoHelper(matrix,row+1,col,memo)
            paintFillMemoHelper(matrix,row-1,col,memo)
            paintFillMemoHelper(matrix,row,col+1,memo)
            paintFillMemoHelper(matrix,row,col-1,memo)
            memo[(row,col)]=True
    return memo[(row,col)]

# paintFillMemo(matrix)
# print(matrix)

def coinChangeWays(n):
    return coinChangeHelper(n,[1,5,10,25])

def coinChangeHelper(n,w):
    ways=0
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        for each in w:
            ways=ways+coinChangeHelper(n-each,w)
    return ways

print(coinChangeWays(5))


def coinChangeWaysMemo(n):
    m={}
    return coinChangeHelperMemo(n,[1,5,10,25],0,m)

def coinChangeHelperMemo(n,coins,index,m):
    if (n,index) in m:
        return m[(n,index)]

    if index>=len(coins)-1:
        return 1
    ways =0

    i=0
    coin=coins[index]
    while(i*coin<=n):
        amountRemaining=n-(i*coin)
        ways=ways+coinChangeHelperMemo(amountRemaining,coins,index+1,m)
        i+=1
    m[(n,index)]=ways
    return ways

print(coinChangeWaysMemo(5))





