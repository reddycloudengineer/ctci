a=['abc']

#output - ['','c','bc','cb','abc','bca','bac','acb','cba','cab']

#ab [0,1] + c
# c-start and c-end

def permute(a):
    allPermutations=[]
    if len(a)==1:
        return [a]
    else:
        firstchar=a[0]
        morePermutations=permute(a[1:])
        for each in morePermutations:
            # for perm in permuteHelper(firstchar,each):
            #     if perm not in allPermutations:
            allPermutations.extend(permuteHelper(firstchar,each))
    return allPermutations



def permuteHelper(firstchar,actualstring):
    permuations=[]
    for i in range(0,len(actualstring)+1):
        permuations.append(actualstring[0:i]+firstchar+actualstring[i:])
    return permuations

# print(permute('abcc'))

maze=[[]]
def getPath(maze):
    return getPathHelper(maze,0,0)
def getPathHelper(maze,r,c):
    if r>len(maze) or c>len(maze[0]):
            return False
    else:
        reachedTarget=(r==len(maze)) and (c==len(maze[0]))
        if getPathHelper(maze,r+1,c) or getPathHelper(maze,r,c+1) or reachedTarget:
            return True
    return False

maze=[[]]

def getPath(maze):
    path=[]
    r,c=0,0
    return getPathHelper(maze,r,c,path)

def getPathHelper(maze,r,c,path):
    if r>len(maze) or c>(len(maze[0])):
        return False
    else:
        reachedTarget=(r==len(maze)) and (c==len(maze[0]))
        if reachedTarget or getPathHelper(maze,r,c,path) or getPathHelper(maze,r,c,path):
            path.append((r,c))
            return True
    return False

maze=[[]]

def getPath(maze):
    path=[]
    r,c=0,0
    failedpoints=[]
    return getPathHelperMemo(maze,r,c,path,failedpoints)

def getPathHelperMemo(maze,r,c,path,failedpoints):
    if r>len(maze) or c>len(maze[0]):
        return False
    else:
        if (r,c) in failedpoints:
            return False
        reachedTarget=(r==len(maze)) and (c==len(maze[0]))
        if reachedTarget or getPathHelper(maze,r+1,c,failedpoints) or getPathHelper(maze,r,c+1,failedpoints):
            path.append((r,c))
            return True
        failedpoints.append((r,c))
        return False

l=[-40,-20,-1,1,2,3,5,7,9,12,13]
def magicIndex(l):
    return indexHelper(l,0,len(l)-1)
def indexHelper(l,start,end):
    mid=(start+end)/2
    if start>end:
        return -1

    if l[mid]==mid:
        return mid

    elif l[mid]>mid:
        return indexHelper(l,start,mid-1)
    elif l[mid]<mid:
        return indexHelper(l,mid+1,end)


l=[1,2,3,4]
def powerSet(l):
    return powerSetHelper(l,0)

def powerSetHelper(l,index):
    allSubsets=[]
    if index>=len(l):
        return [[]]
    else:
        allSubsets=powerSetHelper(l,index+1)
        moreSubsets=[]
        item=l[index]
        for each in allSubsets:
            moreSubsets.append([item]+each)
        allSubsets.extend(moreSubsets)

    return allSubsets

# print(powerSet(l))


s='abcd'
def permutewithdups(s):
    return permutewithdupshelper(s,0)

def permutewithdupshelper(s,index):
    if index==len(s):
        return ['']
    else:
        allPermutations=permutewithdupshelper(s,index+1)
        morePermutattions=[]
        item=s[index]
        for each in allPermutations:
            morePermutattions.extend(stringCombinations(each,item))
        allPermutations=morePermutattions
    return allPermutations

def permutewithoutduphelper(s,index):
    if index==len(s):
        return ['']
    else:
        allPermutations=permutewithoutduphelper(s,index+1)
        morePermutations=[]
        item=s[index]
        for each in allPermutations:
            morePermutations.extend(stringCombinationswithoutdups(each,item))
        allPermutations=morePermutations
    return allPermutations

def stringCombinationswithoutdups(s, char):
    c = []
    if len(s) == 0:
        c.append(s + char)
    else:
        for i in range(0, len(s) + 1):
            if s[:i]+char+s[i:] not in c:
                c.append(s[:i] + char + s[i:])
    return c

def stringCombinations(s,char):
    c=[]
    if len(s)==0:
        c.append(s+char)
    else:
        for i in range(0,len(s)+1):
            print('inside for loop',s[:i]+char+s[i:])
            c.append(s[:i]+char+s[i:])
    return c


# print(permutewithdups('abcd'))

print(permutewithoutduphelper('aacd',0))



n=3
def paranrec(n):
    allPermutations=[]
    if n==1:
        return ['()']
    else:
        morePermutations=[]
        for each in allPermutations:
            pass

#####Eight queens #########

        